from Aplicacion.Exception import MyException

class BadRequestException(MyException):

    def __init__(self, data=None):
        MyException.__init__(self)
        self.data = data or {}

    def to_dict(self):
        return self.data