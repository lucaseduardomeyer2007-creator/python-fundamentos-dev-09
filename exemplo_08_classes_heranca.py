class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    


class Funcionario:
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    

def exemplo_funcionario():
    pessoa = pessoa("Ronaldo", "Femomemo")
    print("Nome Completo:", pessoa.gerar_nome_completo())


