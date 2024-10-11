import customtkinter
from PIL import Image, ImageTk
import os

# Configurações iniciais do CustomTkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


# Função para converter PNG para PhotoImage
def png_para_photo(caminho_png, tamanho=(20, 20)):
    if not os.path.isfile(caminho_png):
        raise FileNotFoundError(f"Arquivo PNG não encontrado: {caminho_png}")
    
    try:
        imagem = Image.open(caminho_png).resize(tamanho)
        return ImageTk.PhotoImage(imagem)
    except Exception as e:
        print(f"Erro ao carregar PNG: {e}")
        return None

# Função para alternar a visibilidade da senha
def alternar_visibilidade():
    global senha_visivel

    if senha_visivel:
        senha.configure(show="*")
        botao_espia.configure(image=eye_closed_icon)
        senha_visivel = False
    else:
        senha.configure(show="")
        botao_espia.configure(image=eye_open_icon)
        senha_visivel = True


# Função para maximizar a janela
def maximizar_janela(janela):
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))  # Ocupa a tela inteira  

# Função de atualização da tela
def atualizar_tela():

    # Limpar campos de entrada e mensagem de erro
    email.delete(0, 'end')
    senha.delete(0, 'end')
    texto2.configure(text="")

# Criação da tela de login:
janela = customtkinter.CTk()
maximizar_janela(janela)  # Aplica a função de maximizar a janela

# Criação da segunda tela, que será ocultada inicialmente
janela2 = customtkinter.CTk()
maximizar_janela(janela2)  # Aplica a função de maximizar a janela
janela2.withdraw()         # Janela se recolher

# Criação da terceira tela, que será ocultada inicialmente
janela3 = customtkinter.CTk()
maximizar_janela(janela3)  # Aplica a função de maximizar a janela
janela3.withdraw()         # Janela se recolher

# Caminho dos arquivos PNG (ajuste conforme necessário)
eye_open_image_path   = "eye-open.png"
eye_closed_image_path = "eye-closed.png"


# Converter PNG e criar objetos PhotoImage
eye_open_icon   = png_para_photo(eye_open_image_path)
eye_closed_icon = png_para_photo(eye_closed_image_path)

if eye_open_icon is None or eye_closed_icon is None:
    raise SystemExit("Não foi possível carregar os ícones. Verifique os arquivos PNG.")

# Variável para controlar se a senha está visível ou não
senha_visivel = False

# Função que será chamada ao clicar no botão login
def chama_janela2():
    email_input = email.get()      # Pega o E-mail digitado pelo usuario
    senha_input = senha.get()      # Pega a senha digitado pelo usuario
    
    if email_input == "gabrielguedes00@hotmail.com" and senha_input == "12345":
        janela.withdraw()           # Janela se recolher 
        janela2.deiconify()         # Mostrar a janela, caso esteja oculta ou minimizada
    else: 
        texto2.configure(text="Dados de login incorretos", text_color="red", font=("Arial", 20))
        janela.after(1000, atualizar_tela)  # Atualizar a tela após 1 segundo
   

# Função para cadastrar um novo usuário
def chama_janela_cadastro():
    janela.withdraw()                       # Janela se recolher 
    janela3.deiconify()                     # Mostrar a janela, caso esteja oculta ou minimizada
    nome_usuario = nome.get()
    email_usuario = email_cadastro.get()
    senha_usuario = senha_cadastro.get()

    if nome_usuario and email_usuario and senha_usuario:
        # Aqui você pode implementar a lógica para salvar o usuário no banco de dados
        print(f"Usuário {nome_usuario} cadastrado com sucesso!")
        texto_cadastro.configure(text="Cadastro realizado com sucesso!", text_color="green")
        # Após o cadastro, você pode limpar os campos
        nome.delete(0, 'end')
        email_cadastro.delete(0, 'end')
        senha_cadastro.delete(0, 'end')
    else:
        texto_cadastro.configure(text="Preencha todos os campos", text_color="red")

# Configurações da janela de cadastro
janela3.configure(bg="#000000")

frame_cadastro = customtkinter.CTkFrame(janela3, fg_color="#000000")
frame_cadastro.pack(expand=True, fill="both")

# Texto superior
texto_cadastro_titulo = customtkinter.CTkLabel(frame_cadastro, text="Cadastro de Usuário", text_color="green", font=("Arial", 20))
texto_cadastro_titulo.pack(pady=20)

# Campo para Nome do usuário
nome = customtkinter.CTkEntry(frame_cadastro, placeholder_text="Nome", width=250)
nome.pack(pady=10)

# Campo para E-mail do usuário
email_cadastro = customtkinter.CTkEntry(frame_cadastro, placeholder_text="E-mail", width=250)
email_cadastro.pack(pady=10)

# Campo para Celular do usuário
email_cadastro = customtkinter.CTkEntry(frame_cadastro, placeholder_text="Celular", width=250)
email_cadastro.pack(pady=10)

# Campo para Senha do usuário
senha_cadastro = customtkinter.CTkEntry(frame_cadastro, placeholder_text="Senha", show="*", width=250)
senha_cadastro.pack(pady=10)

# Campo para Confirmar a Senha do usuário
senha_cadastro = customtkinter.CTkEntry(frame_cadastro, placeholder_text="Confirmar a Senha", show="*", width=250)
senha_cadastro.pack(pady=10)

# Botão para realizar o cadastro
botao_cadastro_usuario = customtkinter.CTkButton(frame_cadastro, text="Cadastrar", command=chama_janela_cadastro, width=250)
botao_cadastro_usuario.pack(pady=10)


# Botão para voltar à tela de login
botao_voltar_login = customtkinter.CTkButton(frame_cadastro, text="Voltar ao Login", command=lambda: [janela3.withdraw(), janela.deiconify()], width=250)
botao_voltar_login.pack(pady=10)


# Texto para mostrar mensagens de sucesso ou erro
texto_cadastro = customtkinter.CTkLabel(frame_cadastro, text="")
texto_cadastro.pack(pady=10)


# Carregar a imagem do logo
logo = Image.open("UNIFESO.png")  # Substitua pelo caminho da sua imagem
logo = logo.resize((250, 150), Image.LANCZOS)  # Redimensiona a imagem, se necessário
logo_tk = ImageTk.PhotoImage(logo)


# Criação dos componentes da Tela principal
janela.configure(bg="#000000")                                      # Fundo preto 
frame_central = customtkinter.CTkFrame(janela, fg_color="#000000")  
frame_central.pack(expand=True, fill="both")                        # Expandir a tela

# Adicionando a imagem do logo
logo_label = customtkinter.CTkLabel(frame_central, image=logo_tk, text="")
logo_label.pack(pady=10)

# Texto superior de "mapa de calor"
texto = customtkinter.CTkLabel(frame_central, text="HeatMap", text_color="green", font=("Arial", 20))
texto.pack(pady=20)

# Campo de E-mail 
email = customtkinter.CTkEntry(frame_central, placeholder_text="E-mail", width=250)
email.pack(pady=10)

# Frame para campo de senha e ícone de visibilidade (sem bordas)
senha_frame = customtkinter.CTkFrame(frame_central, fg_color=None, width=250)
senha_frame.pack(pady=10)

# Campo de senha
senha = customtkinter.CTkEntry(senha_frame, placeholder_text="Senha", show="*", width=200, height=30)  # Campo de senha ajustado para largura correta
senha.pack(side="left", padx=5)


# Ícone do olho embutido no campo de senha (sem bordas e hover removido)
botao_espia = customtkinter.CTkButton(senha_frame, image=eye_closed_icon, width=30, text="", fg_color=None, hover_color=None, command=alternar_visibilidade)
botao_espia.pack(side="right", padx=5)  # Adicionado padding para melhor espaçamento

# Botão de login
botao_loguin = customtkinter.CTkButton(frame_central, text="Login", command=chama_janela2, width=250)
botao_loguin.pack(pady=10)

# Botão de cadastro
botao_cadastro = customtkinter.CTkButton(frame_central, text="Cadastre-se", command=chama_janela_cadastro, width=250)
botao_cadastro.pack(pady=10)

# Texto de "Dados de login incorretos"
texto2 = customtkinter.CTkLabel(frame_central, text="")
texto2.pack(pady=10)

# Início do loop principal da interface gráfica
janela.mainloop()
