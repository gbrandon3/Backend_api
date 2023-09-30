from Aplicacion.Exception import MyException
from Dominio.Dtos.responseDto import Response
from Dominio.Interfaces.EntrevistaServicioInterface import EntrevistaServicioInterface
from Dominio.Modelos.Entrevista import EntrevistaNew, EntrevistaUpd

class EntrevistaServicio(EntrevistaServicioInterface):

    def agregarEntrevista(entrevista, repositorio):        
        entrevista = EntrevistaNew(
            cancelado = entrevista['cancelado'],
            estado = entrevista['estado'],
            observacion = entrevista['observacion'],
            resultado = entrevista['resultado'],
            fecha_hora = entrevista['fecha_hora']
        )
        repositorio.crear(entrevista)
        response = Response()
        response.data = True
        response.isError = 0
        response.errors = ""
        response.mensaje = "Se agrego la entrevista en la base de datos"

        return response  

    def modificarEntrevista(entrevista, repositorio):        
        entrevista = EntrevistaUpd(
            id = entrevista['id'],
            cancelado = entrevista['cancelado'],
            estado = entrevista['estado'],
            observacion = entrevista['observacion'],
            resultado = entrevista['resultado'],
            fecha_hora = entrevista['fecha_hora']
        )
        repositorio.modificar(entrevista)
        response = Response()
        response.data = True
        response.isError = 0
        response.errors = ""
        response.mensaje = "Se actualizo la entrevista en la base de datos"

        return response
    
    def obtenerEntrevista(entrevista, repositorio):
        entrevistas = repositorio.consultar()
        response = Response()
        if len(entrevistas) == 0:
            response.isError = 1
            response.data = ""
            response.mensaje = "No hay datos"
            response.errors = [{'error': 'No hay entrevistas registradas'}]
            return response
        
        serializable_data = []
        for item in entrevistas:
            serializable_item = {
                'id': item['id'],
                'cancelado': item['pregunta'],
                'estado': item['estado'],
                'observacion': item['observacion'],
                'resultado': item['resultado'],
                'fecha_hora': item['fecha_hora']
            }
            serializable_data.append(serializable_item)
        
        response.data = serializable_data
        response.isError = 0
        response.errors = ""
                
        return response