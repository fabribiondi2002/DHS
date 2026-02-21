import os
from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser


class Walker(compiladoresVisitor):

    # Constructor del generador de código intermedio
    def __init__(self):
        # Contador para temporales (t0, t1, t2, ...)
        self.tempCount = 0
        
        # Contador para etiquetas (l0, l1, l2, ...)
        self.labelCount = 0

        # Se asegura de que exista la carpeta output
        os.makedirs("output", exist_ok=True)

        # Archivo donde se escribirá el código intermedio
        self.out = open("output/CodigoIntermedio.txt", "w")
    

    # Cierra el archivo de salida
    def close(self):
        self.out.close()


    # Genera un nuevo temporal
    def newTemp(self):
        t = f"t{self.tempCount}"
        self.tempCount += 1
        return t


    # Genera una nueva etiqueta
    def newLabel(self):
        l = f"l{self.labelCount}"
        self.labelCount += 1
        return l


    # Emite una línea de código intermedio en el archivo
    def emit(self, text):
        self.out.write(text + "\n")


    # =========================
    # PROGRAMA
    # =========================

    # Punto de entrada del AST
    def visitPrograma(self, ctx):
        self.visit(ctx.instrucciones())


    # Recorre recursivamente la lista de instrucciones
    def visitInstrucciones(self, ctx):
        if ctx is None:
            return

        if ctx.instruccion():
            self.visit(ctx.instruccion())

        # Evita recursión infinita
        if ctx.instrucciones() and ctx.instrucciones() != ctx:
            self.visit(ctx.instrucciones())


    # =========================
    # FACTORES Y EXPRESIONES
    # =========================

    # Procesa factores: números, IDs, post-incremento, llamadas, etc.
    def visitFactor(self, ctx):

        # Caso número literal
        if ctx.NUMERO():
            return ctx.NUMERO().getText()

        # Caso variable simple
        if ctx.ID() and ctx.getChildCount() == 1:
            return ctx.ID().getText()

        # Caso post-incremento o post-decremento (x++ / x--)
        if ctx.ID() and ctx.getChildCount() == 2:
            var = ctx.ID().getText()
            op = ctx.getChild(1).getText()

            # Guardamos valor anterior
            old = self.newTemp()
            self.emit(f"{old} = {var}")

            # Calculamos nuevo valor
            t = self.newTemp()
            if op == "++":
                self.emit(f"{t} = {var} + 1")
            else:
                self.emit(f"{t} = {var} - 1")

            # Actualizamos variable
            self.emit(f"{var} = {t}")

            # Retorna el valor original (semántica post)
            return old

        # Caso llamada a función
        if ctx.usofuncion():
            return self.visit(ctx.usofuncion())

        # Caso expresión entre paréntesis
        return self.visit(ctx.opal())


    # Manejo de multiplicaciones, divisiones y módulo
    def visitTerm(self, ctx):
        left = self.visit(ctx.factor())
        tctx = ctx.t()

        while tctx and tctx.getChildCount() > 0:
            op = tctx.getChild(0).getText()
            right = self.visit(tctx.factor())

            tmp = self.newTemp()
            self.emit(f"{tmp} = {left} {op} {right}")
            left = tmp

            tctx = tctx.t()

        return left


    # Manejo de suma y resta
    def visitExp(self, ctx):
        left = self.visit(ctx.term())
        ectx = ctx.e()

        while ectx and ectx.getChildCount() > 0:
            op = ectx.getChild(0).getText()
            right = self.visit(ectx.term())

            t = self.newTemp()
            self.emit(f"{t} = {left} {op} {right}")
            left = t

            ectx = ectx.e()

        return left


    # Manejo de comparaciones
    def visitComp(self, ctx):

        # Caso simple (sin comparación)
        if ctx.comparadores() is None:
            return self.visit(ctx.exp(0))

        # Caso exp op exp
        left = self.visit(ctx.exp(0))
        right = self.visit(ctx.exp(1))
        op = ctx.comparadores().getText()

        t = self.newTemp()
        self.emit(f"{t} = {left} {op} {right}")
        return t


    # Manejo operador &&
    def visitLand(self, ctx):
        left = self.visit(ctx.comp())
        lp = ctx.landp()

        while lp and lp.getChildCount() > 0:
            right = self.visit(lp.comp())
            t = self.newTemp()
            self.emit(f"{t} = {left} && {right}")
            left = t
            lp = lp.landp()

        return left


    # Manejo operador ||
    def visitLor(self, ctx):
        left = self.visit(ctx.land())
        lp = ctx.lorp()

        while lp and lp.getChildCount() > 0:
            right = self.visit(lp.land())
            t = self.newTemp()
            self.emit(f"{t} = {left} || {right}")
            left = t
            lp = lp.lorp()

        return left


    # Entrada general de operación lógica/aritmética
    def visitOpal(self, ctx):
        return self.visit(ctx.lor())


    # =========================
    # ASIGNACIONES Y DECLARACIONES
    # =========================

    # Generación de código para asignaciones
    def visitAsignacion(self, ctx):
        var = ctx.ID().getText()
        val = self.visit(ctx.opal())

        t = self.newTemp()
        self.emit(f"{t} = {val}")
        self.emit(f"{var} = {t}")


    # Declaración con posibles múltiples variables
    def visitDeclaraciones(self, ctx):

        # Primera declaración
        self.visit(ctx.declaracion())

        # Declaraciones separadas por coma
        dp = ctx.declaracionp()
        while dp and dp.ID():
            var = dp.ID().getText()

            if dp.opal():
                op = dp.getChild(2).getText()
                rhs = self.visit(dp.opal())

                if op == "=":
                    self.emit(f"{var} = {rhs}")
                else:
                    t = self.newTemp()
                    if op == "+=":
                        self.emit(f"{t} = {var} + {rhs}")
                    else:
                        self.emit(f"{t} = {var} - {rhs}")
                    self.emit(f"{var} = {t}")

            dp = dp.declaracionp()


    # Declaración individual
    def visitDeclaracion(self, ctx):
        var = ctx.ID().getText()

        if ctx.opal():
            op = ctx.getChild(2).getText()
            rhs = self.visit(ctx.opal())

            if op == "=":
                self.emit(f"{var} = {rhs}")
            else:
                t = self.newTemp()
                if op == "+=":
                    self.emit(f"{t} = {var} + {rhs}")
                else:
                    self.emit(f"{t} = {var} - {rhs}")
                self.emit(f"{var} = {t}")


    # =========================
    # ESTRUCTURAS DE CONTROL
    # =========================

    # IF / IF-ELSE
    def visitIif(self, ctx):
        cond = self.visit(ctx.cond().opal())
        then = ctx.instruccion()

        elseLabel = self.newLabel()
        endLabel = self.newLabel()

        self.emit(f"ifntjmp {cond} , {elseLabel}")
        self.visit(then)

        if ctx.ielse():
            self.emit(f"jump {endLabel}")
            self.emit(f"label {elseLabel}")
            self.visit(ctx.ielse().instruccion())
            self.emit(f"label {endLabel}")
        else:
            self.emit(f"label {elseLabel}")


    # WHILE
    def visitIwhile(self, ctx):
        start = self.newLabel()
        end = self.newLabel()

        self.emit(f"label {start}")
        cond = self.visit(ctx.cond().opal())
        self.emit(f"ifntjmp {cond} , {end}")

        self.visit(ctx.instruccion())
        self.emit(f"jump {start}")
        self.emit(f"label {end}")


    # FOR
    def visitIfor(self, ctx):

        # INIT
        if ctx.init():
            self.visit(ctx.init())

        start = self.newLabel()
        end = self.newLabel()

        self.emit(f"label {start}")

        # COND
        if ctx.cond() and ctx.cond().opal():
            cond = self.visit(ctx.cond().opal())
            self.emit(f"ifntjmp {cond} , {end}")

        # BODY
        self.visit(ctx.instruccion())

        # ITER
        if ctx.iter_():
            self.visit(ctx.iter_())

        self.emit(f"jump {start}")
        self.emit(f"label {end}")


    # =========================
    # FUNCIONES
    # =========================

    # Llamada a función
    def visitUsofuncion(self, ctx):
        nombre = ctx.ID().getText()
        args = []

        # Recolecta recursivamente argumentos
        def recolectar_argumentos(arg_ctx):
            if arg_ctx is None:
                return
            if arg_ctx.opal():
                args.append(self.visit(arg_ctx.opal()))
            recolectar_argumentos(arg_ctx.argumentosp().argumentos() 
                                if arg_ctx.argumentosp() else None)

        recolectar_argumentos(ctx.argumentos())

        # Genera instrucciones param
        for a in args:
            self.emit(f"param {a}")

        # Genera llamada
        t = self.newTemp()
        self.emit(f"{t} = call {nombre}, {len(args)}")
        return t


    # RETURN
    def visitReturn(self, ctx):
        val = None
        if ctx.opal():
            val = self.visit(ctx.opal())

        self.emit(f"return {val}")
        return val


    # Generación de función (solo main)
    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()

        # Solo se genera código para main
        if nombre == "main":
            self.emit(f"label {nombre}")
            self.visit(ctx.bloque())


    # Bloque
    def visitBloque(self, ctx):
        self.visit(ctx.instrucciones())