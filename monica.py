# https://docs.google.com/forms/d/e/1FAIpQLSeGkKoum1HEonSxWeZP8r2PDHBncBVxRn61O4x4SwgTILDWtQ/viewform

import requests
import xlrd
import pandas as pd

def excel_file():
    file = 'automacao.xlsx'
    xl = pd.ExcelFile(file)
    print(xl.sheet_names)
    df1 = xl.parse('Planilha1')

def call_page():
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfZ0-8mzregRLTmn6xo7q05Camz95F4fkWomU5q8OBSnHWg0g/formResponse"

    data = {
        "entry.2005620554": "Hii",
        "entry.1045781291": "this",
        "entry.1065046570": "obviously",
        "entry.1166974658": "works",
        "entry.839337160": "like charm",
        "entry.1360790904": "Yes",
    }

    print(data)
    result = requests.post(url, data)

    print(result)


excel_file()