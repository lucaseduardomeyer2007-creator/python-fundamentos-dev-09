class Tenis:
    def __init__(self, modelo: str, tamanho: int, marca: str, valor: float):

        self.modelo = modelo
        self.tamanho = tamanho
        self.valor = valor


    def apresentar_dados(self):
        print(f"""Modelo: {self.modelo}
    Tamanho: {self.tamanho}
    """, )
        

    def modelos_tenis():
        nike = Tenis("Jordan", 40)
        adidas = Tenis("Adidas Campus", 39)
        puma = Tenis("Nitro 5", 42)


        nike.apresentar_dados()
        adidas.apresentar_dados()
        puma.apresentar_dados()