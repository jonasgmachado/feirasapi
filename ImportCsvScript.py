from tkinter import filedialog
from Models.Feira import Feira
from Models.FeiraDAO import FeiraDAO
import csv
import json


file_path = filedialog.askopenfilename()
with open(file_path) as arquivo_csv:
        fieldnames = ('ID', 'LONG', 'LAT', 'SETCENS', 'AREAP', 'CODDIST', 'DISTRITO', 'CODSUBPREF', 'SUBPREF', 'REGIAO5', 'REGIAO8','NOME_FEIRA', 'REGISTRO', 'LOGRADOURO', 'NUMERO', 'BAIRRO', 'REFERENCIA')
        arquivo_csv.readline()
        reader = csv.DictReader(arquivo_csv, fieldnames)
        out = json.dumps([row for row in reader])
        data = json.loads(out)
        feira = Feira()
        feiradb = FeiraDAO()
        for element in data:
                feira.jsonToFeira(element)
                feiradb.insert_feira(feira)
                print('Feira inserida: '+feira.nome_feira)


