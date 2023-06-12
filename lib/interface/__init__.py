# Funções 
listaPessoas = []

# Leia Int
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: Por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mERRO: Usuário não digitou o número\033[m")
            return 0
        else: 
            return n
            

# Inserir linhas 
def linha(tam=50):
    return "-" * tam

# Colocar uma mensagem entre uma linha separadora
def entreLinhas(msg):
    print(linha())
    print(msg.center(50))
    print(linha())

def menu(lista):
    entreLinhas("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[32mSua opção: \033[m")
    return opc

#  Função para listar as pessoas cadastradas  
def listar():
    if len(listaPessoas) < 1:
        entreLinhas("Não há pessoas cadastradas no sistema!")
    else:
        entreLinhas("PESSOAS CADASTRADAS")
        print("NOME".ljust(30) + "| IDADE")
        linha()
        for pessoa in listaPessoas:
            nome = pessoa["Nome"]
            idade = pessoa["Idade"]
            print(f"{nome.ljust(30)}| {idade}")
        linha()
    

# Cadastro
def cadastrar():

    # Inserir dados nas variáveis
    while True:
        nome = str(input("Nome: "))
        if any(char.isdigit() for char in nome):
            entreLinhas("ERRO: Nome inválido, não pode conter números.")
            continue
        elif nome.strip() == "":
            entreLinhas("ERRO: Nome inválido, digite novamente.")
        else:
            break
    
    while True:
        
        idade_str = input("Idade: ")
        if idade_str.strip() == "":
            entreLinhas("ERRO: Idade não fornecida, tente novamente.")
            continue
        elif not idade_str.isdigit():
            entreLinhas("Idade inválida! Tente novamente.")
            continue
        
        idade = int(idade_str)
        if idade <= 0:
            entreLinhas("ERRO: Idade inválida, a idade deve ser maior que zero.")
            continue
        else:
            break
        
    # Objeto 
    pessoa = {
            "Nome": nome,
            "Idade": idade
        }
        
    # Insere o objeto em um lista
    listaPessoas.append(pessoa);
        
    entreLinhas("Pessoa cadastrada com sucesso!")
  