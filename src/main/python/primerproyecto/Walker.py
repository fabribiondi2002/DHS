import os
from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class Walker(compiladoresVisitor):
    def __init__(self):
            self.tempCount = 0
            self.labelCount = 0

            os.makedirs("output", exist_ok=True)
            self.out = open("output/CodigoIntermedio.txt", "w")
    
    def close(self):
        self.out.close()


    def newTemp(self):
        t = f"t{self.tempCount}"
        self.tempCount += 1
        return t

    def newLabel(self):
        l = f"l{self.labelCount}"
        self.labelCount += 1
        return l
    def emit(self, text):
        print(text)
        self.out.write(text + "\n")

    def visitPrograma(self, ctx):
        self.visit(ctx.instrucciones())
    
    def visitInstrucciones(self, ctx):
        if ctx is None:
            return
        if ctx.instruccion():
            self.visit(ctx.instruccion())
        if ctx.instrucciones() and ctx.instrucciones() != ctx:
            self.visit(ctx.instrucciones())

    
    def visitFactor(self, ctx):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()

        if ctx.ID() and ctx.getChildCount() == 1:
            return ctx.ID().getText()

        if ctx.ID() and ctx.getChildCount() == 2:
            var = ctx.ID().getText()
            op = ctx.getChild(1).getText()

            old = self.newTemp()
            self.emit(f"{old} = {var}")

            t = self.newTemp()
            if op == "++":
                self.emit(f"{t} = {var} + 1")
            else:
                self.emit(f"{t} = {var} - 1")

            self.emit(f"{var} = {t}")
            return old

        if ctx.usofuncion():
            return self.visit(ctx.usofuncion())

        return self.visit(ctx.exp())

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

    def visitComp(self, ctx):
        # Caso: solo exp
        if ctx.comparadores() is None:
            return self.visit(ctx.exp(0))

        # Caso: exp op exp
        left = self.visit(ctx.exp(0))
        right = self.visit(ctx.exp(1))
        op = ctx.comparadores().getText()

        t = self.newTemp()
        self.emit(f"{t} = {left} {op} {right}")
        return t


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

    def visitOpal(self, ctx):
        return self.visit(ctx.lor())

    def visitAsignacion(self, ctx):
        var = ctx.ID().getText()
        val = self.visit(ctx.opal())

        t = self.newTemp()
        self.emit(f"{t} = {val}")
        self.emit(f"{var} = {t}")

    def visitDeclaraciones(self, ctx):
        # primera declaración
        self.visit(ctx.declaracion())

        # declaraciones separadas por coma
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

    def visitIwhile(self, ctx):
        start = self.newLabel()
        end = self.newLabel()

        self.emit(f"label {start}")
        cond = self.visit(ctx.cond().opal())
        self.emit(f"ifntjmp {cond} , {end}")

        self.visit(ctx.instruccion())
        self.emit(f"jump {start}")
        self.emit(f"label {end}")

    def visitIfor(self, ctx):
        # ===== INIT =====
        if ctx.init():
            self.visit(ctx.init())

        start = self.newLabel()
        end = self.newLabel()

        # ===== START =====
        self.emit(f"label {start}")

        # ===== COND =====
        if ctx.cond() and ctx.cond().opal():
            cond = self.visit(ctx.cond().opal())
            self.emit(f"ifntjmp {cond} , {end}")

        # ===== BODY =====
        self.visit(ctx.instruccion())

        # ===== ITER =====
        if ctx.iter_():
            self.visit(ctx.iter_())

        # ===== LOOP =====
        self.emit(f"jump {start}")
        self.emit(f"label {end}")


    def visitIter(self, ctx):
        if ctx is None:
            return

        for a in ctx.asignacion():
            self.visit(a)

        for o in ctx.opal():
            self.visit(o)

    def visitUsofuncion(self, ctx):
        nombre = ctx.ID().getText()
        args = []

        def recolectar_argumentos(arg_ctx):
            if arg_ctx is None:
                return
            if arg_ctx.opal():
                args.append(self.visit(arg_ctx.opal()))
            recolectar_argumentos(arg_ctx.argumentosp().argumentos() 
                                if arg_ctx.argumentosp() else None)

        recolectar_argumentos(ctx.argumentos())

        for a in args:
            self.emit(f"param {a}")

        t = self.newTemp()
        self.emit(f"{t} = call {nombre}, {len(args)}")
        return t


    def visitReturn(self, ctx):
        val = None
        if ctx.opal():
            val = self.visit(ctx.opal())

        self.emit(f"return {val}")
        return val
    def visitFuncion(self, ctx):
        nombre = ctx.ID().getText()

        # Solo generar código para main
        if nombre == "main":
            self.emit(f"label {nombre}")
            self.visit(ctx.bloque())


    def visitBloque(self, ctx):
        self.visit(ctx.instrucciones())

