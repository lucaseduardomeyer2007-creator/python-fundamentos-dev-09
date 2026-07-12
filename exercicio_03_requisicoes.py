import requests

url_base = "https://api.franciscosensaulas.com"



def consultar_empresas():
    url = f"{url_base}/api/v1/empresa"

    resposta = requests.get(url)
    
    print("Status Code", resposta.status_code)
    print("Response:", resposta.text)


def consultar_empresa_por_id(): 
    id = 5

    url = f"{url_base}/api/v1/empresa/{id}"

    resposta = requests.get(url)
    
    print("Status Code", resposta.status_code)
    print("Response:", resposta.text)


def consultar_produtos():
    url = f"{url_base}/api/v1/empresa/produtos"

    resposta = requests.get(url)
    
    print("Status Code", resposta.status_code)
    print("Response:", resposta.text)


def consultar_produto_por_id():
    id = 5

    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    resposta = requests.get(url)
    
    print("Status Code", resposta.status_code)
    print("Response:", resposta.text)

def cadastrar_empresa():
    url = f"{url_base}/api/v1/empresa"

    empresa = {
        "nome": "Bella Janela",
        "cnpj": "88.065.668/0001-68"
    }
    
    resposta = requests.post(url, json=empresa) #Perguntar para o professor
    print("Status Code: ", resposta.status_code)


def cadastrar_produto():
    url = f"{url_base}/api/v1/empresa/produtos"

    produto = {
        "nome": "PS5",
        "preço": "3800",
        "categoria": "informática"
    }
    
    resposta = requests.post(url, json=produto) 
    print("Status Code: ", resposta.status_code)
    print("Texto : ", resposta.text)


def editar_empresa(): 
    url = f"{url_base}/api/v1/empresa/{id}"