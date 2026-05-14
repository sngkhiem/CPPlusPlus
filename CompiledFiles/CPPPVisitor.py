# Generated from ./grammar/CPPP.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CPPPParser import CPPPParser
else:
    from CPPPParser import CPPPParser

# This class defines a complete generic visitor for a parse tree produced by CPPPParser.

class CPPPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CPPPParser#program.
    def visitProgram(self, ctx:CPPPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#subtaskBlock.
    def visitSubtaskBlock(self, ctx:CPPPParser.SubtaskBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#subtaskName.
    def visitSubtaskName(self, ctx:CPPPParser.SubtaskNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#configBlock.
    def visitConfigBlock(self, ctx:CPPPParser.ConfigBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#configItem.
    def visitConfigItem(self, ctx:CPPPParser.ConfigItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#genBlock.
    def visitGenBlock(self, ctx:CPPPParser.GenBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#primitiveType.
    def visitPrimitiveType(self, ctx:CPPPParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#dataType.
    def visitDataType(self, ctx:CPPPParser.DataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#func.
    def visitFunc(self, ctx:CPPPParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#var.
    def visitVar(self, ctx:CPPPParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#printStmt.
    def visitPrintStmt(self, ctx:CPPPParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#loopStmt.
    def visitLoopStmt(self, ctx:CPPPParser.LoopStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#compare.
    def visitCompare(self, ctx:CPPPParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#option.
    def visitOption(self, ctx:CPPPParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CPPPParser#expr.
    def visitExpr(self, ctx:CPPPParser.ExprContext):
        return self.visitChildren(ctx)



del CPPPParser