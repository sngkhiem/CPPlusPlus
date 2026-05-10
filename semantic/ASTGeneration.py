from CompiledFiles.CPPPVisitor import CPPPVisitor
from CompiledFiles.CPPPParser import CPPPParser
from semantic.ASTUtils import *

class ASTGeneration(CPPPVisitor):
    def visitProgram(self, ctx:CPPPParser.ProgramContext):
        subtasks = [subtask.accept(self) for subtask in ctx.subtaskBlock()]
        return Prog(subtasks)
    
    def visitSubtaskBlock(self, ctx:CPPPParser.SubtaskBlockContext):
        name = ctx.subtaskName().getText()
        config = ctx.configBlock().accept(self)
        gen = ctx.genBlock().accept(self)
        return Subtask(name, config, gen)
    
    def visitConfigBlock(self, ctx:CPPPParser.ConfigBlockContext):
        input = ""
        output = ""
        tests = 1
        sol = None
        testSol = None
        compare = False

        for item in ctx.configItem():
            if item.INPUT():
                input = item.STR().getText()
            elif item.OUTPUT():
                output = item.STR().getText()
            elif item.TESTS():
                tests = int(item.NUMBER().getText())
            elif item.SOL():
                sol = item.STR().getText()
            elif item.TEST_SOL():
                testSol = item.STR().getText()
            elif item.COMPARE():
                compare = True
        
        return Config(input, output, tests, sol, testSol, compare)
    
    def visitGenBlock(self, ctx:CPPPParser.GenBlockContext):
        stmts = [func.accept(self) for func in ctx.func()]
        return Generate(stmts)
    
    def visitDataType(self, ctx: CPPPParser.DataTypeContext):
        if ctx.primitiveType():
            return PrimitiveType(ctx.primitiveType().getText())
        elif ctx.ARRAY():
            inner = ctx.dataType().accept(self)
            return ArrayType(inner)
        elif ctx.TREE():
            size = ctx.expr(0).accept(self)
            return TreeType(size)
        elif ctx.GRAPH():
            nodes = ctx.expr(0).accept(self)
            edges = ctx.expr(1).accept(self)
            return GraphType(nodes, edges)
    
    def visitFunc(self, ctx: CPPPParser.FuncContext):
        return ctx.getChild(0).accept(self)

    def visitVar(self, ctx: CPPPParser.VarContext):
        varType = ctx.dataType().accept(self)
        name = ctx.ID().getText()
        dims = [expr.accept(self) for expr in ctx.expr()]
        options = [opt.getText() for opt in ctx.option()]
        return Var(varType, name, dims, options)
    
    def visitPrintStmt(self, ctx: CPPPParser.PrintStmtContext):
        exprs = [expr.accept(self) for expr in ctx.expr()]
        return Print(exprs)
    
    def visitLoopStmt(self, ctx: CPPPParser.LoopStmtContext):
        cnt = ctx.expr().accept(self)
        stmts = [func.accept(self) for func in ctx.func()]
        return Loop(cnt, stmts)
    
    def visitExpr(self, ctx: CPPPParser.ExprContext):
        if ctx.getChildCount() == 1:
            if ctx.NUMBER():
                return Int(int(ctx.NUMBER().getText()))
            elif ctx.STR():
                return Str(ctx.STR().getText())
            elif ctx.ID():
                return Id(ctx.ID().getText())

        elif ctx.getChildCount() == 2:
            if ctx.getChild(0).getText() == '-':
                return BinOp('-', Int(0), ctx.expr(0).accept(self))
                
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == '(':
                return ctx.expr(0).accept(self)
            else:
                op = ctx.getChild(1).getText()
                left = ctx.expr(0).accept(self)
                right = ctx.expr(1).accept(self)
                return BinOp(op, left, right)
    
