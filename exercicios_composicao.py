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



class Livro:
    def __init__(self, titulo : str, quantidade_paginas : int, ano_publicacao : int, descricao : Autor):
        self.titulo = titulo
        self.quantidade_paginas = quantidade_paginas
        self.ano_publicacao = ano_publicacao
        self.descricao = descricao

    def apresentar_dados(self):
        print(f""" Título: {self.titulo}
        Quantidade de páginas: {self.quantidade_paginas}
        Ano da publicação: {self.ano_publicacao}
        Descrição : {self.descricao.obter_descricao()}   
""")


def exemplo_autor():
    autor1 = Autor("J K Rowling", " Yate - Inglaterra", 1965)
    autor2 = Autor("C.S.Lewis", "Belfast - Irlanda do Norte", 1898)

    autor1.apresentar_dados()
    autor2.apresentar_dados()

    livro1 = Livro("Harry Potter e a Pedra Filosofal", 208, 1997, autor1)  #PRECISO DE AJUDA PRA ENTENDER A PARTE DE PEGAR A DESCRIÇÃO
    livro2 = Livro("As Crônicas de Nárnia", 528, 1950, autor2)

    livro1.apresentar_dados()
    livro2.apresentar_dados()



class Endereco:
    def __init__(self, rua : str, numero: int, bairro: str, cidade: str, estado: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    def apresentar_dados(self):
        print(f""" Rua: {self.rua}
        Número: {self.numero}
        Bairro: {self.bairro}
        Cidade: {self.cidade}
        Estado: {self.estado}
        """)

    def obter_endereco_completo(self):
        endereco_completo = f"""{self.rua} -{self.numero} -{self.bairro} - {self.cidade} / {self.estado}"""
        
        return endereco_completo



class Pessoa:
    def __init__(self, nome: str, idade: int, telefone: int, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.endereco = endereco


    def apresentar_dados(self):
        print(f"""Nome : {self.nome}
        Idade: {self.idade}
        Telefone:{self.telefone}
        Endereço : {self.endereco.obter_endereco_completo()}
        """)


    def verificar_maioridade(self):

        if idade >= 18:
            print("Possui 18 anos ou mais")
        
        else: 
            print("Menor de 18 anos")


def exemplo_endereco():
    endereco1 = Endereco("Rua Alcides Lima", 47, "Caimbé", "Boa Vista", "RR")
    endereco2 = Endereco("Alameda João Duda Calado", 59,"Pinheiro", "Maceió", "AL")

    endereco1.apresentar_dados()
    endereco2.apresentar_dados()


    pessoa1 = Pessoa("Batman", 23, 6833616224, endereco1)
    pessoa2 = Pessoa("Robin", 15, 9337505542, endereco2)

    


class Cliente:
    def __init__(self,  nome: str, cpf: int, email: str):
        self.nome = nome
        self.cpf = cpf
        self.email = email
    

    def apresentar_dados(self):
        print(f""" Nome: {self.nome}
        CPF: {self.cpf}
        Email: {self.email} 
        """)

    def obter_identificacao(self):
        identificacao = f"""{self.nome} - {self.cpf}"""
        return identificacao


class Pedido:
    def __init__(self, numero: int, produto: str, quantidade: int, valor_unitario: float, cliente: Cliente):
        self.numero = numero
        self.produto = produto
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.cliente = cliente

    def apresentar_dados(self):
        print(f""" Número do Pedido: {self.numero}
        Produto: {self.produto}
        Quantidade: {self.quantidade}
        Valor Unitário: {self.valor_unitario}
        Identificação do Cliente: {self.cliente.obter_identificacao()}
        """)

    def calcular_total(self):
        total = self.quantidade * self.valor_unitario
        return total


    def apresentar_total(self):
        valor_total = self.calcular_total()
        print("O valor total do pedido é ", valor_total)


def exemplo_cliente():
    cliente1 = Cliente("Batman", 11264657714, "agenorfernandes@gmail.com")
    cliente2 = Cliente("Robin", 16941425156, "telmoborges@gmail.com")

    cliente1.apresentar_dados()
    cliente2.apresentar_dados()

    pedido1 = Pedido(67, "batmovel", 3, 1000, cliente1)
    pedido2 = Pedido(45, "taser", 5, 250, cliente2)

    pedido1.apresentar_dados()
    pedido2.apresentar_dados()
    pedido1.apresentar_total()
    pedido2.apresentar_total()

    
exemplo_cliente()



class Professor:
    def __init__(self, nome : str, especialidade: str, tempo_experiencia: int):
        self.nome = nome
        self.especialidade = especialidade
        self.tempo_experiencia = tempo_experiencia


    def apresentar_dados(self):
        print(f"""Nome do professor: {self.nome}
        Especialidade: {self.especialidade}
        Tempo de experiência: {self.tempo_experiencia}
        """)

    def obter_apresentacao(self):
        apresentacao = f"""{self.nome} - {self.especialidade}"""
        return apresentacao


class Curso:
    def __init__(self, nome: str, carga_horaria: int, quantidade_alunos: int, apresentacao: Professor):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.quantidade_alunos = quantidade_alunos
        self.apresentacao = apresentacao

    def apresentar_dados(self):
        print(f""" Nome do Curso: {self.nome}
        Carga Horária: {self.carga_horaria}
        Quantidade de alunos: {self.quantidade_alunos}
        Apresentação: {self.apresentacao.obter_apresentacao()}        
        """)

    def verificar_duracao(self):

        if self.carga_horaria >= 40:
            print("Curso de longa duração")
        
        else:
            print("Curso de curta duração")


def exemplo_curso():
    professor1 = Professor("Francisco", "Especialista em Python", 8)
    professor2 = Professor("Lukita", "Especialista em Java", 4)

    professor1.apresentar_dados()
    professor2.apresentar_dados()

    curso1= Curso("Python", 50, 20, professor1)
    curso2= Curso("Java", 30, 10, professor2)

    curso1.apresentar_dados()
    curso1.verificar_duracao()
    curso2.apresentar_dados()
    curso2.verificar_duracao()


exemplo_curso()