class Autor:
    def __init__( self, nome: str, nacionalidade: str, ano_nascimento : int):

        self.nome = nome
        self.nacionalidade = nacionalidade
        self.ano_nascimento = ano_nascimento
        self.descricao = self.obter_descricao()

    def apresentar_dados(self):
        print(f"""Nome  do Autor:{self.nome}
    Nacionalidade: {self.nacionalidade}
    Ano de nascimento: {self.ano_nascimento}
""")
        
    def obter_descricao(self):
        descricao = f"""{self.nome} - {self.nacionalidade}"""
        return descricao

def exemplo_autor():
    autor1 = Autor("J K Rowling", " Yate - Inglaterra", 1965)
    autor2 = Autor("C.S.Lewis", "Belfast - Irlanda do Norte", 1898)

    autor1.apresentar_dados()
    autor2.apresentar_dados()




class Livro:
    def __init__(self, titulo : str, quantidade_paginas : int, ano_publicacao : int, descricao : Autor):
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.ano_publicacao = ano_publicacao
        self.descricao = Autor.obter_descricao()

    def apresentar_dados(self):
        print(f""" Título: {self.titulo}
        Quantidade de páginas: {self.quantidade_paginas}
        Ano da publicação: {self.ano_publicacao}
        Descrição : {self.autor.obter_descricao()}   
""")
        
def exemplo_livro():
    autor1 = Livro("Harry Potter e a Pedra Filosofal", 208, 1997, "")  #PRECISO DE AJUDA PRA ENTENDER A PARTE DE PEGAR A DESCRIÇÃO
    autor2 = Livro("As Crônicas de Nárnia", 528, 1950, "")

    autor1.apresentar_dados()
    autor2.apresentar_dados()