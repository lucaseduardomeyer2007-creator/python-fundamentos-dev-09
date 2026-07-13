from typing import Dict


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


exercicio05()