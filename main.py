# Python Project

from lib.interface import *
from time import sleep

# Variáveis
listaPessoas = []

# Laço de repetição
while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    
    if resposta == 1:
        listar()
        sleep(2)
    elif resposta == 2:
        cadastrar()
    elif resposta == 3:
        entreLinhas(f"Programa finalizado, volte sempre!")
        break
    else: 
        entreLinhas("\033[31mOpção inválida! Por favor, escolha uma opção válida.\033[m")
        sleep(2)
