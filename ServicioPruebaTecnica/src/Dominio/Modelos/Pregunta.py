class PreguntaNew():
    def __init__(self, pregunta, vigente):
        self.pregunta = pregunta
        self.vigente = vigente

    def __repr__(self):
        return f'<Pregunta {self.id}>'

    def as_dict(self):
        return {
            'pregunta': self.pregunta,
            'vigente': self.vigente
        }
    
class PreguntaUpd():
    def __init__(self, id, pregunta, vigente):
        self.id = id
        self.pregunta = pregunta
        self.vigente = vigente

    def __repr__(self):
        return f'<Pregunta {self.id}>'

    def as_dict(self):
        return {
            'id': self.id,
            'pregunta': self.pregunta,
            'vigente': self.vigente
        }