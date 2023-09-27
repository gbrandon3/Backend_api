import json
import os

from flask import (
    Flask,
    Response,
    jsonify,
    make_response,
    request
)
import requests
from Dominio.Dtos.responseDto import ResponseDto
from Redis_Cache.redis_cache import RedisCache

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

redisCache = RedisCache()
resp=Response()

@app.route('/healthcheck', methods=['GET'])
def HealthCheck():
    resp = Response()
    resp.status_code = 200
    return jsonify({'status': 'alive!'})

@app.route('/proxypt/preguntas', methods=['GET'])
def consultar_preguntas():
    try:
        session = requests.Session()
        content = session.get(redisCache.getKey("url_prueba_tecnica") + 'preguntas')
        resp=make_response(json.loads(content.text))
        resp.status_code = content.status_code
        return resp
    except Exception:
        response = ResponseDto()
        response.isError = 1
        response.data = ""
        response.mensaje = "Servicio de prueba técnica fallando"
        response.errors = [{'error': 'Servicio {} no encontrado'.format(redisCache.getKey("url_prueba_tecnica") + 'preguntas')}]
        resp=make_response(response.__dict__)
        resp.status_code = 404
        return resp

@app.route('/proxypt/preguntas', methods=['POST'])
def crear_preguntas():
    try:
        print(request.get_json())
        session = requests.Session()
        content = session.post(url=redisCache.getKey("url_prueba_tecnica") + 'preguntas', json=request.get_json())
        resp=make_response(json.loads(content.text))
        resp.status_code = content.status_code
        return resp
    except Exception:
        response = ResponseDto()
        response.isError = 1
        response.data = ""
        response.mensaje = "Servicio de prueba técnica fallando"
        response.errors = [{'error': 'Servicio {} no encontrado'.format(redisCache.getKey("url_prueba_tecnica") + 'preguntas')}]
        resp=make_response(response.__dict__)
        resp.status_code = 404
        return resp

@app.route('/proxypt/preguntas', methods=['PUT'])
def modificar_preguntas():
    try:
        session = requests.Session()
        content = session.put(url=redisCache.getKey("url_prueba_tecnica") + 'preguntas', json=request.get_json())
        resp=make_response(json.loads(content.text))
        resp.status_code = content.status_code
        return resp
    except Exception:
        response = ResponseDto()
        response.isError = 1
        response.data = ""
        response.mensaje = "Servicio de prueba técnica fallando"
        response.errors = [{'error': 'Servicio {} no encontrado'.format(redisCache.getKey("url_prueba_tecnica") + 'preguntas')}]
        resp=make_response(response.__dict__)
        resp.status_code = 404
        return resp

if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
