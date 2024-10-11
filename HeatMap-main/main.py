import customtkinter
from tela_login import TelaLogin
from tela_cadastro import TelaCadastro
from tela_teste import TelaTeste
from utils import maximizar_janela


# Inicializar janela principal
janela = customtkinter.CTk()
maximizar_janela(janela)

# Criar instâncias das telas
tela_login      = TelaLogin(janela)
tela_cadastro   = TelaCadastro(janela, lambda: mostrar_tela(tela_login, tela_cadastro))#
tela_teste      = TelaTeste(janela)

# Passar a instância de tela_teste para tela_login
tela_login.set_tela_teste(tela_teste)

# Mostrar apenas a tela de login inicialmente
tela_login.mostrar()


# Função para alternar entre as telas
def mostrar_tela(tela_para_mostrar, tela_para_ocultar):
    tela_para_ocultar.ocultar()
    tela_para_mostrar.mostrar()

# Configurar o botão de cadastro para trocar de tela
tela_login.botao_cadastro.configure(command=lambda: mostrar_tela(tela_cadastro, tela_login))
tela_cadastro.botao_voltar.configure(command=lambda: mostrar_tela(tela_login, tela_cadastro))

# Configurando o botão de voltar na tela de teste para voltar para o login
tela_teste.botao_voltar.configure(command=lambda: mostrar_tela(tela_login, tela_teste))

# Início do loop principal
janela.mainloop()
