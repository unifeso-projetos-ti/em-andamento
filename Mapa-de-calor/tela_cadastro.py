import customtkinter
from customtkinter import CTkImage
from tela_login import TelaLogin
#from conexao import conn
from PIL import Image

class TelaCadastro:
    def __init__(self, master, callback_voltar_login):
        self.master                 = master
        self.callback_voltar_login  = callback_voltar_login
        self.frame_central          = customtkinter.CTkFrame(self.master, fg_color="#000000") # Cor de fundo da janela 

        # Campos da tela de cadastro
        
        self.label              = customtkinter.CTkLabel(self.frame_central, text="Tela de Cadastro", text_color="#034d32", font=("Arial", 20))
        self.nome_usuario       = customtkinter.CTkEntry(self.frame_central, placeholder_text="Nome Completo", width=250)
        self.email_usuario      = customtkinter.CTkEntry(self.frame_central, placeholder_text="E-mail", width=250)
        self.celular_cadastro   = customtkinter.CTkEntry(self.frame_central, placeholder_text="Celular", width=250)
        self.senha_usuario      = customtkinter.CTkEntry(self.frame_central, placeholder_text="Senha", show="*", width=250)
        self.senha_confirma     = customtkinter.CTkEntry(self.frame_central, placeholder_text="Confirme a Senha", show="*", width=250)

        # Botões da tela de cadastro 
        self.botao_voltar       = customtkinter.CTkButton(self.frame_central, fg_color="#034d32", text="Voltar", width=250)

        # Texto para mostrar mensagens de sucesso ou erro
        self.texto_cadastro     = customtkinter.CTkLabel(self.frame_central, text="")
        self.botao_cadastrar    = customtkinter.CTkButton(self.frame_central, fg_color="#034d32", text="Cadastrar", command= self.realizar_cadastro, width=250)
        
        # Logo UNIFESO
        self.logo_image         = CTkImage(Image.open("UNIFESO.png"), size=(250, 150))
        self.logo_label         = customtkinter.CTkLabel(self.frame_central, image=self.logo_image, text="")
        

        # Adicionando elementos na tela 
        self.logo_label .pack(pady=10)
        self.label.pack(pady=20)
        self.nome_usuario.pack(pady=10)
        self.email_usuario.pack(pady=10)
        self.celular_cadastro.pack(pady=10)
        self.senha_usuario.pack(pady=10)
        self.senha_confirma.pack(pady=10)
        self.botao_voltar.pack(pady=10)
        self.botao_cadastrar.pack(pady=10)
        self.botao_voltar.pack(pady=10)
        self.texto_cadastro.pack(pady=20)

    

    def realizar_cadastro(self):
    
        # Pegando os valores dos campos de entrada
        nome_input         = self.nome_usuario.get().upper().strip()
        email_input        = self.email_usuario.get().strip()
        celular_input      = self.celular_cadastro.get().strip()
        senha_input1       = self.senha_usuario.get().strip()
        senha_input2       = self.senha_confirma.get().strip()

    
        
        # Verificando se todos os campos estão preenchidos
        if nome_input and email_input and celular_input and senha_input1 and senha_input2:
            
            # Verificando se as senhas são iguais
            if senha_input1 == senha_input2:

                # Aqui você pode implementar a lógica para salvar o usuário no banco de dados
                # Tentando inserir no banco de dados
#                try:
#                    connection = conn()
#                    if connection:
#                        cursor = connection.cursor()
#                        query = """
#                        INSERT INTO usuarios (nome, email, celular, senha) 
#                        VALUES (%s, %s, %s, %s)
#                        """
#                        values = (nome_input, email_input, celular_input, senha_input1)
#                        cursor.execute(query, values)
#                        connection.commit()
#
                        self.texto_cadastro.configure(text=f"Cadastro {nome_input} realizado com sucesso!", text_color="green", font=("Arial", 12))
                        self.master.after(2000, self.limpa_tela)  # Atualiza a tela após 2 segundos
                        self.master.after(3000, self.voltar_para_login)  # Volta para o login após 3 segundos
 #                   else:
 #                       self.texto_cadastro.configure(text="Erro de conexão com o banco de dados", text_color="red")
#
 #               except Exception as e:
 #                   self.texto_cadastro.configure(text=f"Erro ao cadastrar: {e}", text_color="red")
#
 #               finally:
 #                   if connection and connection.is_connected():
 #                       cursor.close()
 #                       connection.close()

            else:
                self.texto_cadastro.configure(text="As senhas não coincidem", text_color="red")
        else:
            self.texto_cadastro.configure(text="Preencha todos os campos", text_color="red")


    def limpa_tela(self):
        # Limpando os campos após o cadastro
        self.nome_usuario.delete(0, 'end')
        self.email_usuario.delete(0, 'end')
        self.celular_cadastro.delete(0, 'end')
        self.senha_usuario.delete(0, 'end')
        self.senha_confirma.delete(0, 'end')
        self.texto_cadastro.configure(text="")

    def voltar_para_login(self):
       self.callback_voltar_login()  # Usa o callback para voltar à tela de login

    def mostrar(self):
        self.frame_central.pack(expand=True, fill="both")

    def ocultar(self):
        self.frame_central.pack_forget()
