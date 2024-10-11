import re
from django.core.mail import send_mail
from django.conf import settings

from django.db import connection, transaction
from django.utils.html import escape
from django.shortcuts import get_object_or_404


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .serializers import *
from core.utils.util import *


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request: Request) -> Response:
    required_fields = ['username', 'first_name', 'email', 'password', 'zip_code']
    missing_fields = [field for field in required_fields if not request.data.get(field)]

    if missing_fields:
        return Response(
            {"msg": f"Por favor, informe os seguintes campos: {', '.join(missing_fields)}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name', '')
    email = request.data.get('email')
    password = request.data.get('password')
    zip_code = request.data.get('zip_code')

    if not email_validator(email):
        return Response({"msg": "Email inválido"}, status=status.HTTP_400_BAD_REQUEST)

    if not username_validator(username):
        return Response({"msg": "Nome de usuário inválido"}, status=status.HTTP_400_BAD_REQUEST)

    if not zip_code_validator(zip_code):
        return Response({"msg": "CEP inválido"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        geo_location = get_geo_location(zip_code)
        if not geo_location.get('items'):
            return Response(
                {"msg": "Não foi possível obter a geolocalização para o CEP informado."},
                status=status.HTTP_400_BAD_REQUEST
            )
        geo_data = geo_location['items'][0]
        address = geo_data.get('address', {})
        position = geo_data.get('position', {})
    except Exception as e:
        return Response(
            {"msg": "Erro ao obter geolocalização.", "error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password
    )

    address_instance = Address.objects.create(
        usuario=user,
        cep=zip_code,
        cidade=address.get('city', ''),
        estado=address.get('state', ''),
        pais=address.get('countryName', ''),
        latitude=position.get('lat', 0.0),
        longitude=position.get('lng', 0.0)
    )

    return Response({"msg": "Usuário cadastrado com sucesso!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_address(request: Request) -> Response:
    address = Address.objects.filter(usuario=request.user)
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_event(request: Request) -> Response:
    required_fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'zip_code_event', 'quantidade_ticket', 'valor_ticket']
    missing_fields = [field for field in required_fields if not request.data.get(field)]

    if missing_fields:
        return Response(
            {"msg": f"Por favor, informe os seguintes campos: {', '.join(missing_fields)}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    nome = request.data.get('nome')
    descricao = request.data.get('descricao')
    data_inicio = request.data.get('data_inicio')
    data_fim = request.data.get('data_fim')
    zip_code_event = request.data.get('zip_code_event')
    quantidade_ticket = request.data.get('quantidade_ticket')
    valor_ticket = request.data.get('valor_ticket')

    try:
        geo_location = get_geo_location(zip_code_event)
        if not geo_location.get('items'):
            return Response(
                {"msg": "Não foi possível obter a geolocalização para o CEP informado."},
                status=status.HTTP_400_BAD_REQUEST
            )
        geo_data = geo_location['items'][0]
        address = geo_data.get('address', {})
        position = geo_data.get('position', {})
    except Exception as e:
        return Response(
            {"msg": "Erro ao obter geolocalização.", "error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    event = Events.objects.create(
        nome=nome,
        descricao=descricao,
        data_inicio=data_inicio,
        data_fim=data_fim
    )
    event_address = EventAddress.objects.create(
        evento=event,
        cidade=address.get('city', ''),
        estado=address.get('state', ''),
        pais=address.get('countryName', ''),
        cep=zip_code_event,
        latitude=position.get('lat', 0.0),
        longitude=position.get('lng', 0.0)
    )
    ticket = Tickets.objects.create(
        evento=event,
        quantidade=quantidade_ticket,
        valor=valor_ticket
    )

    return Response({"msg": "Evento criado com sucesso!"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def email_sender(request: Request) -> Response:
    email = request.query_params.get("email")
    assunto = request.data.get("assunto")
    mensagem = request.data.get("mensagem")

    validate = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email or not re.match(validate, email):
        return Response({"message": "Email inválido"}, status=status.HTTP_400_BAD_REQUEST)

    subject = assunto
    message = mensagem

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        return Response({"message": f"Falha ao enviar o email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({"msg": "Email enviado com sucesso!"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events(request: Request) -> Response:
    events = Events.objects.all()
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_event(request: Request) -> Response:
    event_id = request.query_params.get("event_id")
    event = get_object_or_404(Events, id=event_id)
    serializer = EventsSerializer(event)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_for_description(request: Request) -> Response:
    description = request.query_params.get("description")
    events = Events.objects.filter(descricao__icontains=description)
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_for_init_date(request: Request) -> Response:
    data_inicio = request.query_params.get("data_inicio")
    events = Events.objects.filter(data_inicio=data_inicio)
    serializer = EventsSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_for_country(request: Request) -> Response:
    country = request.query_params.get("country")
    events = EventAddress.objects.filter(pais=country)
    serializer = EventAddressSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_for_state(request: Request) -> Response:
    state = request.query_params.get("state")
    events = EventAddress.objects.filter(estado=state)
    serializer = EventAddressSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_for_city(request: Request) -> Response:
    city = request.query_params.get("city")
    events = EventAddress.objects.filter(cidade=city)
    serializer = EventAddressSerializer(events, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_events_for_coordinates_user(request: Request) -> Response:
    user_id = request.query_params.get("user_id")
    user_address = Address.objects.filter(usuario_id=user_id).first()
    if not user_address:
        return Response(
            {"msg": "Usuário não encontrado"},
            status=status.HTTP_404_NOT_FOUND
        )

    user_latitude = float(user_address.latitude)
    user_longitude = float(user_address.longitude)
    user_coords = [user_longitude, user_latitude]

    events = Events.objects.all()
    event_data = []
    locations = [user_coords]

    for event in events:
        event_address = EventAddress.objects.filter(evento=event).first()
        if event_address:
            lat = float(event_address.latitude)
            lon = float(event_address.longitude)
            locations.append([lon, lat])
            event_data.append({
                'event': event,
                'address': event_address
            })
        else:
            continue

    if len(locations) > 40:
        return Response(
            {"msg": "Número de eventos excede o limite permitido para cálculo de distâncias."},
            status=status.HTTP_400_BAD_REQUEST
        )

    api_key = settings.OPENROUTESERVICE_API_KEY
    url = 'https://api.openrouteservice.org/v2/matrix/driving-car'
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json; charset=utf-8'
    }
    payload = {
        "locations": locations,
        "metrics": ["distance"],
        "units": "km",
        "sources": [0],
        "destinations": list(range(1, len(locations)))
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        if 'error' in data:
            return Response(
                {"msg": "Erro na API de roteamento.", "error": data['error']},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        distances = data['distances'][0]

        if len(distances) != len(event_data):
            return Response(
                {"msg": "Erro ao processar distâncias retornadas pela API."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        for idx, event_info in enumerate(event_data):
            distance = distances[idx]
            event_info['distance'] = distance if distance is not None else None

    except requests.exceptions.HTTPError as http_err:
        return Response(
            {"msg": "Erro HTTP ao acessar a API de roteamento.", "error": str(http_err)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    except Exception as err:
        return Response(
            {"msg": "Erro ao calcular distâncias.", "error": str(err)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    sorted_events = sorted(event_data, key=lambda x: x['distance'] if x['distance'] is not None else float('inf'))

    serialized_events = []
    for event_info in sorted_events:
        event = event_info['event']
        event_address = event_info['address']
        distance = event_info['distance']

        event_serializer = EventsSerializer(event)
        event_data_serialized = event_serializer.data

        if distance is not None:
            event_data_serialized['distance'] = round(distance, 2)
        else:
            event_data_serialized['distance'] = None

        event_data_serialized['event_address'] = {
            'cidade': event_address.cidade,
            'estado': event_address.estado,
            'pais': event_address.pais,
            'cep': event_address.cep,
            'latitude': event_address.latitude,
            'longitude': event_address.longitude
        }

        serialized_events.append(event_data_serialized)

    return Response(serialized_events, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def update_event(request: Request, event_id: str) -> Response:
    event = get_object_or_404(Events, id=event_id)
    event.nome = request.data.get('nome', event.nome)
    event.descricao = request.data.get('descricao', event.descricao)
    event.data_inicio = request.data.get('data_inicio', event.data_inicio)
    event.data_fim = request.data.get('data_fim', event.data_fim)
    event.save()
    return Response(
        {"msg": "Evento atualizado com sucesso!"},
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_event(request: Request, event_id: str) -> Response:
    event = get_object_or_404(Events, id=event_id)
    event.delete()
    return Response(
        {"msg": "Evento deletado com sucesso!"},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_event_address(request: Request, event_id: str) -> Response:
    event_address = EventAddress.objects.filter(evento_id=event_id)
    serializer = EventAddressSerializer(event_address, many=True)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )

@api_view(['PUT'])
@permission_classes([AllowAny])
def update_event_address(request: Request, event_id: str) -> Response:
    event_address = get_object_or_404(EventAddress, evento_id=event_id)
    event_address.cidade = request.data.get('cidade', event_address.cidade)
    event_address.estado = request.data.get('estado', event_address.estado)
    event_address.pais = request.data.get('pais', event_address.pais)
    event_address.cep = request.data.get('cep', event_address.cep)
    event_address.save()
    return Response(
        {"msg": "Endereço do evento atualizado com sucesso!"},
        status=status.HTTP_200_OK
    )

@api_view(['GET'])
@permission_classes([AllowAny])
def get_tickets(request: Request, event_id: str) -> Response:
    tickets = Tickets.objects.filter(evento_id=event_id)
    serializer = TicketsSerializer(tickets, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([AllowAny])
def update_tickets(request: Request, event_id: str) -> Response:
    tickets = get_object_or_404(Tickets, evento_id=event_id)
    tickets.quantidade = request.data.get('quantidade', tickets.quantidade)
    tickets.valor = request.data.get('valor', tickets.valor)
    tickets.save()
    return Response(
        {"msg": "Ingressos atualizados com sucesso!"},
        status=status.HTTP_200_OK
    )


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_tickets(request: Request, event_id: str) -> Response:
    tickets = get_object_or_404(Tickets, evento_id=event_id)
    tickets.delete()
    return Response(
        {"msg": "Ingressos deletados com sucesso!"},
        status=status.HTTP_200_OK
    )


# Cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request: Request) -> Response:
    required_fields = ['product_id', 'quantity']
    missing_fields = [field for field in required_fields if not request.data.get(field)]

    if missing_fields:
        return Response(
            {"msg": f"Por favor, informe os seguintes campos: {', '.join(missing_fields)}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')

    product = get_object_or_404(Tickets, id=product_id)
    total = product.valor * quantity

    cart = Cart.objects.create(
        usuario=request.user,
        produto=product,
        quantidade=quantity,
        valor=product.valor,
        total=total
    )

    return Response({"msg": "Produto adicionado ao carrinho com sucesso!"}, status=status.HTTP_201_CREATED)

# daqui pra baixo não tem url
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart(request: Request) -> Response:
    cart = Cart.objects.filter(usuario=request.user)
    serializer = CartSerializer(cart, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_cart_total(request: Request) -> Response:
    cart = Cart.objects.filter(usuario=request.user)
    total = sum([item.total for item in cart])
    return Response({"total": total}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_cart(request: Request, cart_id: str) -> Response:
    cart = get_object_or_404(Cart, id=cart_id)
    cart.delete()
    return Response(
        {"msg": "Produto removido do carrinho com sucesso!"},
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_admin_user(request: Request) -> Response:
    required_fields = ['username', 'first_name', 'email', 'password']
    missing_fields = [field for field in required_fields if not request.data.get(field)]

    if missing_fields:
        return Response(
            {"msg": f"Por favor, informe os seguintes campos: {', '.join(missing_fields)}"},
            status=status.HTTP_400_BAD_REQUEST
        )

    username = request.data.get('username')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name', '')
    email = request.data.get('email')
    password = request.data.get('password')

    if not email_validator(email):
        return Response(
            {"msg": "Email inválido"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not username_validator(username):
        return Response(
            {"msg": "Nome de usuário inválido"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        is_staff=True
    )

    return Response(
        {"msg": "Usuário administrador criado com sucesso!"},
        status=status.HTTP_201_CREATED
    )
