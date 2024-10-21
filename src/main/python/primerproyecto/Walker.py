from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

class Walker (compiladoresVisitor):
    def visitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("=-"*20)
        print("--> Comienza a caminar")
        tmp = super().visitPrograma(ctx)
        print("Fin del programa")
        return tmp
    
    def visitBloque(self, ctx: compiladoresParser.BloqueContext):
        print("Nuevo Contexto")
        # print(ctx.getText())
        return super().visitBloque(ctx)
        # return super().visitInstrucciones(ctx.getChild(1))
    def visitDeclaracion(self, ctx: compiladoresParser.DeclaracionContext):
        print(ctx.getChild(0).getText() + " - " + ctx.getChild(1).getText())
        return super().visitDeclaracion(ctx)
    # def visitTerminal(self, node):
    #     print("--> Token" + node.getText())
    #     return super().visitTerminal(node)