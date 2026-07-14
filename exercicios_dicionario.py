from typing import Dict, List


def exercicio01():
    paciente: Dict [str |int] = {}
    paciente["nome_paciente"] = input("Digite o nome do paciente: ")
    paciente["idade"] = int(input("Digite a  idade do paciente: "))

    print("Nome do paciente: ", paciente["nome_paciente"], "\n", "Idade do paciente: ", paciente["idade"])


def exercicio02():
    aluno: Dict [str,str | int] = {}
    aluno["nome"] = input("Digite o nome do Aluno ")
    aluno["idade"] = int(input("Digite a idade do Aluno "))
    aluno["turma"] = input("Digite a turma do aluno ")
    aluno["curso"] = input("Digite o curso que está sendo feito ")


    for chave in aluno.keys():
        print(chave)
  


def exercicio03(): 
    produto: Dict [str, str | float | int] = {}
    produto["nome"] = input("Digite o nome do produto ")
    produto["preco"] = float(input("Digite o preço do produto "))
    produto["estoque"] = int(input("Estoque do produto "))
    produto["categoria"] = input("Qual a categoria desse produto ")


    for value in produto.values():
        print(value)


def exercicio04():
    funcionario: Dict [str, str| float |int] = {}

    funcionario["nome"] = input("Digite o nome do funcionário ")
    funcionario["cargo"] = input("Digite o cargo do funcionário ")
    funcionario["salario"] = float(input("Digite o salário do funcionário "))
    funcionario["setor"] = input("Digite o setor do funcionário")


    for item in funcionario.items():
        print(item)


def exercicio05():
    livro: Dict [str, str|int|float] = {} 

    livro["titulo"] = input("Digite o título do livro ")
    livro["autor"] = input("Digite o autor do livro ")
    livro["ano_publicacao"] = int(input("Digite o ano da publicação "))
    livro["quantidade_paginas"] = int(input("Digite a quantidade de páginas "))

    for item in livro.items():
        print(item)



def exercicio06():
    
    jogos = [
            {
            "nome_jogo": "Batman",
            "genero": "ação",
            "ano_lancamento": "2007",
            "preco": "100,00"
        },

        {
            "nome_jogo": "Gow ragnarok",
            "genero": "Aventura",
            "ano_lancamento": "2022",
            "preco": "349,90"
        }
    ]

    for jogo in jogos: #Percorrendo a lista que logo abaixo fazendo outro for, será possível percorrer o dicionário
        # para poder usar o .items que não é possível usar em uma lista 
        for chave, valor in jogo.items():
            print(f"{chave}: {valor}")



def exercicio07():
    produtos = [
    {
        "id": 1,
        "nome": "Homem-Aranha",
        "categoria": "brinquedo",
        "preco": 49.90,
        "estoque": 3
    },
    {
        "id": 2,
        "nome": "iphone",
        "categoria": "eletronico",
        "preco": 5000,
        "estoque": 2
    },
    {
        "id": 3,
        "nome": "TV LED 65 POL",
        "categoria": "Eletrodoméstico",
        "preco": 6000,
        "estoque": 2
    },
    {
        "id": 4,
        "nome": "Woody",
        "categoria": "brinquedo",
        "preco": 199.90,
        "estoque": 3
    },
    {
        "id": 5,
        "nome": "Notebook Acer nitro v15",
        "categoria": "eletronico",
        "preco": 6899.90,
        "estoque": 10
    }
]

    
    def obter_nomes_produtos():

        nomes = []  
        for produto in produtos:
                nomes.append(produto["nome"])
        print(nomes) 
    

    obter_nomes_produtos()


    def obter_produtos_com_estoque_baixo():

        produtos_estoque_baixo = []

        for produto in produtos:
            if produto["estoque"] < 10:
                produtos_estoque_baixo.append(produto["nome"])

        print(produtos_estoque_baixo)

    obter_produtos_com_estoque_baixo()


    def obter_produtos_por_categoria():
        produtos_filtrados = []
        



exercicio07()