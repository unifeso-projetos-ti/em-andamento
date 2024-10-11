import os
from PIL import Image, ImageTk

# Função para maximizar a janela no tamanho completo da tela
def maximizar_janela(janela):
    janela.geometry("{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight()))

# Função para converter um arquivo PNG em PhotoImage, ajustando o tamanho
def png_para_photo(caminho_png, tamanho=(20, 20)):
    if not os.path.isfile(caminho_png):
        raise FileNotFoundError(f"Arquivo PNG não encontrado: {caminho_png}")
    
    imagem = Image.open(caminho_png).resize(tamanho)
    return ImageTk.PhotoImage(imagem)

# Função para alternar a visibilidade da senha, sem depender de variável global
def alternar_visibilidade(senha_entry, botao_espia, senha_visivel):
    # Caminho dos arquivos PNG
    eye_open_image_path = "eye-open.png"
    eye_closed_image_path = "eye-closed.png"
    
    # Converter PNG e criar objetos PhotoImage
    eye_open_icon = png_para_photo(eye_open_image_path)
    eye_closed_icon = png_para_photo(eye_closed_image_path)
    
    if senha_visivel:
        senha_entry.configure(show="*")  # Oculta a senha
        botao_espia.configure(image=eye_closed_icon)  # Muda o ícone para 'fechado'
        return False  # Atualiza o estado para "senha oculta"
    else:
        senha_entry.configure(show="")  # Mostra a senha
        botao_espia.configure(image=eye_open_icon)  # Muda o ícone para 'aberto'
        return True  # Atualiza o estado para "senha visível"
