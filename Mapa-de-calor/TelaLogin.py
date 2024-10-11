import customtkinter
from PIL import Image, ImageTk
import io
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

# Função para alternar a visibilidade da senha
def alternar_visibilidade():
    global senha_visivel

    if senha_visivel:
        senha.configure(show="*")
        botao_espia.configure()     # texto do olho
        senha_visivel = False
    else:
        senha.configure(show="")
        botao_espia.configure()     # texto do olho
        senha_visivel = True

# Função que será chamada ao clicar no botão login
def chama_janela2():
    email_input = email.get()      # Pega o E-mail digitado pelo usuario
    senha_input = senha.get()      # Pega a senha digitado pelo usuario

    if email_input == "gabrielguedes00@hotmail.com" and senha_input == "12345":
        janela.withdraw()           # Janela se recolher 
        janela2.deiconify()         # Mostrar a janela, caso esteja oculta ou minimizada
    else: 
        texto2.configure(text="Dados de login incorretos", text_color="red", font=("Arial", 20))
        janela.after(1000, atualizar_tela)  # Atualizar a tela após 1 segundos 
    
# Função que será chamada ao clicar no botão "Cadastre-se"
def chama_janela_cadastro():
    janela.withdraw()                 # Janela se recolher 
    janela3.deiconify()               # Mostrar a janela, caso esteja oculta ou minimizada

# Carregar a imagem do logo
logo = Image.open("UNIFESO.png")  # Substitua pelo caminho da sua imagem
logo = logo.resize((500, 181), Image.LANCZOS)                   # Redimensiona a imagem, se necessário
logo_tk = ImageTk.PhotoImage(logo)

# Criação dos componentes da Tela principal
janela.configure(bg="#000000")                                      # Fundo preto 
frame_central = customtkinter.CTkFrame(janela, fg_color="#000000")  
frame_central.pack(expand=True, fill="both")                        # Expandir a tela

# Adicionando a imagem do logo
logo_label = customtkinter.CTkLabel(frame_central, image=logo_tk, text="")
logo_label.pack(pady=10)

# Texto superior de "mapa de calor"
texto = customtkinter.CTkLabel(frame_central, text="HeatMap", text_color = "green", font=("Arial", 20))
texto.pack(pady=20)

# Label de E-mail 
email = customtkinter.CTkEntry(frame_central, placeholder_text="E-mail", width=250)
email.pack(pady=10)

# Campo de senha 
senha_frame = customtkinter.CTkFrame(frame_central, width=250)
senha_frame.pack(pady=10)

# Label da senha com criptografia da senha 
senha = customtkinter.CTkEntry(senha_frame, placeholder_text="Senha", show="*", width=200)
senha.pack(side="left")

# Botão para alternar visibilidade da senha (olho)
botao_espia = customtkinter.CTkButton(senha_frame, image=eye_closed_icon, width=20, command=alternar_visibilidade, text="")
botao_espia.pack(side="left")

# Botão de login
botao_loguin = customtkinter.CTkButton(frame_central, text="Login", command = chama_janela2, width=200)
botao_loguin.pack(pady=10)

# Botão de cadastro
botao_cadastro = customtkinter.CTkButton(frame_central, text="Cadastre-se", width=200)
botao_cadastro.pack(pady=10)

# Texto de "Dados de login incorretos"
texto2 = customtkinter.CTkLabel(frame_central, text="")
texto2.pack(pady=10)

# Início do loop principal da interface gráfica
janela.mainloop()
