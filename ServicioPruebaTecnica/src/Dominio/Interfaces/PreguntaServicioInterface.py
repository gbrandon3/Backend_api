from abc import (
    ABCMeta,
    abstractmethod
)

class PreguntaServicioInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def obtenerPregunta(self, repositorio):
        pass

    def crearPregunta(self, pregunta, repositorio):
        pass

    def modificarPregunta(self, pregunta, repositorio):
        pass