import matplotlib.pyplot as plt
from conexao import conn


# Função para obter dados de conexão a partir da tabela LOCALIZACAO
def get_connection_data():
    connection = conn()

    try:
        if connection:
            cursor = connection.cursor(dictionary=True)

            # Consulta para identificar redes Wi-Fi
            cursor.execute("""
                SELECT IP_ALUNO, COUNT(DISTINCT MATRICULA) AS matriculas_distintas
                FROM LOCALIZACAO
                GROUP BY IP_ALUNO
            """)
            ip_data = cursor.fetchall()

            wi_fi_count = 0
            mobile_count = 0

            for row in ip_data:
                if row['matriculas_distintas'] > 2:
                    wi_fi_count += 1  # Rede Wi-Fi
                else:
                    mobile_count += 1  # Rede Móvel

            return wi_fi_count, mobile_count

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Função para calcular o percentual
def calcular_percentual(wi_fi_count, mobile_count):
    total = wi_fi_count + mobile_count
    percentual_wifi = (wi_fi_count / total) * 100
    percentual_mobile = (mobile_count / total) * 100
    return percentual_wifi, percentual_mobile


# Função para gerar o gráfico
def gerar_grafico(wi_fi_count, mobile_count):
    labels = ['Rede Wi-Fi', 'Rede Móvel']
    valores = [wi_fi_count, mobile_count]

    plt.figure(figsize=(6, 6))
    plt.pie(valores, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#00aaff', '#ffaa00'])
    plt.title('Percentual de Conexão por Tipo de Rede')
    plt.tight_layout()
    plt.savefig('conexao_rede.png')  # Salva a imagem do gráfico
    plt.show()


# Executando o processo
wi_fi_count, mobile_count = get_connection_data()
percentual_wifi, percentual_mobile = calcular_percentual(wi_fi_count, mobile_count)
print(f"Percentual de Rede Wi-Fi: {percentual_wifi:.2f}%")
print(f"Percentual de Rede Móvel: {percentual_mobile:.2f}%")

# Geração do gráfico
gerar_grafico(wi_fi_count, mobile_count)
