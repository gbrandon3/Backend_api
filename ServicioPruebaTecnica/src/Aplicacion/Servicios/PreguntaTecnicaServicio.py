from Aplicacion.MyException import MyExcepcion
from Dominio.Dtos.responseDto import Response
from Dominio.Interfaces.PreguntaServicioInterface import PreguntaServicioInterface
from Dominio.Modelos.Pregunta import PreguntaNew, PreguntaUpd

class PreguntaTecnicaServicio(PreguntaServicioInterface):
    def obtenerPregunta(repositorio):
        preguntas = repositorio.consultar()
        response = Response()
        if(len(preguntas) == 0):
            response.isError = 1
            response.data = ""
            response.mensaje = "No hay datos"
            response.errors = [{'error': 'No hay preguntas configuradas'}]
            return response
        
        serializable_data = []
        for item in preguntas:
            serializable_item = {
                'id': item['id'],
                'pregunta': item['pregunta'],
                'vigente': item['vigente']
            }
            serializable_data.append(serializable_item)
        
        response.data = serializable_data
        response.isError = 0
        response.errors = ""
        response.mensaje = ""

        return response
    
    def crearPregunta(pregunta, repositorio):        
        pregunta = PreguntaNew(
            pregunta = pregunta['pregunta'],
            vigente= pregunta['vigente']
        )
        repositorio.crear(pregunta)
        response = Response()
        response.data = True
        response.isError = 0
        response.errors = ""
        response.mensaje = "Se agrego la pregunta en la base de datos"

        return response 
        
    
    def modificarPregunta(pregunta, repositorio):        
        pregunta = PreguntaUpd(
            id = pregunta['id'],
            pregunta = pregunta['pregunta'],
            vigente= pregunta['vigente']
        )
        repositorio.modificar(pregunta)
        response = Response()
        response.data = True
        response.isError = 0
        response.errors = ""
        response.mensaje = "Se actualizo la pregunta en la base de datos"

        return response