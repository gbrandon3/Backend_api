from Infraestructura.repositorios.BaseRepositorio import BaseRepositorio
from Dominio.Interfaces.PreguntaRepositorioInterface import PreguntaRepositorioInterface
from Infraestructura.Database import pregunta_tabla

class PreguntaRepositorio(BaseRepositorio, PreguntaRepositorioInterface):
    def consultar(self):
        with self.db_connection.begin():
            return self.db_connection.execute(
                pregunta_tabla.select()
            ).mappings().all()
        
    def crear(self, preguntas):
        with self.db_connection.begin():
            return self.db_connection.execute(
                pregunta_tabla.insert(),
                preguntas.as_dict()
            )
    
    def modificar(self, preguntaupd):
        with self.db_connection.begin():
            return self.db_connection.execute(
                pregunta_tabla.update().where(pregunta_tabla.c.id==preguntaupd.id).values(pregunta=preguntaupd.pregunta, vigente= preguntaupd.vigente)
            )