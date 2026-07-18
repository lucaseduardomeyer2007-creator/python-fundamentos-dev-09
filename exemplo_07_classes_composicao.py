class Motor:
    # Construtor
    def __init__(self, potencia: int, combustivel: str):
        self.potencia = potencia
        self.combustivel = combustivel

    
class Carro:
    def __init__(self, modelo: str, ano_lancamento: int, motor: Motor):
        self.modelo = modelo
        self.ano_lancamento = ano_lancamento
        self.motor = motor


def exemplo_carro():
    motor_golf_tsi = Motor(140, "flex")

    golf_tsi = Carro("Golf TSI", 2013, motor_golf_tsi)

    print(golf_tsi.modelo) # Modelo pertence ao carro
    print(golf_tsi.ano_lancamento) # Ano de Lançamento pertence ao carro
    print(golf_tsi.motor.potencia) # Potencia pertence ao motor
    print(golf_tsi.motor.combustivel)


class Bateria:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        # Definimos que o celular já tem carga em 100%
        self.carga = 100 # 100% de bateria

    def utilizar(self, consumo: int):
        self.carga = self.carga - consumo

    def apresentar_dados(self):
        print(f""" Bateria:
        Capacidade {self.capacidade}
        Carga: {self.carga}
""")
        

class Armazenamento: 
    def __init__(self, capacidade: int):
        self.capacidade = capacidade

    def apresentar_dados(self)
        print(f"Armazenamento: {self.capacidade} GB")


class Celular:
    def __init__(self, modelo: str, preco: float, cor :str, bateria: Bateria, armazenamento: Armazenamento):
        
    