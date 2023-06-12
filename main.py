# Python Project

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

# Laço de repetição
while True:
    resposta = menu(["Cadastrar pessoa no sistema", "Cadastrar pessoa no arquivo","Ver pessoas cadastradas no sistema", "Ver pessoas cadastradas no arquivo", "Sair do sistema"])
    
    if resposta == 1:
        entreLinhas("NOVO CADASTRO")
        cadastrar()
        sleep(2)
    elif resposta == 2:
        entreLinhas("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrarArq(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        listar()
        sleep(2)
    elif resposta == 4:
        lerArquivo(arq)
        sleep(2)
    elif resposta == 5:
        entreLinhas(f"Programa finalizado, volte sempre!")
        break
    else: 
        entreLinhas("\033[31mOpção inválida! Por favor, escolha uma opção válida.\033[m")
        sleep(2)
