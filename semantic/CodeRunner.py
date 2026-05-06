from semantic.ASTUtils import *
from functools import reduce
import math, os, random, subprocess, shutil


class CodeRunner():
    def __init__(self):
        self.varsType = {}
        self.writeCpp = []

    def visitProgram(self, ctx:Prog):
        for subtask in ctx.subtasks:
            subtask.accept(self)
    
    def visitSubtask(self, ctx:Subtask):
        self.writeCpp = []
        config = ctx.config.accept(self)

        subTaskFolder = os.path.join("tests", ctx.name)
        os.makedirs(subTaskFolder, exist_ok=True)

        solPath = config.sol[1:-1]
        solExePath = os.path.abspath(os.path.join(subTaskFolder, "sol.exe"))
        
        subprocess.run(["g++", solPath, "-o", solExePath], check=True)

        ctx.generate.accept(self)

        genCppPath = os.path.join(subTaskFolder, "gen.cpp")
        genExePath = os.path.abspath(os.path.join(subTaskFolder, "gen.exe"))
        cpp = [
            "#include <bits/stdc++.h>",
            "using namespace std;",
            "mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());",
            "long long ran(long long l, long long r) {return l + (rng() % (r - l + 1));}",
            "int main() {",
            *self.writeCpp,
            "return 0;",
            "}",
        ]        
        with open(genCppPath, "w") as f:
            f.write("\n".join(cpp))
        
        for i in range(config.tests):
            folder = os.path.join("tests", ctx.name, f"test{i+1}")
            os.makedirs(folder, exist_ok=True)

            inputPath = os.path.join(folder, config.input[1:-1])  
            outputPath = os.path.join(folder, config.output[1:-1])

            subprocess.run(["g++", genCppPath, "-o", genExePath], check=True)

            with open(inputPath, "w") as out:
                subprocess.run([genExePath], stdout=out, check=True)

            with open(inputPath, "r") as inp, open(outputPath, "w") as out:
                subprocess.run([solExePath], stdin=inp, stdout=out, check=True)

        os.remove(genExePath)
        os.remove(solExePath)

    def visitConfig(self, ctx:Config):
        return ctx

    def visitGenerate(self, ctx:Generate):
        for stmt in ctx.stmts:
            stmt.accept(self)
    
    def visitVar(self, ctx:Var):
        self.varsType[ctx.name] = ctx.varType
        if isinstance(ctx.varType, PrimitiveType):
            if ctx.varType.name == 'int':
                self.writeCpp.append(f"int {ctx.name} = ran(1, 20);")

        elif isinstance(ctx.varType, ArrayType):
            dim = ctx.dims[0].accept(self)
            self.writeCpp.append(f"vector<int> {ctx.name};")
            self.writeCpp.append(f"for(int i = 0; i < {dim}; i++) {ctx.name}.push_back(ran(1, 20));")


    def visitPrintStmt(self, ctx: Print):
        for expr in ctx.exprs:
            name = expr.accept(self)
            type = self.varsType[name]

            if isinstance(type, ArrayType):
                self.writeCpp.append(
                    f'for (int i = 0; i < {expr.name}.size(); i++) '
                    f'{{cout << {expr.name}[i] << " "; }}'
                )
                self.writeCpp.append('cout << endl;')
            else:
                self.writeCpp.append(f'cout << {expr.name} << endl;')


    def visitId(self, ctx: Id):
        return ctx.name

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
