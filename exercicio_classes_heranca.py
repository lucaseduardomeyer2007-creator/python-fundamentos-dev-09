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

    
    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"""
        Salário: {self.salario}
        """)


class Aluno(Pessoa):


    def __init__(self, nome: str, telefone: str, email: str, nota1: float, nota2: float, nota3: float):
        super().__init__(nome, telefone, email)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def apresentar_dados():
        super().apresentar_dados()
        print(f"""Nota 1: {self.nota1}
        Nota2: {self.nota2}
        Nota3: {self.nota3}
        """)

    def apresentar_media(self):
        media : float = (self.nota1 + self.nota2 + self.nota3) / 3
        
        print(f"Média: {media}")


def exemplo_heranca_pessoa():
    aluno1 = Aluno("Aluno 1", "000000000", "email@gmail.com", 9, 8, 4.5)

    professor1 = Professor("Professor 1", "00000000000", "email@gmail.com", 1500) 

    aluno1.apresentar_dados()
    aluno1.apresentar_media()

    professor1.apresentar_dados()
    


    