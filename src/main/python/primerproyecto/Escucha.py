from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from ts.TablaSimbolos import TablaSimbolos
from ts.Id import *
class Escucha (compiladoresListener):
    numTokens = 0
    numNodos = 0

    tablaSimbolos = TablaSimbolos()

     # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienzo de la compilacion\n')

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        contextos = self.tablaSimbolos.getContextos()

        for cont in contextos :
            for var in cont.getSimbolos() :
                if var.getInicializado() == False :
                    print("Variable " + var.getNombre() + " no inicialiada.\n")
                else :
                    if var.getAccedido() == False :
                        print("Variable " + var.getNombre() + " no accedida.\n")

        print('Fin de la compilacion')
    

    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        contexto = self.tablaSimbolos.agregarContexto()

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        #Si no esta declarada la variable, la declaramos
        if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText() != None) :
            var = Variable(str(ctx.getChild(1).getText()), str(ctx.getChild(0).getText()))

            #Si el tercer token es un igual, se esta inicializando
            if (str(ctx.getChild(2).getText()) == '='):
                var.setInicializado()
            #Se agrega la variable al contexto
            self.tablaSimbolos.agregarID(var)

        #Si esta declara la variable, mandamos un error
        else :
            print("Ya existe una variable llamada " + str(ctx.getChild(1).getText())+ "\n")
            return

    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.getChildCount() == 1 :
            
            var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
            
            if  var != None :
                
                if var.getInicializado() == False :
                    print("La variable "+ ctx.getChild(0).getText() + " no esta inicializada\n")
                    return
                
                var.setAccedido()
                tipo = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText()).getTipo()

            else :
                print("La variable "+ ctx.getChild(0).getText() + " no esta declarada\n")  
                return 
            
            self.tablaSimbolos.actualizarId(var)



        
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