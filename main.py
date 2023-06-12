# Python Project

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

# Laço de repetição
while True:
    resposta = menu(["Cadastrar nova pessoa", "Ver pessoas cadastradas no sistema", "Ver pessoas cadastradas no arquivo", "Sair do sistema"])
    
    if resposta == 1:
        cadastrar()
        sleep(2)
    elif resposta == 2:
        listar()
        sleep(2)
        
    elif resposta == 3:
        lerArquivo(arq)
        sleep(2)
    elif resposta == 4:
        entreLinhas(f"Programa finalizado, volte sempre!")
        break
    else: 
        entreLinhas("\033[31mOpção inválida! Por favor, escolha uma opção válida.\033[m")
        sleep(2)
