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
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()
        
    
def cadastrarArq(arq, nome="desconhecido", idade=0):
    try:
         a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado.")
            