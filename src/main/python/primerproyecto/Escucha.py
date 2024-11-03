from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from ts.TablaSimbolos import TablaSimbolos
from ts.Contexto import *
from ts.Id import *
import copy
class Escucha (compiladoresListener):
    # numTokens = 0
    # numNodos = 0
    variablesAsignacion = []
    tablaSimbolos = TablaSimbolos()
    parametros = []
    argumentos = []
    conjunto_argumento = []
    pila_contador_arg = []
    uso_func = False
    def identificarTipo(self, cadena):
        #Verifica si la cadena ingresada es tipo int
        try:
            int(cadena)  
            return "int"
        except ValueError:
            #Verifica si la cadena ingresada es tipo Float en python que seria Double en C
            try:
                float(cadena)  
                return "double"
            #Si no es ni int ni double retorno que no es un numero
            except ValueError:
                return "no es un número"

     # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print('Comienzo de la compilacion\n')   
        contexto = self.tablaSimbolos.agregarContexto()

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        
        
        # for cont in contextos :
        #     for var in cont.getSimbolos() :
        #         if var.getInicializado() == False :
        #             print("Variable " + var.getNombre() + " no inicialiada.\n")
        #         else :
        #             if var.getAccedido() == False :
        #                 print("Variable " + var.getNombre() + " no accedida.\n")


        print('Fin de la compilacion')

    #Se entra a un nuevo bloque cada vez que se declara una funcion
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        #Cada vez que se entra a un nuevo bloque, se agrega un nuevo contexto
        self.tablaSimbolos.agregarContexto()
        #Se toman los IDs que estan en los parametros de la funcion y se los agrega a la tabla de simbolos del contexto creado
        for par in self.parametros :
            id = ID(par['nombre'],par['tipo'])
            id.setInicializado()
            self.tablaSimbolos.agregarID(id)

    def exitFuncion(self, ctx: compiladoresParser.FuncionContext):

        #Se verifica que la funcion no haya sido declarada anteriormente
        if self.tablaSimbolos.buscarID(ctx.getChild(1).getText()) != None:
            print("\nWARNING: La funcion " + ctx.getChild(1).getText() + " ya ha sido declarada.\n")
            return
        
        #Crea un objeto funcion y le asigna los parametros en la lista de parametros de la declaracion de la funcion
        func = Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(),copy.deepcopy(self.parametros))
        
        #Se agrega la funcion a la tabla de simbolos al contexto global
        self.tablaSimbolos.agregarID(func)

        #Se limpia la lista utilizada para guaradar los parametros
        self.parametros.clear()

    #Se identifica los parametros de la funcion a declarar
    def exitParametros(self, ctx: compiladoresParser.ParametrosContext):
        #Si el espacio de parametro no esta vacio, agrega el parametro a la lista de parametros junto con el nombre y el tipo
        if ctx.getChildCount() != 0 :
            param =  {"nombre": ctx.getChild(1).getText(), "tipo": ctx.getChild(0).getText()}
            self.parametros.append(param)

    def enterUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        self.uso_func = True
        self.pila_contador_arg.append(0)
    

    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        self.uso_func = False
        #Se busca la funcion a utilizar por el nombre
        func =self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        #Si la funcion existe se hace el checkeo de parametros y argumentos
        if  func != None :
            #Se inicializa una lista de argumentos auxiliar donde se van a juntar los IDs con las constantes y se les va a dar un tipo para poder comparar con los parametros
            lista_argumentos = []
            lista_aux = []
            #Se trae la lista que contiene la lista de cada espacio de argumentos pasados a la funcion
            listaArgumentosLlamadaAFuncion = self.argumentos
            #Se trae la lista de parametros almacenada en el objeto tipo Funcion
            param = func.getParametros()
            
            for arg in listaArgumentosLlamadaAFuncion :
                #Se identifica el tipo de argumento
                for simb in arg :
                    #Si es un ID
                    if simb["tipo"] != "int" and simb["tipo"] != "double":
                        #Se checkea que la variable haya sido declarada
                        if self.tablaSimbolos.buscarLocalID(simb["nombre"]) == None :
                            print("ERROR: La variable "+ simb["nombre"] + " no esta declarada.")
                        else :
                            
                            lista_aux.append(simb)
                            id = self.tablaSimbolos.buscarLocalID(simb["nombre"])
                            id.setAccedido()  
                            self.tablaSimbolos.actualizarId(id)
                    #Si es una constante, se identifica el tipo y se agrega a la lista de argumentos
                    else :
                        lista_aux.append(simb)
                lista_argumentos.append(lista_aux)
                lista_aux = []
        
            #Se comparan los argumentos con los parametros
            for pa in param:
                
                #Se recorre la lista de parametros mientras se va desapilando la lista de argumentos
                aux = lista_argumentos.pop()
                for aux_argumento in aux:
                    
                    if aux_argumento['tipo'] != pa['tipo'] :
                        print("WARNING: El argumento " + aux_argumento['nombre'] + " es de tipo " + aux_argumento['tipo'] + ". Se espera un argumento de tipo "+ pa['tipo'] + ".\n")
            
            #Se checkea si la pila de argumentos esta vacia
            cant_arg = self.pila_contador_arg.pop()
            if cant_arg < len(param):
                print("WARNING: Falta agregar argumentos a la llamada de la funcion.\n")
            #Se checkea no la pila de argumentos esta vacia despues de haber finalizado la comparacion
            elif cant_arg > len(param):
                print("WARNING: Sobran argumentos en la llamada a la funcion.\n")
            
            #Se actualiza el atributo de accedido de la funcion
            func.setAccedido()
            self.tablaSimbolos.actualizarId(func)
            return

        print("\nWARNING: La funcion " + ctx.getChild(0).getText() + " no ha sido declarada.\n")
        return    
    

    def exitArgumentos(self, ctx: compiladoresParser.ArgumentosContext):
        #Si la llamada a funcion tiene argumentos, se agregan a la lista de argumentos
        if ctx.getChildCount() != 0 :
            self.argumentos.append(self.conjunto_argumento)
            if self.pila_contador_arg:
                self.pila_contador_arg[-1] += 1 
            self.conjunto_argumento =[]

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):

        #Si no esta declarada la variable, la declaramos
        if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None :
            var = Variable(str(ctx.getChild(1).getText()), str(ctx.getChild(0).getText()))

            #Si el tercer token es un igual, se esta inicializando
            if (str(ctx.getChild(2).getText()) == '='):

                #Se checkea que las variables o constantes que se van a asignar son del mismo tipo que la variable a declarar
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
                    aux = {'tipo' : var.getTipo(), 'nombre' : var.getNombre()}
                    if self.uso_func :
                        self.conjunto_argumento.append(aux)
                    else :
                        self.variablesAsignacion.append(aux)
                    var.setAccedido()
                    self.tablaSimbolos.actualizarId(var)

                else :
                    print("ERROR: La variable "+ nombre + " no esta declarada\n")
                    return

            else :
                
                aux = {'tipo' : self.identificarTipo(ctx.getChild(0).getText()), 'nombre' : ctx.getChild(0).getText()}
                if self.uso_func :
                    self.conjunto_argumento.append(aux)
                else :
                    self.variablesAsignacion.append(aux)
            
        else:
            nombre = ctx.getChild(0).getChild(0).getText()
            func = self.tablaSimbolos.buscarID(nombre)
            if  func != None :
                    aux = {'tipo' : func.getTipo(), 'nombre' : func.getNombre()}
                    if self.uso_func :
                        self.conjunto_argumento.append(aux)
                    else :
                        self.variablesAsignacion.append(aux)
                    func.setAccedido()
                    self.tablaSimbolos.actualizarId(func)
            else :
                print("ERROR: La funcion"+ nombre + " no esta declarada\n")
                return


    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):

        var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
        if var != None :

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

    def enterIControl(self, ctx: compiladoresParser.IforContext):
        nuevo_contexto = Contexto()
    
        # Copia los símbolos del contexto actual
        contexto_actual = self.tablaSimbolos.getContextos()[-1]
        for id in contexto_actual.getSimbolos().values():
            nuevo_contexto.agregarSimbolo(id)  # Copia el símbolo

        # Agrega el nuevo contexto
        self.tablaSimbolos.agregarContexto(nuevo_contexto)

    def exitInit(self, ctx: compiladoresParser.InitContext):
        
        if ctx.getChild(0).getText() in {"int", "double", "char"}:
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
        elif ctx.getChild(1).getText() == "=":
            var = self.tablaSimbolos.buscarLocalID(ctx.getChild(0).getText())
            if var != None :

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