from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from ts.TablaSimbolos import TablaSimbolos
from ts.Id import *
import copy
class Escucha (compiladoresListener):
    # numTokens = 0
    # numNodos = 0
    variablesAsignacion = []
    tablaSimbolos = TablaSimbolos()
    parametros = []
    argumentos = []

    def identificarTipo(self, cadena):
        try:
            int(cadena)  # Verifica si puede convertirse a entero
            return "int"
        except ValueError:
            try:
                float(cadena)  # Verifica si puede convertirse a flotante
                return "double"
            except ValueError:
                return "no es un número"

     # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienzo de la compilacion\n')
        contexto = self.tablaSimbolos.agregarContexto()

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        contextos = self.tablaSimbolos.getContextos()
        
        # for cont in contextos :
        #     for var in cont.getSimbolos() :
        #         if var.getInicializado() == False :
        #             print("Variable " + var.getNombre() + " no inicialiada.\n")
        #         else :
        #             if var.getAccedido() == False :
        #                 print("Variable " + var.getNombre() + " no accedida.\n")


        print('Fin de la compilacion')


    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        contexto = self.tablaSimbolos.agregarContexto()
        for par in self.parametros :
            id = ID(par['nombre'],par['tipo'])
            id.setInicializado()
            self.tablaSimbolos.agregarID(id)


    def exitFuncion(self, ctx: compiladoresParser.FuncionContext):
        if self.tablaSimbolos.buscarID(ctx.getChild(1).getText()) != None:
            print("\nWARNING: La funcion " + ctx.getChild(1).getText() + " ya ha sido declarada.\n")
            return
        
        func =Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(),copy.deepcopy(self.parametros))
        self.tablaSimbolos.agregarID(func)
        self.variablesAsignacion.clear()
        self.parametros.clear()

    def exitParametros(self, ctx: compiladoresParser.ParametrosContext):
        if ctx.getChildCount() != 0 :
            param =  {"nombre": ctx.getChild(1).getText(), "tipo": ctx.getChild(0).getText()}
            self.parametros.append(param)


    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):

        func =self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if  func != None :
            
            arg = self.argumentos
            param = func.getParametros()
            lista_parametros = []
            for simb in arg :
                if not simb.isdigit():
                    if self.tablaSimbolos.buscarLocalID(simb) == None :
                        print("ERROR: La variable "+ simb + " no esta declarada.")
                    else :
                        lista_parametros.append({"nombre": simb, "tipo":self.tablaSimbolos.buscarLocalID(simb).getTipo()})  
                else :
                    lista_parametros.append({"nombre": simb, "tipo":self.identificarTipo(simb)})
            
            for pa in param:
                aux = lista_parametros.pop()
                if aux['tipo'] != pa['tipo'] :
                    print("WARNNING: El argumento " + aux['nombre'] + " es de tipo " + aux['tipo'] + ". Se espera un argumento de tipo "+ pa['tipo'] + ".\n")
            self.variablesAsignacion.clear()
            func.setAccedido()
            self.tablaSimbolos.actualizarFuncion(func)
            return

        print("\nWARNING: La funcion " + ctx.getChild(0).getText() + " no ha sido declarada.\n")
        self.variablesAsignacion.clear()
        return    

    def exitArgumentos(self, ctx: compiladoresParser.ArgumentosContext):
        if ctx.getChildCount() != 0 :
            self.argumentos.append(ctx.getChild(0).getText())
    




    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):

        #Si no esta declarada la variable, la declaramos

        if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None :
            var = Variable(str(ctx.getChild(1).getText()), str(ctx.getChild(0).getText()))

            #Si el tercer token es un igual, se esta inicializando
            if (str(ctx.getChild(2).getText()) == '='):

                
                for aux in self.variablesAsignacion :
                    if aux["tipo"] != var.getTipo():
                        print("WARNING: La variable " + aux["nombre"] + " es de tipo " + aux["tipo"] + ". Se espera una variable tipo "+ var.getTipo()+ "\n")
                var.setInicializado()
                
                self.variablesAsignacion.clear()         
            #Se agrega la variable al contexto
            self.tablaSimbolos.agregarID(var)
        else :
            #Si esta declara la variable, mandamos un error
            print("ERROR: Ya existe una variable llamada " + str(ctx.getChild(1).getText())+ ".\n")
            return

    def exitFactor(self, ctx: compiladoresParser.FactorContext):

        if  not ctx.getChild(0).getChildCount() > 1 :

            nombre = ctx.getChild(0).getText()
            if self.identificarTipo(nombre) != "int" and self.identificarTipo(nombre) != "double":

                var = self.tablaSimbolos.buscarLocalID(nombre)
                
                if  var != None :

                    if var.getInicializado() == False :
                        print("ERROR: La variable "+ nombre + " no esta inicializada.\n")
                        return
                    aux = {'tipo' : var.getTipo(), 'nombre' : var.getNombre()}
                    self.variablesAsignacion.append(aux)
                    var.setAccedido()

                else :
                    print("ERROR: La variable "+ nombre + " no esta declarada\n")
                    return
                
                self.tablaSimbolos.actualizarId(var)
                
            else :
                
                aux = {'tipo' : self.identificarTipo(ctx.getChild(0).getText()), 'nombre' : ctx.getChild(0).getText()}
                self.variablesAsignacion.append(aux)
        else:
            nombre = ctx.getChild(0).getChild(0).getText()
            func = self.tablaSimbolos.buscarID(nombre)
            if  func != None :
                    aux = {'tipo' : func.getTipo(), 'nombre' : func.getNombre()}
                    self.variablesAsignacion.append(aux)
                    func.setAccedido()

            else :
                print("ERROR: La funcion"+ nombre + " no esta declarada\n")
                return
            
            self.tablaSimbolos.actualizarFuncion(func)


    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):

        var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
        if var != None :
            print(self.variablesAsignacion)
            for aux in self.variablesAsignacion :
                
                if aux["tipo"] != var.getTipo():
                    print("WARNING: La variable o funcion " + aux["nombre"] + " es de tipo " + aux["tipo"] + ". Se espera una variable tipo "+ var.getTipo()+ "\n")

            var.setInicializado()
            self.tablaSimbolos.actualizarId(var)
            self.variablesAsignacion.clear()
        else :
            print('ERROR: La variable ' + ctx.getChild(0).getText() + ' no esta declarada.\n')
            self.variablesAsignacion.clear()
        return

    
            


    # # Enter a parse tree produced by compiladoresParser#iwhile.
    # def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
    #     print('Encontre WHILE')
    #     print('\tCantidad hijos: ' + str( ctx.getChildCount()))
    #     print('\tNodos: ' + str(self.numNodos))
    #     print('\tTokens: ' + str(self.numTokens))

    # # Exit a parse tree produced by compiladoresParser#iwhile.
    # def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
    #     print('Encontre WHILE')
    #     print('\tCantidad hijos: ' + str( ctx.getChildCount()))
    #     print('\tNodos: ' + str(self.numNodos))
    #     print('\tTokens: ' + str(self.numTokens))

    # # Enter a parse tree produced by compiladoresParser#declaracion.
    # def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
    #     print(' ### Declaracion')

    # # Exit a parse tree produced by compiladoresParser#declaracion.
    # def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
    #     print('Nombre variable: ' + ctx.getChild(1).getText())

    # def visitTerminal(self, node: TerminalNode):
    #     self.numTokens += 1

    # def visitErrorNode(self, node: ErrorNode):
    #     print('--->Error')

    # def enterEveryRule(self, ctx):
    #     self.numNodos += 1