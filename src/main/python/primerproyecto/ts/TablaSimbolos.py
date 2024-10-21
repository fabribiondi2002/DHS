from Contexto import Contexto

class TablaSimbolos:
    listaContextos = []
    def __init__(self):
        self.listaContextos.append(Contexto())

    def agregarContexto(self):

        self.listaContextos.append(Contexto())

    def borrarContexto (self, cont):
        self.listaContextos.pop()

    def agregarID (self, id):
        
        self.listaContextos[-1].agregarSimbolo(id)

    def buscarLocalID (self, id):
        
        if id in self.listaContextos[-1].getSimbolos() :
            return id
        else :
            return None

    def buscarID (self, id):

        for cont in self.listaContextos:

            if id in cont.getSimbolos() :
                return id
        
        return None
                

    
        
    

