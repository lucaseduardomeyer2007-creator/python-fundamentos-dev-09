class Tenis:
    def __init__(self, modelo: str, tamanho: int, marca: str, valor: float):

        self.modelo = modelo
        self.tamanho = tamanho
        self.marca = marca
        self.valor = valor
        


    def apresentar_dados(self):
        print(f"""Modelo: {self.modelo}
    Tamanho: {self.tamanho} Marca: {self.marca} Valor {self.valor}
    """, )
        

def exemplox_tenis():
    nike = Tenis("Jordan", 40, "Nike", 1200)
    adidas = Tenis("Adidas Campus", 39, "Adidas", 200)
    puma = Tenis("Nitro 5", 42, "Puma", 1100)

    nike.apresentar_dados()
    adidas.apresentar_dados()
    puma.apresentar_dados()


class Aluno:
    def __init__(self, nome: str, nota_1: float, nota_2: float):
    
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2    
        self.media = self.calcular_media()
        self.situacao = self.apresentar_situacao()

    def apresentar_dados(self):
        print(f""" Nome: {self.nome} 
        Nota 1: {self.nota_1}
        Nota 2: {self.nota_2}
        {self.situacao}
""")

    def calcular_media(self):
        media = (self.nota_1 + self.nota_2) / 2
        return media
    
    def apresentar_situacao(self): 
        apresentar = ""


        if self.media >= 7:
              apresentar = "Aluno aprovado"
             
        else:
             apresentar = "Aluno reprovado"
  
        return apresentar

def exemplo_aluno():
    elias = Aluno("Elias", 4, 5)
    matheus = Aluno("Matheus", 10, 9.5)
    lucas = Aluno("Lucas", 8, 5)


    elias.apresentar_dados()
    matheus.apresentar_dados()
    lucas.apresentar_dados()


exemplo_aluno()



class Triangulo:
    def __init__(self, base: float, altura: float, lado_1 : float, lado_2: float, lado_3: float):
    
        self.base = base
        self.altura = altura
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
        self.area = self.calcular_area()
        self.triangulo = self.verificar_equilatero()

    def apresentar_dados(self):
        print(f""" Base: {self.base}
        Altura: {self.altura}
        Lado 1: {self.lado_1}
        Lado 2: {self.lado_2}
        Lado 3: {self.lado_3}
""")
    

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area


    def verificar_equilatero(self):
        triangulo = ""

        if self.lado_1 == self.lado_2 == self.lado_3:
            triangulo = "É um triângulo equilátero"
        else: 
            triangulo = "Não é um triângulo equilátero"

        return triangulo

def exemplox_triangulo():
    triangulo = Triangulo(3, 2,60, 3, 3, 3)
    triangulo2 = Triangulo(4, 4.58, 5, 5, 5)

    triangulo.apresentar_dados()
    triangulo2.apresentar_dados()
    
    triangulo.calcular_area()
    triangulo2.calcular_area()
    
    triangulo.verificar_equilatero()
    triangulo2.verificar_equilatero()



class Quadrado:
    def __init__(self, lado: float):
        self.lado = lado

    
    