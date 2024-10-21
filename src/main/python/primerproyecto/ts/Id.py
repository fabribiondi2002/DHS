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
    
class Variable (ID): 
    def __init__(self, nombre, tipo, valor=None, inicializado=False, accedido=False):
        super().__init__(nombre, tipo, inicializado, accedido)
        self.valor = valor

class Funcion :
    list <Variable> parametros