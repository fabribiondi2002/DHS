import sys
from antlr4 import *
from compiladoresLexer  import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
from CustonErrorListener import *
def main(argv):
    archivo = "input/programa.txt"
    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    # print(tree.toStringTree(recog=parser))
    # caminante = Walker()
    # caminante.visitPrograma(tree)

if __name__ == '__main__':
    main(sys.argv)