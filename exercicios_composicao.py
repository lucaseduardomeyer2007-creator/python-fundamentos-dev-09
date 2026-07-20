class Autor:
    def __init__( self, nome: str, nacionalidade: str, ano_nascimento : int):

        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento


    def apresentar_dados(self):
        print(f"""Nome  do Autor:{self.nome}
    Nacionalidade: {self.nacionalidade}
    Ano de nascimento: {self.ano_nascimento}
""")
        
    def obter_descricao(self):
        descricao = f"""{self.nome} - {self.nacionalidade}"""
        return descricao


class Livro:
    def __init__(self, titulo : str, quantidade_paginas : int, ano_publicacao : int, descricao : Autor):
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.ano_publicacao = ano_publicacao
        self.descricao = descricao
