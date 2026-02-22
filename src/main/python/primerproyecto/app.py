import sys
from antlr4 import *
from antlr4.error.ErrorStrategy import BailErrorStrategy

from compiladoresLexer import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
from CustonErrorListener import *
from optimizador import Optimizador


def main(argv):
    archivo = "input/entrada.txt"
    if len(argv) > 1:
        archivo = argv[1]

    input_stream = FileStream(archivo)

    # 🔥 INSTANCIA UNICA DEL LISTENER
    error_listener = CustomErrorListener()

    lexer = compiladoresLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)

    parser = compiladoresParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    parser._errHandler = BailErrorStrategy()

    escucha = Escucha()
    parser.addParseListener(escucha)

    try:
        tree = parser.programa()
    except Exception:
        print("Se encontraron errores sintácticos. Compilación detenida.")
        return

    if error_listener.hayErrores or escucha.errores_semanticos:
        print("Se encontraron errores. No se generará código intermedio.")
        return

    caminante = Walker()
    caminante.visitPrograma(tree)
    caminante.close()

    opt = Optimizador()
    opt.optimizar()


if __name__ == '__main__':
    main(sys.argv)