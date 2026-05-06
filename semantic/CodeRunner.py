from semantic.ASTUtils import *
from functools import reduce
import math, os, random, subprocess, shutil
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
        os.makedirs(subTaskFolder, exist_ok=True)

        solPath = config.sol[1:-1]
        solExePath = os.path.abspath(os.path.join(subTaskFolder, "sol.exe"))
        
        subprocess.run(["g++", solPath, "-o", solExePath], check=True)

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

        os.remove(genExePath)
        os.remove(solExePath)

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
            if ctx.varType.name == 'int':
                low, high = self.getRange(ctx.options, "1", "20")
                self.writeCpp.append(f"int {ctx.name} = ran({low}, {high});")
        elif isinstance(ctx.varType, ArrayType):
            dim = ctx.dims[0].accept(self)
            low, high = self.getRange(ctx.options, "1", "100")
            self.writeCpp.append(f"vector<long long> {ctx.name}({dim});")
            if "distinct" in ctx.options or "distince" in ctx.options:
                poolName = f"pool{ctx.name}"
                self.writeCpp.append(f"vector<long long> {poolName};")
                self.writeCpp.append(f"for(long long val = {low}; val <= {high}; val++) {poolName}.push_back(val);")
                self.writeCpp.append(f"shuffle({poolName}.begin(), {poolName}.end(), rng);")
                self.writeCpp.append(f"assert((long long){dim} <= (long long){poolName}.size());")
                self.writeCpp.append(f"for(int i = 0; i < {dim}; i++) {ctx.name}[i] = {poolName}[i];")
            else:
                self.writeCpp.append(f"for(int i = 0; i < {dim}; i++) {ctx.name}[i] = ran({low}, {high});")
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
