from abc import (
    ABCMeta,
    abstractmethod
)

class EntrevistaServicioInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def agregarEntrevista(self, entrevista,repositorio):
        pass

    def auditoria(self, auditoria, repositorio):
        pass

    def autorizacion(self, token, repositorio):
        pass

    def modificarEntrevista(self, entrevista, repositorio):
        pass

    def obtenerEntrevista(self, entrevista, repositorio):
        pass