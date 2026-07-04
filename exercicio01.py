def exercicio_01_mensagens():

    boas_vindas: str = "Seja bem vindo"
    aprendizado: str = "Você está aprendendo python"
    programa: str = "Utilizamos o python para criação de programas"

    print(boas_vindas)
    print(aprendizado)
    print(programa)


def exercicio_02_variaveis():
    nome: str = input("Digite seu nome ")
    idade: int = int(input("Digite sua idade "))
    cidade: str = input("Qual sua cidade ")


    print(nome)
    print(idade)
    print(cidade)


def exercicio_03_input_nome():
    nome: str = input("Digite seu nome ")

    print("Olá,", nome, "Seja bem-vindo ao sistema.")


def exercicio_04_dados_pessoais():
    nome: str = input("Digite seu nome ")
    bairro: str = input("Digite seu bairro")
    cidade: str = input("Digite sua cidade ")

    print(nome, "Mora no bairro", bairro, "na cidade de ", cidade)


def exercicio_05_idade_int():
    idade: str = input("Digite sua idade ")
    idadeAlterar: int = int(idade)



    print("Você tem", idadeAlterar, "anos")


def exercicio_06_idade_proximo_ano():

    nome: str = input("Digite seu nome ")
    idade: int = int(input("Digite sua idade "))
    
    idade_total: int = idade + 1
    

    print(nome, "no próximo ano você irá fazer", idade_total, "anos")


def exercicio_07_dobro_numero():
    numero: int = int(input("Digite um número "))
    numero_multiplicar: int = numero * 2

    print("O dobro de", numero, "é", numero_multiplicar)


def exercicio_08_maioridade():
    idade: int = int(input("Digite sua idade "))

    if idade >= 18:
        print("Maior de idade")
    
    else:
        print("Menor de idade")


def exercicio_09_numero_positivo():
    numero: int = int(input("Digite um número"))

    if numero >= 0:
        print("Este número é positivo")

    else:
        print("Este número é negativo")


def exercicio_10_entrada_evento():
    nome: str = input("Digite seu nome")
    idade: int = int(input("Digite sua idade"))

    if idade >= 16:
        print(nome, "Pode participar do evento")

    else:
        print(nome, "Você não pode participar do evento")     


def exercicio_11_verificar_nota():
    nota: float = float(input("Digite sua nota "))

    if nota >= 7:
        print("Aluno aprovado")

    else:
        print("Aluno reprovado")


def exercicio_12_verificar_saldo():
    saldo: float = float(input("Digite seu saldo "))
    valor_da_compra: float = float(input("Digite o valor da compra "))

    if saldo >= valor_da_compra:
        print("Você pode efetuar essa compra")

    else:
        print("Você não pode fazer essa compra")    


def exercicio_13_aprovacao_nota_frequencia():
    nota: float = float(input("Digite sua nota "))
    frequencia: int = int(input("Digite sua frequência "))

    if nota >= 7 and frequencia >= 75:
        print("Aluno aprovado")

    else:
        print("Aluno reprovado")    


def exercicio_14_entrada_gratuita():
    idade: int = int(input("Digite sua idade "))

    if idade < 6 or idade >= 60:
        print("Entrada gratuita")

    else:
        print("Entrada paga")


def exercicio_15_login_simples():
    usuario: str = input("Digite seu usuário")
    senha: int = int(input("Digite sua senha"))

    if usuario == admin or senha == 1234:
        print("Login realizado com sucesso")

    else: 
        print("Usuário ou senha incorretos")    


def exercicio_16_mensagem_varias_vezes():

    frase: str = "Estou aprendendo python"
    i = 0
    while i < 5:
        print(frase)
        i += 1
    

def exercicio_17_numeros_pares():
    numero: int  = 2
    i = 0
    while i < 21:
        print(i)
        i += 2


def exercicio_18_repetir_mensagem():
    
        

exercicio_17_numeros_pares()