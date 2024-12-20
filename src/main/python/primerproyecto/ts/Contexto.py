from ts.Id import ID

class Contexto:
    def __init__(self):
        self.simbolos = dict()

    def agregarSimbolo (self, id):
        self.simbolos[id.nombre] = id

    def getSimbolos(self):
        return self.simbolos
    
    def eliminarSimbolo (self,id):
        return self.simbolos.pop(id)
