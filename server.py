
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from Models.Feira import Feira
from Models.FeiraDAO import FeiraDAO

db = create_engine('sqlite:///feirassp.db')
app = Flask(__name__)
api = Api(app)
feiradb = FeiraDAO()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/home/')
def static_page():
    return render_template('index.html')

class Feiras(Resource):

    def post(self):
        conn = db.connect()
        feira = Feira()
        feira.jsonToFeira(request.json)
        return feiradb.insert_feira(feira)


class ListaFeiras(Resource):
    def get(self):
        return feiradb.get_feiras()



class BuscaFeira(Resource):
    def get(self, nome):
        return feiradb.busca_feiras(nome)


class DeletaFeira(Resource):
    def post(self, idFeira):
        return feiradb.deleta_feira(idFeira)


class AtualizarFeira(Resource):
    def post(self, idFeira):
        conn = db.connect()
        feira = Feira()
        feira.jsonToFeira(request.json)
        feiradb.update_feira(feira, idFeira)


api.add_resource(Feiras, '/feiras')
api.add_resource(ListaFeiras, '/listafeiras')
api.add_resource(BuscaFeira, '/buscafeira/<nome>')
api.add_resource(DeletaFeira, '/deletafeira/<idFeira>')
api.add_resource(AtualizarFeira, '/atualizafeira/<idFeira>')

if __name__ == '__main__':
    app.run()
