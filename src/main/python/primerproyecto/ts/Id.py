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
        return self.nombre
    
    def getTipo(self) :
        return self.tipo
    
    def getInicializado(self):
        return self.inicializado
    
    def getAccedido(self):
        return self.accedido
    
class Variable(ID): 
    pass

class Funcion(ID):
    def __init__(self, nombre, tipo, parametros, inicializado=True, accedido=False):
        super().__init__(nombre, tipo, inicializado, accedido)
        self.parametros = parametros
    def getParametros(self):
        return self.parametros
        
