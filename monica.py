import requests
import pandas as pd
from pandas import read_excel

class Entrega():
    def setItemEntrega(self, itemEntrega):
        self.itemEntrega = itemEntrega

    def setProduto(self, produto):
        self.produto = produto

    def setCep(self, cep):
        self.cep = cep

    def setComplemento(self, complemento):
        self.complemento = complemento

def excel_file():
    pd.set_option("display.max_rows", 1000)
    pd.set_option("display.max_columns", 10)

    data = pd.read_excel("automacao.xlsx", "Planilha1")

    for name, sheet in data.items():
        produto = Entrega()
        produto.setEntrega("aoi")
        produto.entrega

        print(sheet)

excel_file()

def send_response():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfZ0-8mzregRLTmn6xo7q05Camz95F4fkWomU5q8OBSnHWg0g/formResponse"
    url_test = "https://docs.google.com/forms/d/e/1FAIpQLSfc5gkEAHvXB9zSZYHUewj466yhpE2_hf7r1JzJYu088VgIzA/formResponse"
    url_monica = "https://docs.google.com/forms/d/e/1FAIpQLSeGkKoum1HEonSxWeZP8r2PDHBncBVxRn61O4x4SwgTILDWtQ/formResponse"

    data = {
        "entry.11703947": "Monica Maria Wanderley Padilha",
        "entry.283002341": "this",
        "entry.96278573": "obviously",
        "entry.1587431302": "works",
        "entry.1495180370": "8888",
        "entry.1360790904": "Yes",
    }

    print(data)
    result = requests.post(url_test, data)

    print(result)
