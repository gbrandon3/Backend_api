from Infraestructura.Repositorios.BaseRepositorio import BaseRepositorio
from Dominio.Interfaces.EntrevistaRepositorioInterface import EntrevistaRepositorioInterface
from Infraestructura.Database import entrevista_tabla

class PreguntaRepositorio(BaseRepositorio, EntrevistaRepositorioInterface):
    def consultar(self):
        with self.db_connection.begin():
            return self.db_connection.execute(
                entrevista_tabla.select()
            ).mappings().all()
        
    def crear(self, entrevista):
        with self.db_connection.begin():
            return self.db_connection.execute(
                entrevista_tabla.insert(),
                entrevista.as_dict()
            )
    
    def modificar(self, entrevistaUpd):
        with self.db_connection.begin():
            return self.db_connection.execute(
                entrevista_tabla.update().where(entrevista_tabla.c.id==entrevistaUpd.id).values(
                    cancelado=entrevistaUpd.cancelado,
                    estado=entrevistaUpd.estado,
                    observacion=entrevistaUpd.observacion,
                    resultado=entrevistaUpd.resultado,
                    fecha_hora=entrevistaUpd.fecha_hora
                    )
            )