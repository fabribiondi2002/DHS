from ts.Contexto import Contexto
from ts.Id import *
class TablaSimbolos:
    
    def __init__(self):
        self.listaContextos = []
        self.listaContextos.append(Contexto())

    def agregarContexto(self):
        self.listaContextos.append(Contexto())

    def borrarContexto (self, cont):
        self.listaContextos.pop()

    def agregarID(self, id):
        if isinstance(id, Funcion):
            self.listaContextos[0].agregarSimbolo(id)
        else:
            # Para variables y otros símbolos, se agrega al contexto actual
            self.listaContextos[-1].agregarSimbolo(id)
        return id
        
    def buscarLocalID(self, id):
        return self.listaContextos[-1].getSimbolos().get(id)

    def buscarID(self, id):
        for cont in self.listaContextos:
            simbolo = cont.getSimbolos().get(id)
            if simbolo is not None:
                return simbolo
        return None
        
    def getContextos (self) :
        return self.listaContextos
                

    def actualizarId(self, id):
        if id.nombre in self.listaContextos[-1].getSimbolos():
            self.listaContextos[-1].eliminarSimbolo(id.nombre)
            self.listaContextos[-1].agregarSimbolo(id)
        else:
            raise ValueError(f"El identificador '{id.nombre}' no existe en el contexto actual.")
    def actualizarFuncion(self,id):
        if id.nombre in self.listaContextos[0].getSimbolos():
            self.listaContextos[0].eliminarSimbolo(id.nombre)
            self.listaContextos[0].agregarSimbolo(id)
        else:
            raise ValueError(f"El identificador '{id.nombre}' no existe en el contexto actual.")