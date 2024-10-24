from ts.Contexto import Contexto

class TablaSimbolos:
    
    def __init__(self):
        self.listaContextos = []
        self.listaContextos.append(Contexto())

    def agregarContexto(self):

        self.listaContextos.append(Contexto())

    def borrarContexto (self, cont):
        self.listaContextos.pop()

    def agregarID(self, id):
        
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
