# GUI => Graphical User Interface
# UI => User interface

#Instalar a biblioteca rich(`pip install rich`)
# Instalar a biblioteca questionary: `pip install questionary`

from rich.console import Console
from rich.table import table
import requests
import questionary
import os

url_base = "https://api.franciscosensaulas.com"


def menu():
    opcoes_menu = [
        "Consultar  Categoria",
        "Cadastrar Categoria",
        "Editar Categoria"
        "Apagar Categoria",
        "Sair"

    ]