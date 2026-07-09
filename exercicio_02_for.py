def exercicio_01 ():
    for i in range(0, 5):
        print("Bem vindo", i)




def exercicio_02():
    for i in range(15, 31):
        print(i)


def exercicio_03():
    
    # O f antes das aspas (f"...") transforma a string em uma f-string (Literais de string formatados). 
    # Ela permite inserir o valor de variáveis e até expressões diretamente dentro do texto usando {}.
    numero : int = int(input("Digite um número "))

    for i in range(1, 11):
        print(f"{numero} * {i} = {numero * i} ")


def exercicio_04():
    soma = 0    
    
    for i in range(0, 5):
        numero: int = int(input("Digite 5 números "))
        soma = soma + numero
        
    print(soma)


def exercicio_05():
    nomes = []

    nomes.append("Batman")
    nomes.append("Robin")
   
    nomes.append("Erick")
    nomes.append("Elias")

    print(f"{nomes[0]}, {nomes[1]}, {nomes[2]}, {nomes[3]}")


def exercicio_06():
    frutas = []
    frutas1: str = input("Digite a primeira fruta ")
    frutas2: str = input("Digite a segunda fruta ")
    frutas3: str = input("Digite a terceira fruta ")

    frutas.append(frutas1)
    frutas.append(frutas2)
    frutas.append(frutas3)

    print(f"{frutas[0]}, {frutas[1]}, {frutas[2]}")


def exercicio_07():
    numeros = []
    numero1: int = int(input("Digite o primeiro número "))
    numero2: int = int(input("Digite o segundo número "))
    numero3: int = int(input("Digite o terceiro número "))
    numero4: int = int(input("Digite o quarto número "))

    numeros.append(numero1)
    numeros.append(numero2)
    numeros.append(numero3)
    numeros.append(numero4)


    print(f"{numeros[0]}, {numeros[1]}, {numeros[2]}, {numeros[3]}")


def exercicio_08():
    notas = []
    nota1: float = float(input("Digite a primeira nota "))
    nota2: float = float(input("Digite a segunda nota "))
    nota3: float = float(input("Digite a terceira nota "))
    nota4: float = float(input("Digite a quarta nota "))

    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    notas.append(nota4)


    print(notas)
    print(f" primeira nota: {notas[0]}")
    print(f" Última nota: {notas[3]}")

    notas[1] = int(input("Digite uma nova nota pra segunda nota "))
    notas.remove(notas[2])
    print(notas)
    soma = notas[0] + notas[1] + notas[2]
    print(f"{soma / 3}")


exercicio_08()