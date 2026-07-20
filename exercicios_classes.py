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
        self.area = self.calcular_area()
        self.perimetro = self.calcular_perimetro()


    def apresentar_dados(self):
        print(f"Lado do quadrado", {self.lado})
    

    def calcular_area(self):
        area = self.lado * self.lado
        return area
    
    def calcular_perimetro(self):
        perimetro = self.lado * 4
        return perimetro
    

def exemplo_quadrado():
    quadrado1 = Quadrado(4)
    quadrado2 = Quadrado(2)

    quadrado1.apresentar_dados()
    quadrado2.apresentar_dados()

    quadrado1.calcular_area()
    quadrado2.calcular_area()

    quadrado1.calcular_perimetro() 
    quadrado2.calcular_perimetro()



class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def apresentar_dados(self):
        print(f"""Base do retangulo {self.base}
    Altura do retangulo {self.altura}
""")
    
    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = (self.base + self.altura) * 2
        return perimetro
    

def exemplo_retangulo():
    retangulo1 = Retangulo(4, 2.5)
    retangulo2 = Retangulo(7, 13.5)

    retangulo1.apresentar_dados()
    retangulo2.apresentar_dados()

    retangulo1.calcular_area()
    retangulo2.calcular_area()

    retangulo1.calcular_perimetro()
    retangulo2.calcular_perimetro()


class Circulo:
    def __init__(self, raio: float):
        self.raio = raio

    def apresentar_dados(self):
        print(f""" O raio é {self.raio}
""")
    
    def calcular_area(self):
        area = (self.raio * self.raio) * 3.14
        return area
    
    def calcular_circunferencia(self):
        circunferencia = 2 * 3.14 * self.raio
        return circunferencia
    

def exemplo_circulo():
    circulo1 = Circulo(5)
    circulo2 = Circulo(11)


    circulo1.apresentar_dados()
    circulo2.apresentar_dados()

    circulo1.calcular_area()
    circulo2.calcular_area()

    circulo1.calcular_circunferencia()
    circulo2.calcular_circunferencia()


class Personagem:
    def __init__(self, nome: str, vida: float, ataque : float):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque


    def apresentar_dados(self):
        print(f""" Nome do personagem é {self.nome}
    Ele tem {self.vida} de vida
    Seu ataque dá o dano de {self.ataque} por ataque
""")
        
    def atacar(self, outro_personagem: "Personagem"):
        outro_personagem.vida = outro_personagem.vida - self.ataque
        print(f"\n {self.nome} atacou {outro_personagem.nome}!")
        print(f" Vida atual de {outro_personagem.nome}: {outro_personagem.vida}")

def executar_jogo():
    
    personagem1 = Personagem("Guerreiro", 100, 20)
    personagem2 = Personagem("Mago", 80, 25)

    
    print("--- Dados Iniciais ---")
    personagem1.apresentar_dados()
    personagem2.apresentar_dados()

    
    personagem1.atacar(personagem2)

    
    personagem2.atacar(personagem1)

    
    print("\n--- Dados Finais ---")
    personagem1.apresentar_dados()
    personagem2.apresentar_dados()
