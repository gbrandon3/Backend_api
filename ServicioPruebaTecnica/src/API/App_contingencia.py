from flask import (
    Flask,
    Response,
    g,
    jsonify,
    request
)

from Aplicacion.MyException import MyExcepcion

from Infraestructura.Database import (
    close_db_connection,
    init_db_engine,
    db_connect
)

from Aplicacion.Servicios.PreguntaTecnicaServicio import PreguntaTecnicaServicio

from Infraestructura.repositorios.PreguntaRepositorio import PreguntaRepositorio
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
@app.errorhandler(MyExcepcion)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response

@app.teardown_appcontext
def teardown_db(exception=None):
    db_con = g.pop('db_con', None)
    if db_con is not None:
        close_db_connection(db_con)

@app.route('/pruebatecnica-contingencia/healthcheck', methods=['GET'])
def HealthCheck():
    resp = Response()
    resp.status_code = 200
    return jsonify({'status': 'alive!'})

@app.route('/pruebatecnica-contingencia/preguntas', methods=['GET'])
def consultar_preguntas():
    return PreguntaTecnicaServicio.obtenerPregunta(repositorio=PreguntaRepositorio(get_db_connection(app))).__dict__

@app.route('/pruebatecnica-contingencia/preguntas', methods=['POST'])
def crear_preguntas():
    return PreguntaTecnicaServicio.crearPregunta(request.get_json(), repositorio=PreguntaRepositorio(get_db_connection(app))).__dict__

@app.route('/pruebatecnica-contingencia/preguntas', methods=['PUT'])
def modificar_preguntas():
    return PreguntaTecnicaServicio.modificarPregunta(request.get_json(), repositorio=PreguntaRepositorio(get_db_connection(app))).__dict__

