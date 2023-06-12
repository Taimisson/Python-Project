# Sistema de Cadastro de Pessoas

Este é um sistema simples de cadastro de pessoas, onde você pode cadastrar pessoas no sistema ou em um arquivo de texto, e também visualizar as pessoas cadastradas. O sistema foi desenvolvido em Python.

## Funcionalidades

- Cadastrar pessoa no sistema
- Cadastrar pessoa no arquivo
- Ver pessoas cadastradas no sistema
- Ver pessoas cadastradas no arquivo
- Sair do sistema

## Pré-requisitos

- Python 3.x

## Instalação

1. Clone o repositório para o seu ambiente local:

git clone https://github.com/seu-usuario/sistema-cadastro-pessoas.git

2. Acesse o diretório do projeto:

cd sistema-cadastro-pessoas

3. Execute o arquivo `main.py`:

python main.py


## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

# Arquivo lib/interface.py

Este arquivo contém as funções de interface do sistema.

## Funções

### `leiaInt(msg)`

Esta função lê um número inteiro digitado pelo usuário.

### `linha(tam=50)`

Esta função retorna uma string com uma linha separadora, com tamanho definido.

### `entreLinhas(msg)`

Esta função imprime uma mensagem centralizada entre linhas separadoras.

### `menu(lista)`

Esta função exibe um menu com as opções fornecidas em uma lista e retorna a opção escolhida pelo usuário.

### `listar()`

Esta função exibe a lista de pessoas cadastradas no sistema.

### `cadastrar()`

Esta função solicita ao usuário o nome e a idade de uma pessoa e realiza o cadastro no sistema.

---

# Arquivo lib/arquivo.py

Este arquivo contém as funções relacionadas à manipulação de arquivos.

## Funções

### `arquivoExiste(nome)`

Esta função verifica se um arquivo existe.

### `criarArquivo(nome)`

Esta função cria um novo arquivo.

### `lerArquivo(nome)`

Esta função lê um arquivo e exibe o conteúdo na tela.

### `cadastrarArq(arq, nome="desconhecido", idade=0)`

Esta função adiciona um novo registro ao arquivo.

---

## Autor

Taimisson de Carvalho Schardosim - [taimissoncontact@gmail.com](mailto:taimissoncontact@gmail.com)

