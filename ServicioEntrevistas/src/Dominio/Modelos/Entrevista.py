class EntrevistaNew():
    def __init__(self, cancelado, estado, fecha_hora, observacion, resultado):
        self.cancelado = cancelado
        self.estado = estado
        self.observacion = observacion
        self.resultado = resultado
        self.fecha_hora = fecha_hora


    def __repr__(self):
        return f'<Entrevista {self.id}>'

    def as_dict(self):
        return {
            'cancelado': self.cancelado,
            'estado': self.estado,
            'observacion': self.observacion,
            'resultado': self.resultado,
            'fecha_hora': self.fecha_hora
        }
    
class EntrevistaUpd():
    def __init__(self, id, cancelado, estado, fecha_hora, observacion, resultado):
        self.id = id
        self.cancelado = cancelado
        self.estado = estado
        self.observacion = observacion
        self.resultado = resultado
        self.fecha_hora = fecha_hora


    def __repr__(self):
        return f'<Entrevista {self.id}>'

    def as_dict(self):
        return {
            'id': self.id,
            'cancelado': self.cancelado,
            'estado': self.estado,
            'observacion': self.observacion,
            'resultado': self.resultado,
            'fecha_hora': self.fecha_hora
        }