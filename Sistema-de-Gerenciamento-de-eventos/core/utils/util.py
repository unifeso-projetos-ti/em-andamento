import requests
from django.contrib.auth.models import User
import re
from events.settings import API_KEY

def email_validator(email: str) -> bool:
    validate = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(email and re.match(validate, email))


def username_validator(username: str) -> bool:
    if not username or len(username) < 3:
        return False
    if User.objects.filter(username=username).exists():
        return False
    return True

def get_geo_location(zip_code: str) -> dict:
    url = f'https://geocode.search.hereapi.com/v1/geocode?q={zip_code}&apiKey={API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def zip_code_validator(cep: str) -> bool:
    if not cep or len(cep) != 8:
        return False
    return True



