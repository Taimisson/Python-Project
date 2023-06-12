from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, "wt+") # Write text create
        a.close()
    except:
        print("Houve um ERRO na criação do Arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        entreLinhas("PESSOAS CADASTRADAS NO ARQUIVO")
        print(a.read())