from ts.Contexto import Contexto
from ts.Id import *
class TablaSimbolos:
    
    def __init__(self):
        #Crea una lista de contextos y agrega el contexto global
        self.listaContextos = []
        self.listaContextos.append(Contexto())

    def agregarContexto(self):
        #Agrega un contexto al final de la pila
        self.listaContextos.append(Contexto())

    def borrarContexto (self):
        #Elimina el contexto actual
        self.listaContextos.pop()

    def agregarID(self, id):
        #Si es una funcion, se la agrega al contexto global
        if isinstance(id, Funcion):
            self.listaContextos[0].agregarSimbolo(id)
        else:
            # Si es una variable, se agrega al contexto actual
            self.listaContextos[-1].agregarSimbolo(id)
        return id
        
    def buscarLocalID(self, id):
        #Se busca el ID en el contexto local
        return self.listaContextos[-1].getSimbolos().get(id)

    def buscarID(self, id):
        #Se busca el ID en todos los contextos
        for cont in self.listaContextos:
            simbolo = cont.getSimbolos().get(id)
            if simbolo is not None:
                return simbolo
        return None
        
    def getContextos (self) :
        #Retorna la totalidad de los contextos
        return self.listaContextos
                
    def actualizarId(self, id):
        #Busca el ID a actualizar por el nombre en el contexto local, lo elimina y agrega el ID modificado
        if isinstance(id, Funcion):
            #Busca la funcion en el contexto global por el nombre, la elimina y agrega la funcion modificada
            if id.nombre in self.listaContextos[0].getSimbolos():
                self.listaContextos[0].eliminarSimbolo(id.nombre)
                self.listaContextos[0].agregarSimbolo(id)
                return id
            else:
                raise ValueError(f"La funcion '{id.nombre}' no existe.")
        else:
            if id.nombre in self.listaContextos[-1].getSimbolos():
                self.listaContextos[-1].eliminarSimbolo(id.nombre)
                self.listaContextos[-1].agregarSimbolo(id)
                return id
            else:
                raise ValueError(f"La variable '{id.nombre}' no existe en el contexto actual.")
        return None