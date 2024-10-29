from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from ts.TablaSimbolos import TablaSimbolos
from ts.Id import *
class Escucha (compiladoresListener):
    # numTokens = 0
    # numNodos = 0
    variablesAsignacion = []
    tablaSimbolos = TablaSimbolos()
    funciones = []
    parametros = []
    argumentos = []

    def identificarTipo(self, cadena):
        try:
            int(cadena)  # Verifica si puede convertirse a entero
            return "int"
        except ValueError:
            try:
                float(cadena)  # Verifica si puede convertirse a flotante
                return "float"
            except ValueError:
                return "no es un número"

     # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienzo de la compilacion\n')

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        contextos = self.tablaSimbolos.getContextos()
        print(self.funciones)
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


    def exitFuncion(self, ctx: compiladoresParser.FuncionContext):
        for aux in self.funciones :
            if ctx.getChild(1).getText() == aux["nombre"] :
                print("\nWARNING: La funcion " + ctx.getChild(1).getText() + " ya ha sido declarada.\n")
                return
        func =  {"nombre": ctx.getChild(1).getText(), "tipo": ctx.getChild(0).getText(), "parametros": self.parametros}
        self.funciones.append(func)
        self.parametros.clear()

    def exitParametros(self, ctx: compiladoresParser.ParametrosContext):
        if ctx.getChildCount() != 0 :
            param=  {"nombre": ctx.getChild(1).getText(), "tipo": ctx.getChild(0).getText()}
            self.parametros.append(param)
            print(ctx.getChild(1).getText())


    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):

        #VER COMOL HACER

        for func in self.funciones :
            if ctx.getChild(0).getText() == func["nombre"] :
        
                arg = self.argumentos
                param = func["parametros"]
                lista_parametros = []
                for simb in arg :
                    print(simb)
                    print(type(simb))
                    if not simb.isdigit():
                        if self.tablaSimbolos.buscarLocalID(simb) == None :
                            print("ERROR: La variable "+ simb + " no esta declarada.")
                        else :
                            lista_parametros.append(self.tablaSimbolos.buscarLocalID(simb).getTipo())  
                    else :
                        lista_parametros.append(self.identificarTipo(simb))
                
                print("parametros---------------")
                print(lista_parametros)
                print("parametros---------------")


                for pa in param:
                    aux 





                # for pa in param:
                #     aux = arg.pop()
                #     if arg.isdigit():
                #         if type(arg) is int and pa["tipo"] == "double":
                #             print("\nWARNNING: El argumento " + arg + " no es de tipo double.\n")
                #         if type(arg) is float and pa["tipo"] == "int":
                #             print("\nWARNNING: El argumento " + arg + " no es de tipo int.\n")
                #     else:
                #         if aux != pa["nombre"] :
                #             print("\nWARNNING: El argumento " + arg + " no es de tipo int.\n")
                    


                return    

        print("\nWARNING: La funcion " + ctx.getChild(0).getText() + " no ha sido declarada.\n")
        return    


        
        #        aux2 = aux["parametros"]
        #        if self.argumentos.pop() != aux2.pop():
        #            print("E")


        #        return

        # 

    def exitArgumentos(self, ctx: compiladoresParser.ArgumentosContext):
        if ctx.getChildCount() != 0 :
            self.argumentos.append(ctx.getChild(0).getText())
    




    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):

        print('Declaracion \n')
        #Si no esta declarada la variable, la declaramos
        print('Se intentará declarar la variable ' + ctx.getChild(1).getText())

        if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None :
            var = Variable(str(ctx.getChild(1).getText()), str(ctx.getChild(0).getText()))
            print('Se declaró la variable ' + ctx.getChild(1).getText())

            #Si el tercer token es un igual, se esta inicializando
            if (str(ctx.getChild(2).getText()) == '='):
                print('Se inicializo la variable ' + ctx.getChild(1).getText())
                var.setInicializado()

            #Se agrega la variable al contexto
            self.tablaSimbolos.agregarID(var)
        else :
            #Si esta declara la variable, mandamos un error
            print("ERROR: Ya existe una variable llamada " + str(ctx.getChild(1).getText())+ ".\n")
            return

    def exitFactor(self, ctx: compiladoresParser.FactorContext):

        print('Factor \n')

        nombre = ctx.getChild(0).getText()
        print('nombre '+ nombre)
        if not nombre.isdigit():
            var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
            if  var != None :

                if var.getInicializado() == False :
                    print("ERROR: La variable "+ ctx.getChild(0).getText() + " no esta inicializada.\n")
                    return
                print('Se accedio a la variable ' + ctx.getChild(0).getText())
                aux = {'tipo' : var.getTipo(), 'nombre' : var.getNombre()}
                self.variablesAsignacion.append(aux)
                var.setAccedido()

            else :
                print("ERROR: La variable "+ ctx.getChild(0).getText() + " no esta declarada\n")
                return

            self.tablaSimbolos.actualizarId(var)
        else :
            aux = {'tipo' : 'int', 'nombre' : ctx.getChild(0).getText()}
            self.variablesAsignacion.append(aux)
            print('El factor es el numero ' + ctx.getChild(0).getText())

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):


        print('Se intentara asignar un valor a la variable ' + ctx.getChild(0).getText())
        var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
        if var != None :
            for aux in self.variablesAsignacion :
                if aux["tipo"] != var.getTipo():
                    print("WARNING: La variable " + aux["nombre"] + " es de tipo " + aux["tipo"] + ". Se espera una variable tipo "+ var.getTipo()+ "\n")

            var.setInicializado()
            self.tablaSimbolos.actualizarId(var)
            print('Se asigno un valor a la variable ' + ctx.getChild(0).getText() )
            self.variablesAsignacion.clear()
        else :
            print('La variable ' + ctx.getChild(0).getText() + ' no esta declarada.\n')
        print('Fin asignacion \n')
        return

    def enterAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        print('Inicio asignacion.')
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