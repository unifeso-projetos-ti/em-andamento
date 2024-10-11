import pandas as pd
import matplotlib.pyplot as plt
import io
import matplotlib
matplotlib.use('Agg')

def plotar_grafico(Arquivo_csv, pizza=True):

    analise = pd.read_csv(Arquivo_csv)
    # Calculando a média das notas por curso
    notas_medias_curso = analise.groupby('curso')['nota da materia'].mean().reset_index()
    notas_medias_curso['nota da materia'] = notas_medias_curso['nota da materia'].round(2)

    # Renomeando as colunas
    notas_medias_curso.columns = ['Curso', 'Média das Notas']

    img = io.BytesIO()  # Cria um buffer de memória para armazenar a imagem

    if pizza:
        # Gráfico de pizza
        plt.figure(figsize=(6, 3))
        plt.pie(notas_medias_curso['Média das Notas'], labels=notas_medias_curso['Curso'], autopct='%1.1f%%',
                startangle=140, colors=plt.cm.Paired(range(len(notas_medias_curso))))
        plt.title('Distribuição das Médias das Notas por Curso')

    else:
        # Gráfico em barra
        plt.figure(figsize=(8, 4))
        plt.bar(notas_medias_curso['Curso'], notas_medias_curso['Média das Notas'], color='skyblue')
        plt.xlabel('Curso')
        plt.ylabel('Média das Notas')
        plt.title('Média das Notas por Curso')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

    plt.savefig(img, format='png')  # Salva o gráfico no buffer em formato PNG
    img.seek(0)  # Volta para o início do buffer
    plt.close()  # Fecha o gráfico para liberar memória

    return img  # Retorna a imagem
