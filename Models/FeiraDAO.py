from flask import jsonify

from Models.Feira import Feira
from sqlalchemy import create_engine


class FeiraDAO:

    def __init__(self):
        self.db = create_engine('sqlite:///feirassp.db')

    def insert_feira(self, feira):
        conn = self.db.connect()
        querystr = "insert into feiras values(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        query = conn.execute(querystr, (feira.long, feira.lat, feira.setcens,
                                     feira.areap, feira.coddist, feira.distrito,
                                     feira.codsubpref,
                                     feira.subpref, feira.regiao5, feira.regiao8,
                                     feira.nome_feira, feira.registro, feira.logradouro,
                                     feira.numero, feira.bairro, feira.referencia))
        return {'status': 'success'}

    def update_feira(self,feira,idFeira):
        conn = self.db.connect()
        querystr = "update feiras set LONG=?,LAT=?,SETCENS=?,AREAP=?, \
                                       CODDIST=?,DISTRITO=?,CODSUBPREF=?,SUBPREF=?, \
                                       REGIAO5=?,REGIAO8=?,NOME_FEIRA=?,REGISTRO=?, \
                                       LOGRADOURO=?, NUMERO=?,BAIRRO=?,REFERENCIA=? WHERE ID=? "
        query = conn.execute(querystr, (feira.long, feira.lat, feira.setcens,
                                        feira.areap, feira.coddist, feira.distrito,
                                        feira.codsubpref,
                                        feira.subpref, feira.regiao5, feira.regiao8,
                                        feira.nome_feira, feira.registro, feira.logradouro,
                                        feira.numero, feira.bairro, feira.referencia, idFeira))
        return {'status': 'success'}

    def get_feiras(self):
        conn = self.db.connect()
        query = conn.execute("select * from feiras;")
        result = {'rows': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def busca_feiras(self, nome):
        conn = self.db.connect()
        querystr = "select * from feiras where NOME_FEIRA like ? "
        query = conn.execute(querystr, '%'+nome+'%')
        result = {'rows': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

    def deleta_feira(self,idFeira):
        conn = self.db.connect()
        querystr = "delete from feiras where id=?"
        query = conn.execute(querystr, (idFeira,))
        return {'status': 'success'}