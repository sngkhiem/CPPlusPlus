'''
This file defines the Abstract Syntax Tree (AST) structure;
classes in this file represent nodes in the AST
'''

from abc import ABC, abstractmethod, ABCMeta # Abstract Base Classe (ABC)
from dataclasses import dataclass, field
from typing import List, Optional

def printlist(lst,f=str,start="[",sepa=",",end="]"):
	return start + sepa.join(f(i) for i in lst) + end

class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v):
        return v.visit(self)
        
class Expr(AST): pass
class Type(AST): pass
class Stmt(AST): pass
class check(AST): pass

@dataclass
class PrimitiveType(Type):
    name: str

    def __str__(self): 
        return f"PrimitiveType({self.name})"
    def accept(self, v):
        return v.visitPrimitiveType(self)

@dataclass 
class ArrayType(Type):
    inner: Type

    def __str__(self): 
        return f"ArrayType({str(self.inner)})"
    def accept(self, v): 
        return v.visitArrayType(self) 
    
@dataclass
class TreeType(Type):
    size: Expr

    def __str__(self):
        return f"TreeType({str(self.size)})"
    def accept(self, v):
        return v.visitTreeType(self)
    
@dataclass
class GraphType(Type):
    nodes: Expr
    edges: Expr

    def __str__(self):
        return f"GraphType({str(self.nodes), {str(self.edges)}})"
    def accept(self, v):
        return v.visitGraphType(self)
    
@dataclass
class Id(Expr):
    name: str
    def __str__(self): 
        return f"Id({self.name})"
    def accept(self, v): 
        return v.visitId(self)

@dataclass
class Int(Expr):
    value: int
    def __str__(self): 
        return f"Int({self.value})"
    def accept(self, v): 
        return v.visitIntLit(self)

@dataclass
class Str(Expr):
    value: str
    def __str__(self): 
        return f"Str({self.value})"
    def accept(self, v): 
        return v.visitStrLit(self)

@dataclass
class BinOp(Expr):
    op:str
    left:Expr
    right:Expr

    def __str__(self):
        return f"BinOp('{self.op}', {str(self.left)}, {str(self.right)})"

    def accept(self, v):
        return v.visitBinaryOp(self)
    
@dataclass
class Var(Stmt):
    varType: Type
    name: str
    dims: List[Expr] = field(default_factory=list) 
    options: List[str] = field(default_factory=list)

    def __str__(self):
        dimsStr = printlist(self.dims) if self.dims else "[]"
        optionsStr = printlist(self.options) if self.options else "[]"
        return f"Var({str(self.varType)}, {self.name}, dims={dimsStr}, options={optionsStr})"
    def accept(self, v): 
        return v.visitVar(self)
    
@dataclass
class Print(Stmt):
    exprs: List[Expr]
    def __str__(self): 
        return f"Print({printlist(self.exprs)})"
    def accept(self, v): 
        return v.visitPrintStmt(self)
    
@dataclass
class Loop(Stmt):
    cnt: Expr
    stmts: List[Stmt]
    def __str__(self): 
        return f"Loop({str(self.cnt)}, {printlist(self.stmts)})"
    def accept(self, v, param=None): 
        return v.visitLoopStmt(self)
    
@dataclass
class Assert(check):
    condition: Expr
    msg: Optional[str] 
    def __str__(self): 
        msg = f", msg={self.msg}" if self.msg else ""
        return f"Assert({str(self.condition)}{msg})"
    def accept(self, v): 
        return v.visitAssert(self)
    
@dataclass
class CheckRead(check):
    varType: Type
    name: str
    src: str 
    def __str__(self): 
        return f"CheckRead({str(self.varType)}, {self.name}, {self.src})"
    def accept(self, v): 
        return v.visitCheckRead(self)
    
@dataclass
class Config(AST):
    input: str
    output: str
    tests: int
    def __str__(self): 
        return f"Config(in={self.input}, out={self.output}, tests={self.tests})"
    def accept(self, v): 
        return v.visitConfig(self)
    
@dataclass
class Generate(AST):
    stmts: List[Stmt]
    def __str__(self): 
        return f"Generate({printlist(self.stmts)})"
    def accept(self, v): 
        return v.visitGenerate(self)

@dataclass
class Checker(AST):
    solution: Optional[str]
    stmts: List[check]
    def __str__(self): 
        return f"Checker(solution={self.solution}, {printlist(self.stmts)})"
    def accept(self, v): 
        return v.visitChecker(self)
    
@dataclass
class Subtask(AST):
    name: str
    config: Config
    generate: Generate
    checker: Optional[Checker] 
    def __str__(self): 
        checkerStr = str(self.checker) if self.checker else "None"
        return f"Subtask({self.name}, {str(self.config)}, {str(self.generate)}, {checkerStr})"
    def accept(self, v): 
        return v.visitSubtask(self)

@dataclass
class Prog(AST):
    subtasks: List[Subtask]
    def __str__(self): 
        return f"Prog({printlist(self.subtasks)})"
    def accept(self, v): 
        return v.visitProgram(self)
