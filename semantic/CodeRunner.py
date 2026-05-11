from semantic.ASTUtils import *
from functools import reduce
import os, subprocess, shutil
import re


class CodeRunner():
    def __init__(self):
        self.varsType = {}
        self.varsOption = {}
        self.writeCpp = []
        self.loopIdx = 0
        
    def visitProgram(self, ctx:Prog):
        for subtask in ctx.subtasks:
            subtask.accept(self)
    
    def visitSubtask(self, ctx:Subtask):
        self.writeCpp = []
        self.varsType = {}
        self.varsOption = {}
        self.loopIdx = 0
        config = ctx.config.accept(self)

        subTaskFolder = os.path.join("tests", ctx.name)

        if os.path.exists(subTaskFolder):
            shutil.rmtree(subTaskFolder)

        os.makedirs(subTaskFolder, exist_ok=True)

        solPath = config.sol[1:-1]
        solExePath = os.path.abspath(os.path.join(subTaskFolder, "sol.exe"))
        
        subprocess.run(["g++", solPath, "-o", solExePath], check=True)

        testSolExePath = None
        timeLimit = None
        if config.compare:
            if not config.testSol:
                raise ValueError(f"{ctx.name}: compare requires test_sol in config")
            testSolPath = config.testSol[1:-1]
            testSolExePath = os.path.abspath(os.path.join(subTaskFolder, "test_sol.exe"))
            subprocess.run(["g++", testSolPath, "-o", testSolExePath], check=True)
            if config.timeLimit:
                timeLimitMs = config.timeLimit.accept(self)
                timeLimit = timeLimitMs / 1000

        ctx.generate.accept(self)

        genCppPath = os.path.join(subTaskFolder, "gen.cpp")
        genExePath = os.path.abspath(os.path.join(subTaskFolder, "gen.exe"))
        cpp = [
            "#include <bits/stdc++.h>",
            "",
            "using namespace std;",
            "",
            "mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());",
            "",
            "long long ran(long long l, long long r) {",
            "    return l + (rng() % (r - l + 1));",
            "}",
            "",
            "string randString(long long len) {",
            "    string s;",
            "    for(long long i = 0; i < len; i++) s += char('a' + ran(0, 25));",
            "    return s;",
            "}",
            "",
            "signed main() {",
            *[f"    {line}" for line in self.writeCpp],
            "    return 0;",
            "}"
        ]      
        with open(genCppPath, "w") as f:
            f.write("\n".join(cpp))

        subprocess.run(["g++", genCppPath, "-o", genExePath], check=True)
        
        for i in range(config.tests):
            folder = os.path.join("tests", ctx.name, f"test{i+1}")
            os.makedirs(folder, exist_ok=True)

            inputPath = os.path.join(folder, config.input[1:-1])  
            outputPath = os.path.join(folder, config.output[1:-1])

            with open(inputPath, "w") as out:
                subprocess.run([genExePath], stdout=out, check=True)

            with open(inputPath, "r") as inp, open(outputPath, "w") as out:
                subprocess.run([solExePath], stdin=inp, stdout=out, check=True)

            if config.compare:
                testOutputPath = os.path.join(folder, "test_sol.out")
                try:
                    with open(inputPath, "r") as inp, open(testOutputPath, "w") as out:
                        subprocess.run(
                            [testSolExePath],
                            stdin=inp,
                            stdout=out,
                            check=True,
                            timeout=timeLimit
                        )
                    with open(outputPath, "r") as solOut, open(testOutputPath, "r") as testOut:
                        solTokens = solOut.read().split()
                        testTokens = testOut.read().split()

                    if solTokens == testTokens:
                        print(f"{ctx.name} test{i+1}: AC" )
                    else:
                        print(f"{ctx.name} test{i+1}: WA")

                except subprocess.TimeoutExpired:
                    print(f"{ctx.name} test{i+1}: TLE")
                    continue

        os.remove(genExePath)
        os.remove(solExePath)
        if testSolExePath:
            os.remove(testSolExePath)

    def visitConfig(self, ctx:Config):
        return ctx

    def visitGenerate(self, ctx:Generate):
        for stmt in ctx.stmts:
            stmt.accept(self)

    def visitLoopStmt(self, ctx:Loop):
        loopVar = f"loop{self.loopIdx}"
        self.loopIdx += 1
        cnt = ctx.cnt.accept(self)
        self.writeCpp.append(f"for(int {loopVar} = 0; {loopVar} < {cnt}; {loopVar}++) {{")
        for stmt in ctx.stmts:
            prev = len(self.writeCpp)
            stmt.accept(self)
            self.writeCpp[prev:] = [f"    {line}" for line in self.writeCpp[prev:]]
        self.writeCpp.append("}")
    
    def visitVar(self, ctx:Var):
        self.varsType[ctx.name] = ctx.varType
        self.varsOption[ctx.name] = ctx.options

        if isinstance(ctx.varType, PrimitiveType):
            low, high = self.getRange(ctx.options, "1", "20")
            if ctx.varType.name == "int":
                self.writeCpp.append(f"int {ctx.name} = ran({low}, {high});")
            elif ctx.varType.name == "ll":
                self.writeCpp.append(f"long long {ctx.name} = ran({low}, {high});")
            elif ctx.varType.name == "float":
                self.writeCpp.append(f"float {ctx.name} = (float)ran({low}, {high});")
            elif ctx.varType.name == "double":
                self.writeCpp.append(f"double {ctx.name} = (double)ran({low}, {high});")
            elif ctx.varType.name == "char":
                low, high = self.getRange(ctx.options, "97", "122")
                self.writeCpp.append(f"char {ctx.name} = char(ran({low}, {high}));")
            elif ctx.varType.name == "string":
                low, high = self.getRange(ctx.options, "1", "10")
                self.writeCpp.append(f"string {ctx.name} = randString(ran({low}, {high}));")
        elif isinstance(ctx.varType, ArrayType):
            dim = ctx.dims[0].accept(self)
            innerType = self.cppType(ctx.varType.inner)
            value = self.randomValue(ctx.varType.inner, ctx.options)
            self.writeCpp.append(f"vector<{innerType}> {ctx.name}({dim});")
            if "distinct" in ctx.options or "distince" in ctx.options:
                if isinstance(ctx.varType.inner, PrimitiveType) and ctx.varType.inner.name == "string":
                    usedName = f"used{ctx.name}"
                    self.writeCpp.append(f"set<string> {usedName};")
                    self.writeCpp.append(f"for(int i = 0; i < {dim}; i++) {{")
                    self.writeCpp.append(f"    do {{ {ctx.name}[i] = {value}; }} while({usedName}.count({ctx.name}[i]));")
                    self.writeCpp.append(f"    {usedName}.insert({ctx.name}[i]);")
                    self.writeCpp.append("}")
                else:
                    if isinstance(ctx.varType.inner, PrimitiveType) and ctx.varType.inner.name == "char":
                        low, high = self.getRange(ctx.options, "97", "122")
                    else:
                        low, high = self.getRange(ctx.options, "1", "100")
                    poolName = f"pool{ctx.name}"
                    self.writeCpp.append(f"vector<long long> {poolName};")
                    self.writeCpp.append(f"for(long long val = {low}; val <= {high}; val++) {poolName}.push_back(val);")
                    self.writeCpp.append(f"shuffle({poolName}.begin(), {poolName}.end(), rng);")
                    self.writeCpp.append(f"assert((long long){dim} <= (long long){poolName}.size());")
                    self.writeCpp.append(f"for(int i = 0; i < {dim}; i++) {ctx.name}[i] = {self.castValue(ctx.varType.inner, f'{poolName}[i]')};")
            else:
                self.writeCpp.append(f"for(int i = 0; i < {dim}; i++) {ctx.name}[i] = {value};")
            if "sorted" in ctx.options:
                self.writeCpp.append(f"sort({ctx.name}.begin(), {ctx.name}.end());")
        elif isinstance(ctx.varType, TreeType):
            size = ctx.varType.size.accept(self)
            self.writeCpp.append(f"vector<pair<long long, long long>> {ctx.name};")
            self.writeCpp.append(f"for(int i = 2; i <= {size}; i++) {ctx.name}.push_back({{ran(1, i-1), i}});")
        elif isinstance(ctx.varType, GraphType):
            nodes = ctx.varType.nodes.accept(self)
            edges = ctx.varType.edges.accept(self)
            weighted = "weighted" in ctx.options
            directed = "directed" in ctx.options
            simple = "simple" in ctx.options
            connected = "connected" in ctx.options
            adjName = f"adj{ctx.name}"
            adjSetName = f"adjSet{ctx.name}"
            edgesName = f"edges{ctx.name}"
            
            if weighted:
                self.writeCpp.append(f"vector<tuple<long long, long long, long long>> {adjName};")
            else:
                self.writeCpp.append(f"vector<pair<long long, long long>> {adjName};") 
            if simple:
                self.writeCpp.append(f"set<pair<long long, long long>> {adjSetName};") 
            self.writeCpp.append(f"long long {edgesName} = {edges};")
            
            if connected:
                self.writeCpp.append(f"for(int i = 2; i <= {nodes}; i++) {{")
                self.writeCpp.append(f"    long long u = ran(1, i-1), v = i;")
                if simple:
                    if not directed: self.writeCpp.append(f"    {adjSetName}.insert({{min(u, v), max(u, v)}});")
                    else: self.writeCpp.append(f"    {adjSetName}.insert({{u, v}});")
                if weighted: 
                    self.writeCpp.append(f"    {adjName}.push_back({{u, v, ran(1, 1000000)}});")
                else: self.writeCpp.append(f"    {adjName}.push_back({{u, v}});")
                self.writeCpp.append(f"    {edgesName}--;")
                self.writeCpp.append(f"}}")
                
            self.writeCpp.append(f"while({edgesName} > 0) {{")
            self.writeCpp.append(f"    long long u = ran(1, {nodes});")
            self.writeCpp.append(f"    long long v = ran(1, {nodes});")
            if simple:
                self.writeCpp.append(f"    if(u == v) continue;")
                if not directed:
                    self.writeCpp.append(f"    if({adjSetName}.count({{min(u, v), max(u, v)}})) continue;")
                    self.writeCpp.append(f"    {adjSetName}.insert({{min(u, v), max(u, v)}});")
                else:
                    self.writeCpp.append(f"    if({adjSetName}.count({{u, v}})) continue;")
                    self.writeCpp.append(f"    {adjSetName}.insert({{u, v}});")
            if weighted: self.writeCpp.append(f"    {adjName}.push_back({{u, v, ran(1, 1000000)}});")
            else: self.writeCpp.append(f"    {adjName}.push_back({{u, v}});")
            self.writeCpp.append(f"    {edgesName}--;")
            self.writeCpp.append(f"}}")

    def visitPrintStmt(self, ctx: Print):
        for expr in ctx.exprs:
            name = expr.accept(self)
            if name not in self.varsType:
                self.writeCpp.append(f'cout << {name} << "\\n";')
                continue
            
            type = self.varsType[name]
            if isinstance(type, ArrayType):
                self.writeCpp.append(f'for (int i = 0; i < {name}.size(); i++) {{cout << {name}[i] << (i == {name}.size() - 1 ? "" : " "); }}')
                self.writeCpp.append('cout << "\\n";')
            elif isinstance(type, TreeType):
                self.writeCpp.append(f'for (auto& e : {name}) {{ cout << e.first << " " << e.second << "\\n"; }}')
            elif isinstance(type, GraphType):
                adjName = f"adj{name}"
                self.writeCpp.append(f'for (auto& e : {adjName}) {{')
                if "weighted" in self.varsOption.get(name, []):
                    self.writeCpp.append(f'    cout << get<0>(e) << " " << get<1>(e) << " " << get<2>(e) << "\\n";') 
                else:
                    self.writeCpp.append(f'    cout << e.first << " " << e.second << "\\n";') 
                self.writeCpp.append(f'}}')
            else:
                self.writeCpp.append(f'cout << {name} << "\\n";')

    def visitId(self, ctx: Id):
        return ctx.name

    def visitInt(self, ctx: Int):
        return ctx.value

    def visitStr(self, ctx: Str):
        return ctx.value
        
    def visitBinaryOp(self, ctx:BinOp):
        left = ctx.left.accept(self)
        right = ctx.right.accept(self)
        return f"({left} {ctx.op} {right})"

    def getRange(self, options, lo, hi):
        for option in options:
            match = re.fullmatch(r"range\((.*),(.*)\)", option)
            if match:
                return match.group(1), match.group(2)
        return lo, hi

    def cppType(self, varType):
        if isinstance(varType, PrimitiveType):
            if varType.name == "ll":
                return "long long"
            return varType.name
        return "long long"

    def randomValue(self, varType, options):
        if not isinstance(varType, PrimitiveType):
            return "0"

        low, high = self.getRange(options, "1", "100")
        if varType.name == "int":
            return f"ran({low}, {high})"
        if varType.name == "ll":
            return f"ran({low}, {high})"
        if varType.name == "float":
            return f"(float)ran({low}, {high})"
        if varType.name == "double":
            return f"(double)ran({low}, {high})"
        if varType.name == "char":
            low, high = self.getRange(options, "97", "122")
            return f"char(ran({low}, {high}))"
        if varType.name == "string":
            low, high = self.getRange(options, "1", "10")
            return f"randString(ran({low}, {high}))"
        return "0"

    def castValue(self, varType, value):
        if isinstance(varType, PrimitiveType):
            if varType.name == "char":
                return f"char({value})"
            if varType.name == "float":
                return f"(float){value}"
            if varType.name == "double":
                return f"(double){value}"
        return value
