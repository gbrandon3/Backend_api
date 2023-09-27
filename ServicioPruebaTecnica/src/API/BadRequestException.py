from Aplicacion.MyException import MyExcepcion

class BadRequestException(MyExcepcion):

    def __init__(self, data=None):
        MyExcepcion.__init__(self)
        self.data = data or {}

    def to_dict(self):
        return self.data