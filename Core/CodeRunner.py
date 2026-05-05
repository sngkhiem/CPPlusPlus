from .ASTUtils import *
from functools import reduce
import math

class CodeRunner():
    def __init__(self, context=None):
        self.context = context
        self.variables = context.python_variables() if context else {}

    def visitProgram(self, ctx:Prog):
        return "\n".join([str(expr.accept(self)) for expr in ctx.expr])

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
        elif ctx.op == "concate":
            return str(left)+str(right)
        elif ctx.op == "log":
            return math.log(left, right)
        
    def visitSingleOp(self, ctx:SingleOp):
        input = ctx.input.accept(self)
        if ctx.op == 'sqrt':
            return math.sqrt(input)
        elif ctx.op == 'abs':
            return abs(input)

    def visitInteger(self, node:Int):
        return node.value
    
    def visitStr(self, node:Str):
        return node.value
