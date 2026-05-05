from semantic.ASTUtils import *
from functools import reduce
import math, os, random, subprocess


class CodeRunner():
    def __init__(self):
        self.vars = {}
        self.writeInput = []
        self.writeOutput = []

    def visitProgram(self, ctx:Prog):
        for subtask in ctx.subtasks:
            subtask.accept(self)
    
    def visitSubtask(self, ctx:Subtask):
        config = ctx.config.accept(self)

        solPath = config.sol[1:-1]
        exePath = os.path.abspath(os.path.join(ctx.name, "sol.exe"))
        print(exePath)
        os.makedirs(ctx.name, exist_ok=True)
        subprocess.run(["g++", solPath, "-o", exePath], check=True)
        
        for i in range(config.tests):
            self.vars = {}
            self.writeInput = []
            self.writeOutput = []
            folder = os.path.join(ctx.name, f"test{i+1}")
            os.makedirs(folder, exist_ok=True)
            
            ctx.generate.accept(self)

            inputPath = os.path.join(folder, config.input[1:-1])  
            with open(inputPath, "w") as f:
                f.write("\n".join(self.writeInput))
            
            outputPath = os.path.join(folder, config.output[1:-1])
            with open(inputPath, "r") as inp, open(outputPath, "w") as out:
                subprocess.run([exePath], stdin=inp, stdout=out, check=True)

    def visitConfig(self, ctx:Config):
        return ctx

    def visitGenerate(self, ctx:Generate):
        for stmt in ctx.stmts:
            stmt.accept(self)
    
    def visitVar(self, ctx:Var):
        if isinstance(ctx.varType, PrimitiveType):
            if ctx.varType.name == 'int':
              self.vars[ctx.name] = random.randint(0, 20)
        elif isinstance(ctx.varType, ArrayType):
            dim = ctx.dims[0].accept(self)
            self.vars[ctx.name] = [random.randint(0, 20) for _ in range(dim)]


    def visitPrintStmt(self, ctx: Print):
        for expr in ctx.exprs:
            value = expr.accept(self)

            if isinstance(value, list):
                self.writeInput.append(" ".join(map(str, value)))
            else:
                self.writeInput.append(str(value))

    def visitId(self, ctx: Id):
        return self.vars[ctx.name]

    def visitIntLit(self, ctx: Int):
        return ctx.value
        
    def visitBinaryOp(self, ctx:BinOp):
        left = ctx.left.accept(self)
        right = ctx.right.accept(self)
        if ctx.op == "+":
            return left + right
        elif ctx.op == "-":
            return left - right
        elif ctx.op == "*":
            return left * right
        elif ctx.op == "/":
            return left / right
        elif ctx.op == "pow":
            return math.pow(left, right)
        elif ctx.op ==  "log":
            return math.log(left, right)
        elif ctx.op == "sqrt":
            return math.sqrt(left)