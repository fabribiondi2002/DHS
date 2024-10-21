class ID ():
    def __init__(self, nombre, tipo, inicializado = False, accedido = False):
        self.nombre = nombre
        self.tipo = tipo
        self.inicializado = inicializado
        self.accedido = accedido
    
    def setInicializado(self):
        self.inicializado=True

    def setAccedido(self):
        self.accedido=True

    def getNombre(self) :
        return self.nombre()
    
class Variable(ID): 
    pass

class Funcion :
    def __init__(self, nombre, tipo, parametros,inicializado=False, accedido=False):
        super().__init__(nombre, tipo, inicializado, accedido)
        self.parametros = parametros