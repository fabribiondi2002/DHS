from antlr4 import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from ts.TablaSimbolos import TablaSimbolos
from ts.Contexto import *
from ts.Id import *
import copy
class Escucha (compiladoresListener):
    #Lista utilizada para contener todos los factores que se utilizan en una asignacion
    variablesAsignacion = []
    #Se crea un objeto tabla de simbolos
    tablaSimbolos = TablaSimbolos()
    #Lista utilizada para guardar los parametros de una funcion
    parametros = []
    #Lista utilizada para guardar la lista que representa el conjunto de factores utilizados en un espacio de argumentos en una llamada a funcion
    argumentos = []
    #Lista utilizada para guardar el conjunto de factores utilizados en un espacio de argumentos en una llamada a funcion
    conjunto_argumento = []
    #Lista utilizada como pila para guardar la cantidad de espacios de argumentos que tiene una llamada a la funcio, sirve para poder anidar llamadas de funcion
    pila_contador_arg = []
    #Variable que sirve como bandera para saber si estamos en una llamada a funcion, se utiliza para hacer las listas de argumentos
    uso_func = False
    EsFuncion = False
    tipo_declaracion = None
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

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        #Si esta la funcion main se modifica para que siempre sea accedida
        func = self.tablaSimbolos.buscarID("main")
        if func != None :
            func.setAccedido()
            self.tablaSimbolos.actualizarId(func)

        cont = self.tablaSimbolos.borrarContexto()
        for var in cont.getSimbolos().values() :
            if isinstance(var,Funcion) : 
                if var.getAccedido() == False :
                    print("WARNING: La funcion " + var.getNombre() + " no ha sido accedida.\n")
            else :
                    if var.getInicializado() == False :
                        print("WARNING: La variable " + var.getNombre() + " no ha sido inicializada.\n")
                    else :
                        if var.getAccedido() == False :
                            print("WARNING: La variable " + var.getNombre() + " no ha sido accedida.\n")
        
        
        
        print('Fin de la compilacion')

    def enterFuncion(self, ctx: compiladoresParser.FuncionContext):
        self.EsFuncion = True
    #Se entra a un nuevo bloque cada vez que se declara una funcion
    
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        #Cada vez que se entra a un nuevo bloque, se agrega un nuevo contexto
        self.tablaSimbolos.agregarContexto()
        if self.EsFuncion == True :
            #Se toman los IDs que estan en los parametros de la funcion y se los agrega a la tabla de simbolos del contexto creado
            for par in self.parametros :
                id = Variable(par['nombre'],par['tipo'])
                id.setInicializado()
                self.tablaSimbolos.agregarID(id)
            self.EsFuncion = False

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        #Se checkea si las variables y funciones fueron accedidas e inicializadas
        
        cont = self.tablaSimbolos.borrarContexto()
        for var in cont.getSimbolos().values() :
            if isinstance(var,Funcion) : 
                if var.getAccedido() == False :
                    print("WARNING: La funcion " + var.getNombre() + " no ha sido accedida.\n")
            else :
                    if var.getInicializado() == False :
                        print("WARNING: La variable " + var.getNombre() + " no ha sido inicializada.\n")
                    else :
                        if var.getAccedido() == False :
                            print("WARNING: La variable " + var.getNombre() + " no ha sido accedida.\n")

    def exitPrototipo(self, ctx: compiladoresParser.PrototipoContext):
        #Se verifica que el prototipo de la funcion no haya sido declarado anteriormente
        if self.tablaSimbolos.buscarID(ctx.getChild(1).getText()) != None:
            print("\nWARNING: El prototipo de la funcion " + ctx.getChild(1).getText() + " ya ha sido declarada.\n")
            return
        
        #Crea un objeto funcion y le asigna los parametros en la lista de parametros de la declaracion de la funcion
        func = Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(),copy.deepcopy(self.parametros))
        #Se agrega la funcion a la tabla de simbolos al contexto global
        self.tablaSimbolos.agregarID(func)

        #Se limpia la lista utilizada para guaradar los parametros
        self.parametros.clear()

    def exitFuncion(self, ctx: compiladoresParser.FuncionContext):
        func = Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(),copy.deepcopy(self.parametros))
        #Se verifica que la funcion no haya sido declarada anteriormente
        func_aux = self.tablaSimbolos.buscarID(ctx.getChild(1).getText())
        if func_aux != None:
            if func_aux.getInicializado() :
                print("\nWARNING: La funcion " + ctx.getChild(1).getText() + " ya ha sido declarada.\n")
                self.parametros.clear()
                return
            
            if func_aux.getTipo() != func.getTipo():
                print("WARNING: El tipo de dato de retorno de la funcion es " + func.getTipo() +". Segun el prototipo de la misma, se espera un tipo de dato de retorno " + func_aux.getTipo() + ".\n")
            aux_par_prot = func_aux.getParametros()
            aux_par_func = copy.deepcopy(self.parametros)

            if len(aux_par_func) > len(aux_par_prot):
                print("ERROR: Hay mas parametros en la declaracion de la funcion que en su prototipo./n")
            elif len(aux_par_func) < len(aux_par_prot)  :
                print("ERROR: Hay mas parametros en el prototipo de la funcion que en su declaracion./n")

            for par in aux_par_prot:
                if not aux_par_func :
                    break
                aux = aux_par_func.pop()
                if aux["tipo"]  != par["tipo"]:
                    print("WARNING: El parametro de la declaracion de funcion " + aux['nombre'] + " es de tipo " + aux['tipo'] + ". Se espera un argumento de tipo "+ par['tipo'] + " segun el prototipo.\n")
            func.setInicializado()
            self.tablaSimbolos.actualizarId(func)
            self.parametros.clear()
            return


        #Crea un objeto funcion y le asigna los parametros en la lista de parametros de la declaracion de la funcion
        func = Funcion(ctx.getChild(1).getText(),ctx.getChild(0).getText(),copy.deepcopy(self.parametros))
        func.setInicializado()
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
        #Se levanta la bandera indicadora de que se esta haciendo una llamada a funcion
        self.uso_func = True
        #Se agrega a la pila un contador de argumentos de la llamada a funcion
        self.pila_contador_arg.append(0)
    

    def exitUsofuncion(self, ctx: compiladoresParser.UsofuncionContext):
        #Se baja la bandera de que se esta en una llamada a funcion
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
                        if self.tablaSimbolos.buscarID(simb["nombre"]) == None :
                            print("ERROR: La variable "+ simb["nombre"] + " no esta declarada.")
                        else :
                            lista_aux.append(simb)
                            id = self.tablaSimbolos.buscarID(simb["nombre"])
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
                    #Se checkea si los tipos de datos de los argumentos son iguales a los de los parametros
                    if aux_argumento['tipo'] != pa['tipo'] :
                        print("WARNING: El argumento " + aux_argumento['nombre'] + " es de tipo " + aux_argumento['tipo'] + ". Se espera un argumento de tipo "+ pa['tipo'] + ".\n")
            
            #Se checkea si la pila de argumentos esta vacia utilizando el contador de argumentos para comparar la cantidad de argumentos con la cnatida de parametros
            cant_arg = self.pila_contador_arg.pop()
            if cant_arg < len(param):
                print("WARNING: Falta agregar argumentos a la llamada de la funcion.\n")
            elif cant_arg > len(param):
                print("WARNING: Sobran argumentos en la llamada a la funcion.\n")
            
            #Se actualiza el atributo de accedido de la funcion
            func.setAccedido()
            self.tablaSimbolos.actualizarId(func)
            return
        
        print("ERROR: La funcion " + ctx.getChild(0).getText() + " no ha sido declarada.\n")
        return    
    

    def exitArgumentos(self, ctx: compiladoresParser.ArgumentosContext):
        #Si la llamada a funcion tiene argumentos, se agregan a la lista de argumentos y se aumenta el contador de cantidad de argumentos
        if ctx.getChildCount() != 0 :
            self.argumentos.append(self.conjunto_argumento)
            if self.pila_contador_arg:
                self.pila_contador_arg[-1] += 1 
            #Se limpia la lista de factores en los argumentos
            self.conjunto_argumento =[]

    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        self.tipo_declaracion = str(ctx.getChild(0).getText())
        #Si no esta declarada la variable, la declaramos
        if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None :
            var = Variable(str(ctx.getChild(1).getText()), str(ctx.getChild(0).getText()))

            #Si el tercer token es un igual, se esta inicializando
            if (ctx.getChildCount() > 2):

                #Se checkea que las variables o constantes que se van a asignar son del mismo tipo que la variable a declarar
                for aux in self.variablesAsignacion :
                    if aux["tipo"] != var.getTipo():
                        print("WARNING: La variable " + aux["nombre"] + " es de tipo " + aux["tipo"] + ". Se espera una variable tipo "+ var.getTipo()+ "\n")
                
                var.setInicializado()
                #Se limpia la lista de variables de asignacion
                self.variablesAsignacion.clear()         
            #Se agrega la variable al contexto
            self.tablaSimbolos.agregarID(var)
        else :
            #Si esta declara la variable, mandamos un error
            print("ERROR: Ya existe una variable llamada " + str(ctx.getChild(1).getText())+ ".\n")
            return
        

    def exitDeclaracionp(self, ctx: compiladoresParser.DeclaracionpContext):
        if ctx.getChildCount() > 0:
            #Si no esta declarada la variable, la declaramos
            if self.tablaSimbolos.buscarLocalID(ctx.getChild(1).getText()) == None :
                var = Variable(str(ctx.getChild(1).getText()), self.tipo_declaracion)

                #Si el tercer token es un igual, se esta inicializando
                if (ctx.getChildCount() > 3):

                    #Se checkea que las variables o constantes que se van a asignar son del mismo tipo que la variable a declarar
                    for aux in self.variablesAsignacion :
                        if aux["tipo"] != var.getTipo():
                            print("WARNING: La variable " + aux["nombre"] + " es de tipo " + aux["tipo"] + ". Se espera una variable tipo "+ var.getTipo()+ "\n")
                    
                    var.setInicializado()
                    #Se limpia la lista de variables de asignacion
                    self.variablesAsignacion.clear()         
                #Se agrega la variable al contexto
                self.tablaSimbolos.agregarID(var)
            else :
                #Si esta declara la variable, mandamos un error
                print("ERROR: Ya existe una variable llamada " + str(ctx.getChild(1).getText())+ ".\n")
                return

    def exitDeclaraciones(self, ctx: compiladoresParser.DeclaracionesContext):
        self.tipo_declaracion = None
        
    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        #Se checkea si el factor es una funcion
        if  not ctx.getChild(0).getChildCount() > 1 :
            #Se checkea si el factor no es una expresion entre parentesis
            nombre = ctx.getChild(0).getText()
            if nombre != "(" :
                #Se checkea si es una Variable o una constante
                if self.identificarTipo(nombre) != "int" and self.identificarTipo(nombre) != "double":
                    #Si es una variable se checkea que exista 
                    var = self.tablaSimbolos.buscarID(nombre)
                    if  var != None :
                        #Se checkea si la variable esta inicializada
                        if var.getInicializado() == False :
                            print("ERROR: La variable "+ nombre + " no esta inicializada.\n")

                        #Se checkea si el factor tipo variable pertenece a un argumento o a una asignacion
                        aux = {'tipo' : var.getTipo(), 'nombre' : var.getNombre()}
                        if self.uso_func :
                            self.conjunto_argumento.append(aux)
                        else :
                            self.variablesAsignacion.append(aux)
                        #Se actualiza la variable
                        var.setAccedido()
                        self.tablaSimbolos.actualizarId(var)

                    else :
                        print("ERROR: La variable "+ nombre + " no esta declarada\n")
                        return

                else :
                    #Se checkea si el factor tipo constante pertenece a un argumento o a una asignacion
                    aux = {'tipo' : self.identificarTipo(ctx.getChild(0).getText()), 'nombre' : ctx.getChild(0).getText()}
                    if self.uso_func :
                        self.conjunto_argumento.append(aux)
                    else :
                        self.variablesAsignacion.append(aux)
        #Si es una funcion
        else:
            #Recuperamos el nombre de la funcion y se checkea si la funcion existe
            nombre = ctx.getChild(0).getChild(0).getText()
            func = self.tablaSimbolos.buscarID(nombre)
            if  func != None :
                    #Se checkea si el factor tipo funcion pertenece a un argumento o a una asignacion
                    aux = {'tipo' : func.getTipo(), 'nombre' : func.getNombre()}
                    if self.uso_func :
                        self.conjunto_argumento.append(aux)
                    else :
                        self.variablesAsignacion.append(aux)
                    func.setAccedido()
                    self.tablaSimbolos.actualizarId(func)

    def enterAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        #Se limpia la lista de varibles de asignacion (Esto es por si hubo una operacion que no haya sido una asignacion que use la lista CORREGIR)
        self.variablesAsignacion.clear()
        
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        #Se checkea si la variable a la cual queremos hacerle una asignacion existe
        var = self.tablaSimbolos.buscarID(ctx.getChild(0).getText())
        if var != None :
            #Se checkea los tipos de datos de los IDs o constantes que se van a asignar sean los mismos que la variable a hacerle asignacion
            for aux in self.variablesAsignacion :
                if aux["tipo"] != var.getTipo():
                    print("WARNING: La variable o funcion " + aux["nombre"] + " es de tipo " + aux["tipo"] + ". Se espera una variable tipo "+ var.getTipo()+ "\n")
            #Se actualiza la varible
            var.setInicializado()
            self.tablaSimbolos.actualizarId(var)
            self.variablesAsignacion.clear()
        else :
            print('ERROR: La variable ' + ctx.getChild(0).getText() + ' no esta declarada.\n')
            self.variablesAsignacion.clear()
        return

