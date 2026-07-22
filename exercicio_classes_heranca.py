class Pessoa:
    def __init__(self, nome: str, numero_telefone: int, email: str):
        self.nome = nome
        self.numero_telefone = numero_telefone
        self.email = email


    def apresentar_dados(self):
        print(f""" Nome: {self.nome}
    Número de telefone: {self.numero_telefone}
    Email: {self.email}
        
        """)


class Professor:
    def __init__(self, nome: str, numero_telefone: int, email: str, salario: float):
        super().__init__(nome, numero_telefone, email)
        self.salario = salario

