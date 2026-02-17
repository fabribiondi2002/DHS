import re

# ===============================
# IR INSTRUCTIONS
# ===============================

class Instr:
    pass

class Assign(Instr):
    def __init__(self, dest, value):
        self.dest = dest
        self.value = value

class BinOp(Instr):
    def __init__(self, dest, left, op, right):
        self.dest = dest
        self.left = left
        self.op = op
        self.right = right

class Label(Instr):
    def __init__(self, name):
        self.name = name

class Jump(Instr):
    def __init__(self, label):
        self.label = label

class CondJump(Instr):
    def __init__(self, cond, label):
        self.cond = cond
        self.label = label

class Param(Instr):
    def __init__(self, value):
        self.value = value

class Call(Instr):
    def __init__(self, dest, name, argc):
        self.dest = dest
        self.name = name
        self.argc = argc

class Return(Instr):
    def __init__(self, value):
        self.value = value


# ===============================
# PARSER TAC → IR
# ===============================

def is_number(x):
    return re.fullmatch(r"-?\d+", x) is not None

def parse_line(line):
    line = line.strip()

    if line.startswith("label"):
        return Label(line.split()[1])

    if line.startswith("jump"):
        return Jump(line.split()[1])

    if line.startswith("ifntjmp"):
        _, cond, _, label = line.split()
        return CondJump(cond, label)

    if line.startswith("param"):
        return Param(line.split()[1])

    if line.startswith("return"):
        parts = line.split()
        return Return(parts[1] if len(parts) > 1 else None)

    if "call" in line:
        dest, rest = line.split("=")
        rest = rest.strip()
        _, name, argc = rest.split()
        return Call(dest.strip(), name.strip(","), int(argc))

    if "=" in line:

        dest, expr = line.split("=", 1)

        dest = dest.strip()
        tokens = expr.strip().split()

        if len(tokens) == 1:
            return Assign(dest, tokens[0])

        if len(tokens) == 3:
            return BinOp(dest, tokens[0], tokens[1], tokens[2])

    return None


# ===============================
# OPTIMIZER
# ===============================

class Optimizador:

    def __init__(self,
                 input_file="output/CodigoIntermedio.txt",
                 output_file="output/CodigoOptimizado.txt"):
        self.input_file = input_file
        self.output_file = output_file
        self.code = []

    # -------- Load IR --------

    def load(self):
        with open(self.input_file) as f:
            for line in f:
                instr = parse_line(line)
                if instr:
                    self.code.append(instr)

    # -------- Constant Propagation --------

    def constant_propagation(self):

        env = {}
        new_code = []

        def flush_env():
            env.clear()

        for instr in self.code:

            if isinstance(instr, (Label, Jump, Call, Return)):
                flush_env()

            if isinstance(instr, Assign):

                if instr.value in env:
                    instr.value = env[instr.value]

                if is_number(instr.value):
                    env[instr.dest] = instr.value
                else:
                    env.pop(instr.dest, None)


            elif isinstance(instr, BinOp):

                left = env.get(instr.left, instr.left)
                right = env.get(instr.right, instr.right)

                if is_number(left) and is_number(right):

                    result = str(int(eval(f"{left}{instr.op}{right}")))
                    instr = Assign(instr.dest, result)
                    env[instr.dest] = result

                else:
                    instr.left = left
                    instr.right = right
                    env.pop(instr.dest, None)

            elif isinstance(instr, CondJump):

                if instr.cond in env:
                    instr.cond = env[instr.cond]
            
            new_code.append(instr)

        self.code = new_code


    # -------- Dead Code Elimination --------

    def dead_code(self):

        changed = True

        while changed:

            changed = False
            used = set()

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

            for instr in self.code:

                if isinstance(instr, (Assign, BinOp)):
                    if instr.dest.startswith("t") and instr.dest not in used:
                        changed = True
                        continue

                new_code.append(instr)

            self.code = new_code


    def simplify_jumps(self):

        new_code = []
        i = 0

        while i < len(self.code):

            instr = self.code[i]

            if isinstance(instr, CondJump):

                if is_number(instr.cond):

                    if instr.cond == "0":
                        # siempre salta → jump incondicional
                        new_code.append(Jump(instr.label))

                    # si es 1 → nunca salta → eliminar

                    i += 1
                    continue

            new_code.append(instr)
            i += 1

        self.code = new_code

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


    def remove_redundant_jumps(self):

        new_code = []

        for i in range(len(self.code)):

            instr = self.code[i]

            if isinstance(instr, Jump):

                if i + 1 < len(self.code):
                    next_instr = self.code[i + 1]

                    if isinstance(next_instr, Label) and next_instr.name == instr.label:
                        continue  # eliminar jump redundante

            new_code.append(instr)

        self.code = new_code

    def dead_store_elimination(self):
        live = set()
        new_code = []

        # recorrer hacia atrás
        for instr in reversed(self.code):

            if isinstance(instr, Assign):

                # si la variable ya no es live y nunca se usa, eliminar
                if instr.dest not in live:
                    continue

                # actualizar live
                live.discard(instr.dest)
                if not is_number(instr.value):
                    live.add(instr.value)

            elif isinstance(instr, BinOp):

                if instr.dest not in live:
                    continue

                live.discard(instr.dest)
                live.add(instr.left)
                live.add(instr.right)

            elif isinstance(instr, CondJump):
                live.add(instr.cond)

            elif isinstance(instr, Param):
                live.add(instr.value)

            elif isinstance(instr, Return) and instr.value:
                live.add(instr.value)

            elif isinstance(instr, Label):
                # los labels no afectan liveness
                pass

            new_code.append(instr)

        # invertir para recuperar orden original
        self.code = list(reversed(new_code))

    # -------- Save IR → TAC --------

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

    # -------- Pipeline --------

    def optimizar(self):

        self.load()

        for _ in range(3):  # iterar optimizaciones
            self.constant_propagation()
            self.simplify_jumps()
            self.dead_code()
            self.dead_store_elimination()
            self.remove_unreachable()
            self.remove_redundant_jumps()

        self.save()

