import os
import enum

from sqlalchemy import (
    Column,
    MetaData,
    String,
    Table,
    Boolean,
    Integer,
    Enum,
    DateTime,
    create_engine,
)

metadata = MetaData()
class TipoTransaccion(str, enum.Enum):
    PROGRAMADA = 'PROGRAMADA'
    APLAZADA = 'APLAZADA'
    CANCELADA = 'CANCELADA'
    REPROGRAMADA = 'REPROGRAMADA'
    RECHAZADA = 'RECHAZADA'
    REALIZADA = 'REALIZADA'

entrevista_tabla = Table(
    'entrevistas', metadata,
    Column('id', Integer, primary_key=True),
    Column('cancelado', Boolean, nullable=False),
    Column('estado', Enum(TipoTransaccion)),
    Column('observacion', String, nullable=True),
    Column('resultado', Integer, nullable=True),
    Column('fecha_hora', DateTime, nullable=False) 
    )

def init_db_engine(db_uri=None):
    uri = db_uri or os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///entrevistas.db')
    db_engine = create_engine(uri)
    __create_tables_if_not_exists(db_engine)
    return db_engine

def db_connect(db_engine):
    return db_engine.connect()

def close_db_connection(db_connection):
    try:
        db_connection.close()
    except:
        pass

def __create_tables_if_not_exists(db_engine):
    entrevista_tabla.create(db_engine, checkfirst=True)