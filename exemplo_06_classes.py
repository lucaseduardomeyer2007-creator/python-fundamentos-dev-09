class Cachorro:
    # _init_ é o construtor da classe, que é executado
    # quando instanciamos um objet oda classe
    def _init_(self, apelido: str, raca: str, cor: str, peso: float, idade: int):
        self.apelido = apelido
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade

    
    def apresentar_dados(self):
        print(f"Cachorro: {self.apelido}")
        print(f"Raça: {self.raca}")
        print(f"Cor: {self.cor}", end="\n\n\n")

        
    def fazer_aniversario(self):
        self.idade = self.idade + 1
        print("FELIZ ANIVERSÁRIO!!!!!!!!!", self.apelido, "fez", self.idade, "anos")

    
tobi = Cachorro("Tobi", "Vira-Lata", "caramelo", 25.60, 6)
tobi.peso = 29.34
tobi.apresentar_dados()

Thor = Cachorro("Thor", "Pastor-Alemão", "capa preta", 38, 8)
Thor.fazer_aniversario()
Thor.apresentar_dados()

mogli = Cachorro("mogli", "Vira-Lata", "preto", 30, 6)
mogli.apresentar_dados()

