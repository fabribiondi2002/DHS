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

     # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienzo de la compilacion\n')

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

    def enterFuncionreturn(self, ctx: compiladoresParser.FuncionreturnContext):
        print("Declarando funcion tipo return/n")
    def exitFuncionreturn(self, ctx: compiladoresParser.FuncionreturnContext):
        i=3
        while ctx.getChild(i).getText() != ')':
            if ctx.getChild(i).getText() in {'int', 'char', 'double'} :
        funcion = Funcion(str(ctx.getChild(1).getText()), str(ctx.getChild(0).getText()))
        aux = {'tipo' : var.getTipo(), 'nombre' : var.getNombre()}

    

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