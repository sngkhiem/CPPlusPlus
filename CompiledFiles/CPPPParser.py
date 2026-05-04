# Generated from ./grammar/CPPP.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\3\3\3\3\4\6")
        buf.write("\4(\n\4\r\4\16\4)\3\5\3\5\3\5\6\5/\n\5\r\5\16\5\60\3\5")
        buf.write("\3\5\3\6\3\6\3\6\6\68\n\6\r\6\16\69\3\6\3\6\3\7\3\7\3")
        buf.write("\7\6\7A\n\7\r\7\16\7B\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\tO\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nX\n\n")
        buf.write("\f\n\16\n[\13\n\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n")
        buf.write("\f\16\20\22\24\2\4\3\2\16\23\3\2\25\27\2^\2\27\3\2\2\2")
        buf.write("\4\35\3\2\2\2\6\'\3\2\2\2\b+\3\2\2\2\n\64\3\2\2\2\f=\3")
        buf.write("\2\2\2\16F\3\2\2\2\20N\3\2\2\2\22P\3\2\2\2\24^\3\2\2\2")
        buf.write("\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31\27\3\2\2")
        buf.write("\2\31\32\3\2\2\2\32\33\3\2\2\2\33\34\7\2\2\3\34\3\3\2")
        buf.write("\2\2\35\36\5\6\4\2\36\37\7\3\2\2\37 \5\b\5\2 \"\5\n\6")
        buf.write("\2!#\5\f\7\2\"!\3\2\2\2\"#\3\2\2\2#$\3\2\2\2$%\7\4\2\2")
        buf.write("%\5\3\2\2\2&(\7\26\2\2\'&\3\2\2\2()\3\2\2\2)\'\3\2\2\2")
        buf.write(")*\3\2\2\2*\7\3\2\2\2+,\7\5\2\2,.\7\3\2\2-/\7\26\2\2.")
        buf.write("-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\63\7\4\2\2\63\t\3\2\2\2\64\65\7\6\2\2\65\67")
        buf.write("\7\3\2\2\668\7\26\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2")
        buf.write("\2\29:\3\2\2\2:;\3\2\2\2;<\7\4\2\2<\13\3\2\2\2=>\7\7\2")
        buf.write("\2>@\7\3\2\2?A\7\26\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2")
        buf.write("BC\3\2\2\2CD\3\2\2\2DE\7\4\2\2E\r\3\2\2\2FG\t\2\2\2G\17")
        buf.write("\3\2\2\2HO\5\16\b\2IJ\7\24\2\2JK\7\b\2\2KL\5\20\t\2LM")
        buf.write("\7\t\2\2MO\3\2\2\2NH\3\2\2\2NI\3\2\2\2O\21\3\2\2\2PQ\7")
        buf.write("\n\2\2QR\5\20\t\2RY\7\26\2\2ST\7\13\2\2TU\5\24\13\2UV")
        buf.write("\7\f\2\2VX\3\2\2\2WS\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2")
        buf.write("\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\r\2\2]\23\3\2\2\2^_\t\3")
        buf.write("\2\2_\25\3\2\2\2\n\31\")\609BNY")
        return buf.getvalue()


class CPPPParser ( Parser ):

    grammarFileName = "CPPP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'config'", "'generate'", 
                     "'checker'", "'<'", "'>'", "'var'", "'['", "']'", "';'", 
                     "'int'", "'float'", "'double'", "'ll'", "'char'", "'string'", 
                     "'array'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "DOUBLE", "LL", "CHAR", "STRTYPE", 
                      "ARRAY", "NUMBER", "ID", "STR", "WS" ]

    RULE_program = 0
    RULE_subtaskBlock = 1
    RULE_subtaskName = 2
    RULE_configBlock = 3
    RULE_genBlock = 4
    RULE_checkerBlock = 5
    RULE_primitiveType = 6
    RULE_dataType = 7
    RULE_var = 8
    RULE_expr = 9

    ruleNames =  [ "program", "subtaskBlock", "subtaskName", "configBlock", 
                   "genBlock", "checkerBlock", "primitiveType", "dataType", 
                   "var", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    INT=12
    FLOAT=13
    DOUBLE=14
    LL=15
    CHAR=16
    STRTYPE=17
    ARRAY=18
    NUMBER=19
    ID=20
    STR=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CPPPParser.EOF, 0)

        def subtaskBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.SubtaskBlockContext)
            else:
                return self.getTypedRuleContext(CPPPParser.SubtaskBlockContext,i)


        def getRuleIndex(self):
            return CPPPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CPPPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.subtaskBlock()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 25
            self.match(CPPPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubtaskBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def subtaskName(self):
            return self.getTypedRuleContext(CPPPParser.SubtaskNameContext,0)


        def configBlock(self):
            return self.getTypedRuleContext(CPPPParser.ConfigBlockContext,0)


        def genBlock(self):
            return self.getTypedRuleContext(CPPPParser.GenBlockContext,0)


        def checkerBlock(self):
            return self.getTypedRuleContext(CPPPParser.CheckerBlockContext,0)


        def getRuleIndex(self):
            return CPPPParser.RULE_subtaskBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtaskBlock" ):
                return visitor.visitSubtaskBlock(self)
            else:
                return visitor.visitChildren(self)




    def subtaskBlock(self):

        localctx = CPPPParser.SubtaskBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_subtaskBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.subtaskName()
            self.state = 28
            self.match(CPPPParser.T__0)
            self.state = 29
            self.configBlock()
            self.state = 30
            self.genBlock()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPPPParser.T__4:
                self.state = 31
                self.checkerBlock()


            self.state = 34
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubtaskNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.ID)
            else:
                return self.getToken(CPPPParser.ID, i)

        def getRuleIndex(self):
            return CPPPParser.RULE_subtaskName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtaskName" ):
                return visitor.visitSubtaskName(self)
            else:
                return visitor.visitChildren(self)




    def subtaskName(self):

        localctx = CPPPParser.SubtaskNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_subtaskName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.match(CPPPParser.ID)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.ID)
            else:
                return self.getToken(CPPPParser.ID, i)

        def getRuleIndex(self):
            return CPPPParser.RULE_configBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigBlock" ):
                return visitor.visitConfigBlock(self)
            else:
                return visitor.visitChildren(self)




    def configBlock(self):

        localctx = CPPPParser.ConfigBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_configBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(CPPPParser.T__2)
            self.state = 42
            self.match(CPPPParser.T__0)
            self.state = 44 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 43
                self.match(CPPPParser.ID)
                self.state = 46 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 48
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GenBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.ID)
            else:
                return self.getToken(CPPPParser.ID, i)

        def getRuleIndex(self):
            return CPPPParser.RULE_genBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGenBlock" ):
                return visitor.visitGenBlock(self)
            else:
                return visitor.visitChildren(self)




    def genBlock(self):

        localctx = CPPPParser.GenBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_genBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(CPPPParser.T__3)
            self.state = 51
            self.match(CPPPParser.T__0)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.match(CPPPParser.ID)
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 57
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckerBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.ID)
            else:
                return self.getToken(CPPPParser.ID, i)

        def getRuleIndex(self):
            return CPPPParser.RULE_checkerBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckerBlock" ):
                return visitor.visitCheckerBlock(self)
            else:
                return visitor.visitChildren(self)




    def checkerBlock(self):

        localctx = CPPPParser.CheckerBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_checkerBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(CPPPParser.T__4)
            self.state = 60
            self.match(CPPPParser.T__0)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 61
                self.match(CPPPParser.ID)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 66
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CPPPParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CPPPParser.FLOAT, 0)

        def DOUBLE(self):
            return self.getToken(CPPPParser.DOUBLE, 0)

        def LL(self):
            return self.getToken(CPPPParser.LL, 0)

        def CHAR(self):
            return self.getToken(CPPPParser.CHAR, 0)

        def STRTYPE(self):
            return self.getToken(CPPPParser.STRTYPE, 0)

        def getRuleIndex(self):
            return CPPPParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = CPPPParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.INT) | (1 << CPPPParser.FLOAT) | (1 << CPPPParser.DOUBLE) | (1 << CPPPParser.LL) | (1 << CPPPParser.CHAR) | (1 << CPPPParser.STRTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(CPPPParser.PrimitiveTypeContext,0)


        def ARRAY(self):
            return self.getToken(CPPPParser.ARRAY, 0)

        def dataType(self):
            return self.getTypedRuleContext(CPPPParser.DataTypeContext,0)


        def getRuleIndex(self):
            return CPPPParser.RULE_dataType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = CPPPParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dataType)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INT, CPPPParser.FLOAT, CPPPParser.DOUBLE, CPPPParser.LL, CPPPParser.CHAR, CPPPParser.STRTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.primitiveType()
                pass
            elif token in [CPPPParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(CPPPParser.ARRAY)
                self.state = 72
                self.match(CPPPParser.T__5)
                self.state = 73
                self.dataType()
                self.state = 74
                self.match(CPPPParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(CPPPParser.DataTypeContext,0)


        def ID(self):
            return self.getToken(CPPPParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ExprContext,i)


        def getRuleIndex(self):
            return CPPPParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = CPPPParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(CPPPParser.T__7)
            self.state = 79
            self.dataType()
            self.state = 80
            self.match(CPPPParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.T__8:
                self.state = 81
                self.match(CPPPParser.T__8)
                self.state = 82
                self.expr()
                self.state = 83
                self.match(CPPPParser.T__9)
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(CPPPParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CPPPParser.ID, 0)

        def NUMBER(self):
            return self.getToken(CPPPParser.NUMBER, 0)

        def STR(self):
            return self.getToken(CPPPParser.STR, 0)

        def getRuleIndex(self):
            return CPPPParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CPPPParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.NUMBER) | (1 << CPPPParser.ID) | (1 << CPPPParser.STR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





