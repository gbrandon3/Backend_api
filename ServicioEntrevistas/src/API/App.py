import os

from flask import (
    Flask,
    Response,
    g,
    jsonify,
    request
)

from Aplicacion.Exception import MyException

from Infraestructura.Database import (
    close_db_connection,
    init_db_engine,
    db_connect
)

from Aplicacion.Servicios.EntrevistaServicio import EntrevistaServicio

from Infraestructura.Repositorios import EntrevistaRepositorio
from API.BadRequestException import BadRequestException

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

app.config['PROPAGATE_EXCEPTIONS'] = True

def get_db_connection(app):
    if 'db_con' not in g:
        db_engine = app.config.get('DB_ENGINE', None) or init_db_engine()
        g.db_con = db_connect(db_engine)
    return g.db_con

@app.errorhandler(BadRequestException)
@app.errorhandler(MyException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response

@app.teardown_appcontext
def teardown_db(exception=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        close_db_connection(db_con)

@app.route('/entrevistas/healthcheck', methods=['GET'])
def HealthCheck():
    resp = Response()
    resp.status_code = 200
    return jsonify({'status': 'alive!'})

@app.route('/entrevistas', methods=['GET'])
def consultar_entrevistas():
    print('Hola')
    return EntrevistaServicio.obtenerEntrevista(repositorio=EntrevistaRepositorio(get_db_connection(app))).__dict__

@app.route('/entrevistas', methods=['POST'])
def crear_entrevista():
    return EntrevistaServicio.agregarEntrevista(request.get_json(), repositorio=EntrevistaRepositorio(get_db_connection(app))).__dict__

@app.route('/entrevistas', methods=['PUT'])
def modificar_entrevista():
    return EntrevistaServicio.modificarEntrevista(request.get_json(), repositorio=EntrevistaRepositorio(get_db_connection(app))).__dict__
