import mysql.connector
from mysql.connector import Error

def conn():
    try:
        # Configurações de conexão
        connection = mysql.connector.connect(
            host="34.39.138.35",
            user="DEV",
            password="E3s1XxiTp(vU%pY",
            database="DB_HEATMAP",
            port=3306
        )

        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
        

def fechar_conexao(connection):
    """ Função para fechar a conexão de forma segura """
    if connection and connection.is_connected():
        connection.close()
        print("Conexão ao MySQL foi encerrada.")