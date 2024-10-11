import customtkinter
from customtkinter import CTkImage
from PIL import Image

class TelaLogin:
    def __init__(self, master):
        self.master = master
        self.frame_central = customtkinter.CTkFrame(self.master, fg_color="#000000")  # Cor de fundo da janela
        self.tela_teste = None  # Inicializar a variável para tela de teste

        # Elementos da tela de login
        self.texto          = customtkinter.CTkLabel(self.frame_central, text="HeatMap", text_color="#034d32", font=("Arial", 20))
        self.email          = customtkinter.CTkEntry(self.frame_central, placeholder_text="E-mail", width=250)
        self.senha          = customtkinter.CTkEntry(self.frame_central, placeholder_text="Senha", show="*", width=250, height=30)
        self.botao_login    = customtkinter.CTkButton(self.frame_central, fg_color="#034d32", text="Login", command=self.realizar_login, width=250)
        self.botao_cadastro = customtkinter.CTkButton(self.frame_central, fg_color="#034d32", text="Cadastre-se", width=250)
        self.texto2         = customtkinter.CTkLabel(self.frame_central, text="", text_color="#034d32", font=("Arial", 20))
        self.texto_login    = customtkinter.CTkLabel(self.frame_central, text="", text_color="#034d32", font=("Arial", 20))

        # Logo UNIFESO
        self.logo_image     = CTkImage(Image.open("UNIFESO.png"), size=(250, 150))
        self.logo_label     = customtkinter.CTkLabel(self.frame_central, image=self.logo_image, text="")
        

        # Adicionando elementos a tela 
        self.logo_label.pack(pady=10)
        self.texto.pack(pady=20)
        self.email.pack(pady=10)
        self.senha.pack(pady=10)
        self.botao_login.pack(pady=10)
        self.botao_cadastro.pack(pady=10)
        self.texto2.pack(pady=10)
        self.texto_login.pack(pady=10)

    def set_tela_teste(self, tela_teste):
        self.tela_teste = tela_teste  # Configurar a tela de teste

    def realizar_login(self):
        email_input = self.email.get()  # Pega o E-mail digitado pelo usuario
        senha_input = self.senha.get()  # Pega a senha digitado pelo usuario

        if email_input and senha_input != "": 

            if email_input == "gabrielguedes00@hotmail.com" and senha_input == "12345":
                self.texto2.configure(text="Login bem-sucedido!", text_color="green", font=("Arial", 20))
                # Mostrar a tela de teste após o login bem-sucedido
                self.ocultar()  # Oculta a tela de login
                self.tela_teste.mostrar()  # Chamando a tela de teste
                self.master.after(1000, self.atualizar_tela)  # Atualizar a tela após 1 segundo
            else:
                self.texto2.configure(text="Dados de login incorretos", text_color="red", font=("Arial", 20))
                self.master.after(1000, self.atualizar_tela)  # Atualizar a tela após 1 segundo
        
        else:
            self.texto_login.configure(text="Preencha todos os campos", text_color="red")

    def atualizar_tela(self):
        # Limpar campos de entrada e mensagem de erro
        self.email.delete(0, 'end')
        self.senha.delete(0, 'end')
        self.texto2.configure(text="")

    def mostrar(self):
        self.frame_central.pack(expand=True, fill="both")

    def ocultar(self):
        self.frame_central.pack_forget()
