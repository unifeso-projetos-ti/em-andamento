
# def request_info(request):
#     return {
#         'Método': request.method,
#         'URL': request.url,
#         'Headers': dict(request.headers),
#         'Dados do Formulário': request.form,
#         'Parâmetros da URL': request.args,
#         # 'JSON Recebido': request.json,
#         'Cookies': request.cookies,
#         'Arquivos Enviados': {nome: arquivo.filename for nome, arquivo in request.files.items()},
#         'Dados Recebidos': request.data.decode('utf-8'),
#         'Dados': request.data,
#         'Arquivos': request.files
#     } 

# def rotina_download_de_arquivos(request=request):

        
#         #   verifica se a chave "Arquivo" existe dentro do objeto "request.files". Isso é usado para verificar se o arquivo enviado na solicitação de upload foi incluído corretamente na solicitação. Se a chave "Arquivo" não estiver presente, isso significa que o arquivo não foi incluído corretamente e a função exibe uma mensagem de erro e redireciona para a mesma página.
#         # "Arquivo" é o nome do item que será enviado, foi definido no arquivo "home.html", junto do seu tipo que será "file".
#         print("INFOS DO REQUEST")
#         print(request_info(request))
#         return
#         if 'Arquivo' not in request.files:

#             print('Não esta contido dentro do objeto.')

#             return redirect(request.url)

#         #   Adiciona o valor que corresponde a chave "Arquivo" dentro do objeto "request.files" em uma variavel para facilitar a utilização no código.
#         arquivo = request.files['Arquivo']

#         #  verifica se o usuario nao selecionou um arquivo, e caso não tenha selecionado a função retorna para a mesma pagina '/', e da um aviso no terminal.
#         if arquivo.filename == '':

#             print('Nenhum arquivo foi selecionado')

#             # o "redirect(request.url)" retorna o url de onde a pagina ja estava e pode ser subistituido por "render_template('home.html')" que retorna a pagina original tendo o mesmo efeito prático.
#             return redirect(request.url)

#         #   verifica se existe algo na variavel arquivo e se o tipo do arquivo esta dentre os permitidos para upload.
#         elif arquivo and arquivos_permitidos(arquivo.filename):

#             #if mostrar_grafico == True: 

#             #    return redirect(url_for(endpoint='show', nome=nome_do_arquivo))
            
#             #   a função "secure_filename()" converte os nomes dos arquivos para o padrão ASCII retirando irregularidades como espaços e "/" ou "\" que por exemplo poderia ser confundido como uma pasta pelo sistema, entre outras modificações.
#             #   adiciona o resultado a uma variavel para ser trabalhado
#             nome_corrigido_do_arquivo = secure_filename(arquivo.filename)

#             #   arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)), usa o método save() do objeto "arquivo" para salvar o arquivo enviado no caminho especificado pela constante UPLOAD_FOLDER configurada anteriormente no código. Essa linha também usa o método os.path.join() para garantir que o caminho do arquivo seja construído de forma correta independentemente do sistema operacional em uso.
#             arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_corrigido_do_arquivo))

#             #   "return redirect(url_for('mostre_me_o_download_do_arquivo', name=nome_corrigido_do_arquivo))"", usa a função "redirect()"" para redirecionar o usuário para a rota mostre_me_o_download_do_arquivo com o parâmetro name definido como o nome do arquivo salvo. Isso permitirá que o usuário baixe o arquivo que acabou de ser enviado.
           
#             return redirect(url_for(endpoint='show', nome=nome_corrigido_do_arquivo))

# @app.route('/Analise')
# @app.route('/Analise.html')
# def Analise():
#     nome_do_arquivo = request.args.get('nome')

#     if not nome_do_arquivo:
#         return "Nenhum arquivo foi selecionado.", 400

#     # Renderiza a página Analise.html e passa o nome do arquivo CSV
#     return render_template('Analise.html', nome=nome_do_arquivo)


# @app.route('/Analise')
# @app.route('/Analise.html')
# def Analise(nome, arquivo):
#     if nome and arquivo:
#         return render_template('Analise.html', nome=nome, arquivo=arquivo)
#     else:
#         print('sem nome e sem arquivoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
#         return render_template('Analise.html')


# @app.route('/Coleta', methods=['GET', 'POST'])
# @app.route('/Coleta.html', methods=['GET', 'POST'])
# def Coleta():
#     # verifica se o metodo da requisição é do tipo "POST".
#     if request.method == 'POST':

#         rotina_download_de_arquivos(request=request)
                
#         #   verifica se a chave "Arquivo" existe dentro do objeto "request.files". Isso é usado para verificar se o arquivo enviado na solicitação de upload foi incluído corretamente na solicitação. Se a chave "Arquivo" não estiver presente, isso significa que o arquivo não foi incluído corretamente e a função exibe uma mensagem de erro e redireciona para a mesma página.
#         # "Arquivo" é o nome do item que será enviado, foi definido no arquivo "home.html", junto do seu tipo que será "file".
#         if 'Arquivo' not in request.files:

#             print('Não esta contido dentro do objeto.')

#             return redirect(request.url)

#         #   Adiciona o valor que corresponde a chave "Arquivo" dentro do objeto "request.files" em uma variavel para facilitar a utilização no código.
#         arquivo = request.files['Arquivo']

#         #  verifica se o usuario nao selecionou um arquivo, e caso não tenha selecionado a função retorna para a mesma pagina '/', e da um aviso no terminal.
#         if arquivo.filename == '':

#             print('Nenhum arquivo foi selecionado')

#             # o "redirect(request.url)" retorna o url de onde a pagina ja estava e pode ser subistituido por "render_template('home.html')" que retorna a pagina original tendo o mesmo efeito prático.
#             return redirect(request.url)

#         #   verifica se existe algo na variavel arquivo e se o tipo do arquivo esta dentre os permitidos para upload.
#         elif arquivo and arquivos_permitidos(arquivo.filename):

#             # print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"+ request.files())

#             #if mostrar_grafico == True: 

#             #    return redirect(url_for(endpoint='show', nome=nome_do_arquivo))
            
#             #   a função "secure_filename()" converte os nomes dos arquivos para o padrão ASCII retirando irregularidades como espaços e "/" ou "\" que por exemplo poderia ser confundido como uma pasta pelo sistema, entre outras modificações.
#             #   adiciona o resultado a uma variavel para ser trabalhado
#             nome_corrigido_do_arquivo = secure_filename(arquivo.filename)
#             print(nome_corrigido_do_arquivo, arquivo)

#             #   arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)), usa o método save() do objeto "arquivo" para salvar o arquivo enviado no caminho especificado pela constante UPLOAD_FOLDER configurada anteriormente no código. Essa linha também usa o método os.path.join() para garantir que o caminho do arquivo seja construído de forma correta independentemente do sistema operacional em uso.
#             # arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_corrigido_do_arquivo))

#             #   "return redirect(url_for('mostre_me_o_download_do_arquivo', name=nome_corrigido_do_arquivo))"", usa a função "redirect()"" para redirecionar o usuário para a rota mostre_me_o_download_do_arquivo com o parâmetro name definido como o nome do arquivo salvo. Isso permitirá que o usuário baixe o arquivo que acabou de ser enviado.
#             print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
#             return redirect(url_for(endpoint='Analise', nome=nome_corrigido_do_arquivo, arquivo=arquivo))

    # return render_template('Coleta.html')


# #   essa rota deveria mostrar os arquivos que foram upados na pagina após o envio.
# @app.route('/uploads/<nome_do_arquivo>')
# def mostre_me_o_download_do_arquivo(nome_do_arquivo):
#     print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

#     return '''<iframe width="500px" height="500px" src="{{ url_for('download', nome_do_arquivo_para_ser_baixado=nome, p=False) }}"></iframe>'''


# @app.route('/plot.png')
# def plot_png(nome,arquivo):
#     # Aqui você pode carregar o arquivo CSV diretamente ou passar o caminho.
#     # Supondo que você tenha um arquivo CSV salvo em algum lugar:

#     arquivo_csv = request.args.get()
#     print("arquivo csv: "+arquivo_csv)

#     # Recebe o parâmetro da URL para definir o tipo de gráfico (pizza ou barra)
#     tipo_grafico = request.args.get('tipo', 'pizza')  # 'pizza' ou 'barra'
#     print("TIPO DE GRAFICO"+tipo_grafico)

#     # Gera o gráfico apropriado com base no parâmetro
#     img = plotar_grafico(arquivo_csv, pizza=(tipo_grafico == 'pizza'))

#     # Retorna a imagem como uma resposta HTTP
#     return Response(img.getvalue(), mimetype='image/png')

# #não preciso mexer aqui
# @app.route('/download/<nome>/<p>')
# def download(nome,p):

#     parametro = p
#     print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")

#     if parametro == 'True':

#         print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB2")

#         return send_file(plotar_grafico(f'data/{nome}',False), as_attachment=True)
    
    
#     elif parametro == 'False':
#         print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB1")

#         return send_file(plotar_grafico(f'data/{nome}',True), as_attachment=False)
    
#     else:
            
#         return 'Erro'

# @app.route('/show/<nome_do_arquivo>')
# def mostre_me_o_grafico_do_arquivo(nome_do_arquivo):

#    if request.method == "GET":

#     return send_file(f'data/{nome_do_arquivo}')


# def plotar_grafico(Arquivo_csv, pizza=True):


#     analise = pd.read_csv(Arquivo_csv)
#     # Calculando a média das notas por curso
#     notas_medias_curso = analise.groupby('curso')['nota da materia'].mean().reset_index()
#     notas_medias_curso['nota da materia'] = notas_medias_curso['nota da materia'].round(2)

#     # Renomeando as colunas
#     notas_medias_curso.columns = ['Curso', 'Média das Notas']

#     if pizza == True:
#         #gráfico de pizza
#         plt.figure(figsize=(8, 8))
#         plt.pie(notas_medias_curso['Média das Notas'], labels=notas_medias_curso['Curso'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(notas_medias_curso))))
#         plt.title('Distribuição das Médias das Notas por Curso')

#         return plt.show()

#     else:
#         #grafico em barra
#         plt.figure(figsize=(10, 6))
#         plt.bar(notas_medias_curso['Curso'], notas_medias_curso['Média das Notas'], color='skyblue')
#         plt.xlabel('Curso')
#         plt.ylabel('Média das Notas')
#         plt.title('Média das Notas por Curso')
#         plt.xticks(rotation=45, ha='right')
#         plt.tight_layout()

#         return plt.show() 
    
