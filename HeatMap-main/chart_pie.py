import matplotlib.pyplot as plt
from conexao import conn

# Obtém a conexão ao banco de dados
connection = conn()

try:
    if connection:
        cursor = connection.cursor(dictionary=True)

        # Consulta para dispositivos
        cursor.execute("SELECT DISPOSITIVO, COUNT(*) AS total FROM LOCALIZACAO GROUP BY DISPOSITIVO")
        dispositivos_data = cursor.fetchall()

        # Consulta para sistemas operacionais
        cursor.execute("SELECT SISTEMA_OPERACIONAL, COUNT(*) AS total FROM LOCALIZACAO GROUP BY SISTEMA_OPERACIONAL")
        so_data = cursor.fetchall()

        # Consulta para navegadores
        cursor.execute("SELECT NAVEGADOR, COUNT(*) AS total FROM LOCALIZACAO GROUP BY NAVEGADOR")
        navegador_data = cursor.fetchall()

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

# Função para extrair dados para gráficos
def extract_data(data, key_label, key_value):
    labels = [row[key_label] for row in data]
    values = [row[key_value] for row in data]
    return labels, values

# Dados para os gráficos
labels_dispositivos, values_dispositivos = extract_data(dispositivos_data, 'DISPOSITIVO', 'total')
labels_so, values_so = extract_data(so_data, 'SISTEMA_OPERACIONAL', 'total')
labels_navegador, values_navegador = extract_data(navegador_data, 'NAVEGADOR', 'total')

# Gráfico de Pizza - Dispositivos
plt.figure(figsize=(6, 6))  # Cria uma nova figura para o gráfico de dispositivos
plt.pie(values_dispositivos, labels=labels_dispositivos, autopct='%1.1f%%', startangle=140)
plt.title('Dispositivos')
plt.tight_layout()  # Ajusta o layout para remover espaços desnecessários
plt.savefig('grafico_dispositivos.png')  # Salva o gráfico como imagem
plt.close()  # Fecha o gráfico para não sobrepor os próximos

# Gráfico de Pizza - Sistemas Operacionais
plt.figure(figsize=(6, 6))  # Cria uma nova figura para o gráfico de sistemas operacionais
plt.pie(values_so, labels=labels_so, autopct='%1.1f%%', startangle=140)
plt.title('Sistemas Operacionais')
plt.tight_layout()  # Ajusta o layout para remover espaços desnecessários
plt.savefig('grafico_sistemas_operacionais.png')  # Salva o gráfico como imagem
plt.close()  # Fecha o gráfico para não sobrepor os próximos

# Gráfico de Pizza - Navegadores
plt.figure(figsize=(6, 6))  # Cria uma nova figura para o gráfico de navegadores
plt.pie(values_navegador, labels=labels_navegador, autopct='%1.1f%%', startangle=140)
plt.title('Navegadores')
plt.tight_layout()  # Ajusta o layout para remover espaços desnecessários
plt.savefig('grafico_navegadores.png')  # Salva o gráfico como imagem
plt.close()  # Fecha o gráfico para não sobrepor os próximos

# Exibe os gráficos se desejar (opcional)
# plt.show()  # Somente se quiser exibir os gráficos após salvar
