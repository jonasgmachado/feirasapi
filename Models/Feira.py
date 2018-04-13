
class Feira:

    def __init__(self):
        self.id = -1
        self.long = ''
        self.lat = ''
        self.setcens = ''
        self.areap = ''
        self.coddist = ''
        self.distrito = ''
        self.codsubpref = ''
        self.subpref = ''
        self.regiao5 = ''
        self.regiao8 = ''
        self.nome_feira = ''
        self.registro = ''
        self.logradouro = ''
        self.numero = ''
        self.bairro = ''
        self.referencia = ''

    def setFeira(self, long, lat, setcens, areap, coddist, distrito, codsubpref, subpref, regiao5, regiao8, nome_feira, registro, logradouro, numero, bairro, referencia):
        self.long = long
        self.lat = lat
        self.setcens = setcens
        self.areap = areap
        self.coddist = coddist
        self.distrito = distrito
        self.codsubpref = codsubpref
        self.subpref = subpref
        self.regiao5 = regiao5
        self.regiao8 = regiao8
        self.nome_feira = nome_feira
        self.registro = registro
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.referencia = referencia

    def jsonToFeira(self, jsonstr):
        # self.long = jsonstr.json['LONG']
        # self.lat = jsonstr.json['LAT']
        # self.setcens = jsonstr.json['SETCENS']
        # self.areap = jsonstr.json['AREAP']
        # self.coddist = jsonstr.json['CODDIST']
        # self.distrito = jsonstr.json['DISTRITO']
        # self.codsubpref = jsonstr.json['CODSUBPREF']
        # self.subpref = jsonstr.json['SUBPREF']
        # self.regiao5 = jsonstr.json['REGIAO5']
        # self.regiao8 = jsonstr.json['REGIAO8']
        # self.nome_feira = jsonstr.json['NOME_FEIRA']
        # self.registro = jsonstr.json['REGISTRO']
        # self.logradouro = jsonstr.json['LOGRADOURO']
        # self.numero = jsonstr.json['NUMERO']
        # self.bairro = jsonstr.json['BAIRRO']
        # self.referencia = jsonstr.json['REFERENCIA']
        self.long = jsonstr['LONG']
        self.lat = jsonstr['LAT']
        self.setcens = jsonstr['SETCENS']
        self.areap = jsonstr['AREAP']
        self.coddist = jsonstr['CODDIST']
        self.distrito = jsonstr['DISTRITO']
        self.codsubpref = jsonstr['CODSUBPREF']
        self.subpref = jsonstr['SUBPREF']
        self.regiao5 = jsonstr['REGIAO5']
        self.regiao8 = jsonstr['REGIAO8']
        self.nome_feira = jsonstr['NOME_FEIRA']
        self.registro = jsonstr['REGISTRO']
        self.logradouro = jsonstr['LOGRADOURO']
        self.numero = jsonstr['NUMERO']
        self.bairro = jsonstr['BAIRRO']
        self.referencia = jsonstr['REFERENCIA']

