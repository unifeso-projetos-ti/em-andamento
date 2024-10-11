import os
from flask import Flask, request, redirect, url_for, render_template, make_response, send_file, Response
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify
from app.analisar_csv import plotar_grafico


app = Flask(__name__)

EXTENCOES_PERMITIDAS = {'csv'}#'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx', 'json'}
PASTA_DE_UPLOAD = './app/data'
TAMANHO_MAX_PERMITIDO = 16 * 1000 * 1000
#mostrar_grafico = True


app.config['UPLOAD_FOLDER'] = PASTA_DE_UPLOAD
app.config['MAX_CONTENT_LENGTH'] = TAMANHO_MAX_PERMITIDO

#==FUNÇÕES==============================================================================================================================

# retorna o parametro "True" se o arquivo possuir um "."(ponto no nome) e se a extenção estiver dentre as permitidas.
def arquivos_permitidos(NOME_DO_ARQUIVO):

    # verifica se o arquivo possui um "."(ponto no nome) e se a extenção está entre as permitidas.
    # a "\" encontrado nesse trecho de código tem a função de fazer a quebra de uma linha de logica e é conhecido como "line-continuation".
    if '.' in NOME_DO_ARQUIVO and \
        NOME_DO_ARQUIVO.rsplit('.', 1)[1].lower() in EXTENCOES_PERMITIDAS:
        return True

#==ROTAS================================================================================================================================

@app.route('/Login')
@app.route('/Login.html')
def Login():
    return render_template('Login.html')

@app.route('/Tela_analise')
@app.route('/Tela_analise.html')
def Tela_analise():
    nome_do_arquivo = request.args.get('nome')

    if not nome_do_arquivo:
        return "Nenhum arquivo foi selecionado.", 400

    # Renderiza a página Analise.html e passa o nome do arquivo CSV
    return render_template('Tela_analise.html', nome=nome_do_arquivo)


@app.route('/Cadastra')
@app.route('/Cadastra.html')
def Cadastra():
    return render_template('Cadastra.html')

@app.route('/Coleta', methods=['GET', 'POST'])
@app.route('/Coleta.html', methods=['GET', 'POST'])
def Coleta():
    if request.method == 'POST':
        arquivo = request.files.get('Arquivo')
        
        if not arquivo or arquivo.filename == '':
            return "Nenhum arquivo foi selecionado.", 400

        # Verifica se o arquivo é permitido
        if not arquivos_permitidos(arquivo.filename):
            return "Tipo de arquivo não permitido.", 400

        # Corrige o nome do arquivo e salva no diretório configurado
        nome_corrigido_do_arquivo = secure_filename(arquivo.filename)
        caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_corrigido_do_arquivo)
        arquivo.save(caminho_arquivo)

        # Redireciona para a página que vai mostrar o gráfico
        return redirect(url_for('Tela_analise', nome=nome_corrigido_do_arquivo))

    return render_template('Coleta.html')


@app.route('/IndexCadastrado')
@app.route('/IndexCadastrado.html')
@app.route('/indexCadastrado')
@app.route('/indexCadastrado.html')
def IndexCadastro():
    return render_template('IndexCadastrado.html')

@app.route('/')
@app.route('/Init')
@app.route('/Init.html')
def Init():
    return render_template('Index.html')

@app.route('/plot.png')
def plot_png():
    # Pega o nome do arquivo CSV via parâmetro da URL
    nome_do_arquivo = request.args.get('nome')
    
    # Verifica se o nome do arquivo foi passado
    if not nome_do_arquivo:
        return "Nome do arquivo CSV não foi fornecido.", 400

    # Cria o caminho completo para o arquivo CSV
    caminho_arquivo_csv = os.path.join(app.config['UPLOAD_FOLDER'], nome_do_arquivo)

    # Verifica se o arquivo CSV existe
    if not os.path.exists(caminho_arquivo_csv):
        return f"Arquivo CSV '{nome_do_arquivo}' não encontrado.", 404

    # Define o tipo de gráfico baseado no parâmetro 'tipo' (padrão: pizza)
    tipo_grafico = request.args.get('tipo', 'pizza')  # 'pizza' ou 'barra'
    pizza = tipo_grafico == 'pizza'

    # Chama a função plotar_grafico para gerar o gráfico
    img = plotar_grafico(caminho_arquivo_csv, pizza=pizza)

    # Retorna a imagem como resposta HTTP
    return Response(img.getvalue(), mimetype='image/png')

#=======================================================================================================================================
if __name__ == '__main__':
    app.run()