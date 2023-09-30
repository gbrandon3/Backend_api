from abc import (
    ABCMeta,
    abstractmethod
)

class EntrevistaRepositorioInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def consultar(self):
        pass

    def crear(self, pregunta):
        pass

    def modificar(self, pregunta):
        pass