from antlr4.error.ErrorListener import ErrorListener

ERRORS_PATH = "output/errores.txt"

class CustomErrorListener(ErrorListener):

    def __init__(self):
        super().__init__()
        self.hayErrores = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hayErrores = True
        mensaje = f"ERROR [Sintactico] línea {line}:{column} - {msg}\n"
        print(mensaje)

        try:
            with open(ERRORS_PATH, "a", encoding="utf-8") as f:
                f.write(mensaje)
        except OSError:
            pass