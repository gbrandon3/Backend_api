import os

from sqlalchemy import (
    Column,
    MetaData,
    String,
    Table,
    Boolean,
    Integer,
    create_engine,
)

metadata = MetaData()

pregunta_tabla = Table(
    'preguntas', metadata,
    Column('id', Integer, primary_key=True),
    Column('pregunta', String(250), nullable=False),
    Column('vigente', Boolean, nullable=False)
)

def init_db_engine(db_uri=None):
    uri = db_uri or os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///pruebas_tecnicas.db')
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
    pregunta_tabla.create(db_engine, checkfirst=True)