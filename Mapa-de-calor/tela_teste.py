import customtkinter
from customtkinter import CTkImage
from PIL import Image
import webbrowser

class TelaTeste:
    def __init__(self, master):
        self.master = master
        
        # Definindo o frame_central
        self.frame_central      = customtkinter.CTkFrame(self.master, fg_color="#000000") # Cor de fundo da janela 
        
        # Definindo o botão "Voltar"
        self.botao_voltar = customtkinter.CTkButton(self.frame_central, fg_color="#034d32", text="Voltar", width=250)
        
        # Logo UNIFESO
        self.logo_image         = CTkImage(Image.open("UNIFESO.png"), size=(250, 150))
        self.logo_label         = customtkinter.CTkLabel(self.frame_central, image=self.logo_image, text="")

       # Adicionando elementos na tela 
        self.logo_label .pack(pady=10)
        self.botao_voltar.pack(pady=20)

    def abrir_link(self):
        # Função que abre o link do Power BI
        url = "https://app.powerbi.com/reportEmbed?reportId=7456a55c-7721-45ae-8acc-ae2194e7562a&autoAuth=true&ctid=fc466b9b-be22-4a53-a1f9-098894485f86"
        webbrowser.open(url)

    def mostrar(self):
        self.frame_central.pack(expand=True, fill="both")
        self.abrir_link()  # O link será aberto quando a tela for mostrada

    def ocultar(self):
        self.frame_central.pack_forget()