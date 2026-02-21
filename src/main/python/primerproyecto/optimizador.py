import re

# ===============================
# IR INSTRUCTIONS (Representación Intermedia)
# ===============================
# Estas clases representan las distintas instrucciones
# del código intermedio en forma estructurada (IR).
# Cada clase modela un tipo de instrucción TAC.

class Instr:
    # Clase base para todas las instrucciones
    pass


# Asignación simple:  a = b
class Assign(Instr):
    def __init__(self, dest, value):
        self.dest = dest      # variable destino
        self.value = value    # valor asignado


# Operación binaria: t1 = a + b
class BinOp(Instr):
    def __init__(self, dest, left, op, right):
        self.dest = dest      # destino
        self.left = left      # operando izquierdo
        self.op = op          # operador (+,-,*,/,&&, etc)
        self.right = right    # operando derecho


# Etiqueta: label L1
class Label(Instr):
    def __init__(self, name):
        self.name = name


# Salto incondicional: jump L1
class Jump(Instr):
    def __init__(self, label):
        self.label = label


# Salto condicional: ifntjmp t1 , L1
class CondJump(Instr):
    def __init__(self, cond, label):
        self.cond = cond
        self.label = label


# Parámetro de función: param x
class Param(Instr):
    def __init__(self, value):
        self.value = value


# Llamada a función: t1 = call foo, 2
class Call(Instr):
    def __init__(self, dest, name, argc):
        self.dest = dest
        self.name = name
        self.argc = argc


# Retorno de función: return x
class Return(Instr):
    def __init__(self, value):
        self.value = value


# ===============================
# PARSER TAC → IR
# ===============================
# Convierte el archivo de texto (TAC)
# en objetos IR manipulables.

def is_number(x):
    return re.fullmatch(r"-?\d+", x) is not None


def parse_line(line):

    line = line.strip()

    # ---------- LABEL ----------
    if line.startswith("label"):
        return Label(line.split()[1])

    # ---------- JUMP ----------
    if line.startswith("jump"):
        return Jump(line.split()[1])

    # ---------- COND JUMP ----------
    if line.startswith("ifntjmp"):
        _, cond, _, label = line.split()
        return CondJump(cond, label)

    # ---------- PARAM ----------
    if line.startswith("param"):
        return Param(line.split()[1])

    # ---------- RETURN ----------
    if line.startswith("return"):
        parts = line.split()
        return Return(parts[1] if len(parts) > 1 else None)

    # ---------- CALL ----------
    if "call" in line:
        dest, rest = line.split("=")
        rest = rest.strip()
        _, name, argc = rest.split()
        return Call(dest.strip(), name.strip(","), int(argc))

    # ---------- ASSIGN / BINOP ----------
    if "=" in line:

        dest, expr = line.split("=", 1)
        dest = dest.strip()
        tokens = expr.strip().split()

        # asignación simple
        if len(tokens) == 1:
            return Assign(dest, tokens[0])

        # operación binaria
        if len(tokens) == 3:
            return BinOp(dest, tokens[0], tokens[1], tokens[2])

    return None


# ===============================
# OPTIMIZADOR
# ===============================

class Optimizador:

    # Constructor
    def __init__(self,
                 input_file="output/CodigoIntermedio.txt",
                 output_file="output/CodigoOptimizado.txt"):

        self.input_file = input_file
        self.output_file = output_file
        self.code = []   # lista de instrucciones IR


    # ===============================
    # CARGA DEL IR
    # ===============================

    def load(self):
        # Lee el archivo TAC y lo convierte en IR
        with open(self.input_file) as f:
            for line in f:
                instr = parse_line(line)
                if instr:
                    self.code.append(instr)


    # ===============================
    # CONSTANT PROPAGATION + FOLDING
    # ===============================
    # Propaga constantes conocidas a lo largo del código y evalúa operaciones con operandos constantes (constant folding). También simplifica saltos condicionales con condiciones constantes.
    def constant_propagation(self):

        # Entorno que guarda constantes conocidas
        env = {}
        new_code = []

        # Limpia el entorno (cuando se rompe flujo)
        def flush_env():
            env.clear()

        # Detecta número entero o decimal
        def is_number_local(x):
            return re.fullmatch(r"-?\d+(\.\d+)?", x) is not None

        # Evalúa operación binaria
        def eval_binop(left, op, right):

            # Operadores lógicos
            if op == "&&":
                return "1" if eval(f"{left} and {right}") else "0"

            if op == "||":
                return "1" if eval(f"{left} or {right}") else "0"

            # Comparadores
            if op in ("<", ">", "<=", ">=", "==", "!="):
                return "1" if eval(f"{left}{op}{right}") else "0"

            # Aritméticos
            try:
                val = eval(f"{left}{op}{right}")
                if isinstance(val, bool):
                    return "1" if val else "0"
                if float(val).is_integer():
                    return str(int(val))
                return str(val)
            except:
                return None

        # Recorre instrucciones
        for instr in self.code:

            # Instrucciones que rompen flujo
            if isinstance(instr, (Label, Jump, Call, Return)):
                flush_env()

            # -------- ASSIGN --------
            if isinstance(instr, Assign):

                # Propagar constante conocida
                if instr.value in env:
                    instr.value = env[instr.value]

                # Guardar en entorno si es constante
                if is_number_local(instr.value):
                    env[instr.dest] = instr.value
                else:
                    env.pop(instr.dest, None)

            # -------- BINOP --------
            elif isinstance(instr, BinOp):

                left = env.get(instr.left, instr.left)
                right = env.get(instr.right, instr.right)

                # Intentar constant folding
                if is_number_local(left) and is_number_local(right):

                    result = eval_binop(left, instr.op, right)

                    if result is not None:
                        instr = Assign(instr.dest, result)
                        env[instr.dest] = result
                    else:
                        instr.left = left
                        instr.right = right
                        env.pop(instr.dest, None)

                else:
                    instr.left = left
                    instr.right = right
                    env.pop(instr.dest, None)

            # -------- COND JUMP --------
            elif isinstance(instr, CondJump):

                if instr.cond in env:
                    instr.cond = env[instr.cond]

            new_code.append(instr)

        self.code = new_code


    # ===============================
    # DEAD CODE ELIMINATION (temporales)
    # ===============================
    # Elimina asignaciones a temporales que no se usan posteriormente.

    def dead_code(self):

        changed = True

        while changed:

            changed = False
            used = set()

            # Detectar variables usadas
            for instr in self.code:

                if isinstance(instr, BinOp):
                    used.add(instr.left)
                    used.add(instr.right)

                if isinstance(instr, Assign):
                    used.add(instr.value)

                if isinstance(instr, CondJump):
                    used.add(instr.cond)

                if isinstance(instr, Param):
                    used.add(instr.value)

                if isinstance(instr, Return) and instr.value:
                    used.add(instr.value)

            new_code = []

            # Eliminar temporales no usados
            for instr in self.code:

                if isinstance(instr, (Assign, BinOp)):
                    if instr.dest.startswith("t") and instr.dest not in used:
                        changed = True
                        continue

                new_code.append(instr)

            self.code = new_code


    # ===============================
    # SIMPLIFICACIÓN DE SALTOS
    # ===============================
    # Convierte saltos condicionales con condiciones constantes en saltos incondicionales o los elimina si la condición es siempre verdadera.

    def simplify_jumps(self):

        new_code = []
        i = 0

        while i < len(self.code):

            instr = self.code[i]

            if isinstance(instr, CondJump):

                if is_number(instr.cond):

                    if instr.cond == "0":
                        new_code.append(Jump(instr.label))

                    # si es 1 → eliminar

                    i += 1
                    continue

            new_code.append(instr)
            i += 1

        self.code = new_code


    # ===============================
    # ELIMINAR CÓDIGO INALCANZABLE
    # ===============================
    # Elimina instrucciones que no pueden ser alcanzadas debido a saltos incondicionales JUMP o retornos anteriores RETURN.

    def remove_unreachable(self):

        new_code = []
        reachable = True

        for instr in self.code:

            if not reachable:

                if isinstance(instr, Label):
                    reachable = True
                else:
                    continue

            new_code.append(instr)

            if isinstance(instr, Jump) or isinstance(instr, Return):
                reachable = False

        self.code = new_code


    # ===============================
    # ELIMINAR JUMPS REDUNDANTES
    # ===============================
    # Elimina saltos incondicionales que van directamente a una etiqueta que sigue inmediatamente después.
    def remove_redundant_jumps(self):

        new_code = []

        for i in range(len(self.code)):

            instr = self.code[i]

            if isinstance(instr, Jump):

                if i + 1 < len(self.code):
                    next_instr = self.code[i + 1]

                    if isinstance(next_instr, Label) and next_instr.name == instr.label:
                        continue

            new_code.append(instr)

        self.code = new_code


    # ===============================
    # DEAD STORE ELIMINATION
    # ===============================
    # Elimina asignaciones a variables (especialmente temporales) que no se usan posteriormente en el código. Esto es similar a la eliminación de código muerto, pero se enfoca específicamente en las asignaciones que no tienen efecto observable.

    def dead_store_elimination(self):

        live = set()
        new_code = []

        # recorrido hacia atrás
        for instr in reversed(self.code):

            if isinstance(instr, Assign):

                if instr.dest.startswith("t") and instr.dest not in live:
                    continue

                if instr.dest in live:
                    live.discard(instr.dest)

                if not is_number(instr.value):
                    live.add(instr.value)

            elif isinstance(instr, BinOp):

                if instr.dest.startswith("t") and instr.dest not in live:
                    continue

                if instr.dest in live:
                    live.discard(instr.dest)

                live.add(instr.left)
                live.add(instr.right)

            elif isinstance(instr, CondJump):
                if not is_number(instr.cond):
                    live.add(instr.cond)

            elif isinstance(instr, Param):
                live.add(instr.value)

            elif isinstance(instr, Return) and instr.value:
                live.add(instr.value)

            new_code.append(instr)

        self.code = list(reversed(new_code))


    # ===============================
    # ELIMINAR LABELS MUERTOS
    # ===============================
    # Elimina etiquetas que no son el destino de ningún salto (JUMP o COND JUMP) y que no son el punto de entrada del programa. 
    def remove_unused_labels(self):

        used = set()

        for instr in self.code:
            if isinstance(instr, Jump):
                used.add(instr.label)
            elif isinstance(instr, CondJump):
                used.add(instr.label)

        new_code = []
        for instr in self.code:
            if isinstance(instr, Label) and instr.name not in used:
                continue
            new_code.append(instr)

        self.code = new_code


    # ===============================
    # GUARDAR IR → TAC
    # ===============================

    def save(self):

        def emit(instr):

            if isinstance(instr, Label):
                return f"label {instr.name}"

            if isinstance(instr, Jump):
                return f"jump {instr.label}"

            if isinstance(instr, CondJump):
                return f"ifntjmp {instr.cond} , {instr.label}"

            if isinstance(instr, Assign):
                return f"{instr.dest} = {instr.value}"

            if isinstance(instr, BinOp):
                return f"{instr.dest} = {instr.left} {instr.op} {instr.right}"

            if isinstance(instr, Param):
                return f"param {instr.value}"

            if isinstance(instr, Call):
                return f"{instr.dest} = call {instr.name}, {instr.argc}"

            if isinstance(instr, Return):
                return f"return {instr.value}"

        with open(self.output_file, "w") as f:
            for instr in self.code:
                f.write(emit(instr) + "\n")


    # ===============================
    # PIPELINE COMPLETO
    # ===============================

    def optimizar(self):

        # Cargar IR
        self.load()

        # Iterar varias veces para estabilizar optimizaciones
        for _ in range(3):
            self.constant_propagation()
            self.simplify_jumps()
            self.dead_code()
            self.dead_store_elimination()
            self.remove_unreachable()
            self.remove_redundant_jumps()
            self.remove_unused_labels()

        # Guardar resultado final
        self.save()