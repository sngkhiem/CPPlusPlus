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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3!")
        buf.write("\u008c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\6\2\36\n\2\r\2\16\2\37\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3)\n\3\3\3\3\3\3\4\6\4.\n\4\r\4\16\4/\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5<\n\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\6\6C\n\6\r\6\16\6D\3\6\3\6\3\7\3\7\3\7\6\7L\n")
        buf.write("\7\r\7\16\7M\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\td\n\t\3\n\3")
        buf.write("\n\5\nh\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13q\n")
        buf.write("\13\f\13\16\13t\13\13\3\13\7\13w\n\13\f\13\16\13z\13\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\7\r\u0082\n\r\f\r\16\r\u0085")
        buf.write("\13\r\3\16\6\16\u0088\n\16\r\16\16\16\u0089\3\16\2\2\17")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\3\2\20\25\3\2\36")
        buf.write(" \2\u008c\2\35\3\2\2\2\4#\3\2\2\2\6-\3\2\2\2\b\61\3\2")
        buf.write("\2\2\n?\3\2\2\2\fH\3\2\2\2\16Q\3\2\2\2\20c\3\2\2\2\22")
        buf.write("g\3\2\2\2\24i\3\2\2\2\26}\3\2\2\2\30\177\3\2\2\2\32\u0087")
        buf.write("\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\2\2\3\"\3\3\2\2")
        buf.write("\2#$\5\6\4\2$%\7\3\2\2%&\5\b\5\2&(\5\n\6\2\')\5\f\7\2")
        buf.write("(\'\3\2\2\2()\3\2\2\2)*\3\2\2\2*+\7\4\2\2+\5\3\2\2\2,")
        buf.write(".\7\37\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write("\7\3\2\2\2\61\62\7\5\2\2\62;\7\3\2\2\63\64\7\33\2\2\64")
        buf.write("\65\7\35\2\2\65\66\7\34\2\2\66<\7\35\2\2\678\7\34\2\2")
        buf.write("89\7\35\2\29:\7\33\2\2:<\7\35\2\2;\63\3\2\2\2;\67\3\2")
        buf.write("\2\2<=\3\2\2\2=>\7\4\2\2>\t\3\2\2\2?@\7\6\2\2@B\7\3\2")
        buf.write("\2AC\5\22\n\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2")
        buf.write("EF\3\2\2\2FG\7\4\2\2G\13\3\2\2\2HI\7\7\2\2IK\7\3\2\2J")
        buf.write("L\7\37\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3")
        buf.write("\2\2\2OP\7\4\2\2P\r\3\2\2\2QR\t\2\2\2R\17\3\2\2\2Sd\5")
        buf.write("\16\b\2TU\7\26\2\2UV\7\b\2\2VW\5\20\t\2WX\7\t\2\2Xd\3")
        buf.write("\2\2\2YZ\7\31\2\2Z[\7\n\2\2[\\\7\36\2\2\\d\7\13\2\2]^")
        buf.write("\7\32\2\2^_\7\n\2\2_`\7\36\2\2`a\7\f\2\2ab\7\36\2\2bd")
        buf.write("\7\13\2\2cS\3\2\2\2cT\3\2\2\2cY\3\2\2\2c]\3\2\2\2d\21")
        buf.write("\3\2\2\2eh\5\24\13\2fh\5\30\r\2ge\3\2\2\2gf\3\2\2\2h\23")
        buf.write("\3\2\2\2ij\7\30\2\2jk\5\20\t\2kr\7\37\2\2lm\7\r\2\2mn")
        buf.write("\5\26\f\2no\7\16\2\2oq\3\2\2\2pl\3\2\2\2qt\3\2\2\2rp\3")
        buf.write("\2\2\2rs\3\2\2\2sx\3\2\2\2tr\3\2\2\2uw\5\32\16\2vu\3\2")
        buf.write("\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx\3\2\2\2")
        buf.write("{|\7\17\2\2|\25\3\2\2\2}~\t\3\2\2~\27\3\2\2\2\177\u0083")
        buf.write("\7\27\2\2\u0080\u0082\7\37\2\2\u0081\u0080\3\2\2\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\31\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0088\7\37")
        buf.write("\2\2\u0087\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u0087")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\33\3\2\2\2\16\37(/")
        buf.write(";DMcgrx\u0083\u0089")
        return buf.getvalue()


class CPPPParser ( Parser ):

    grammarFileName = "CPPP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'config'", "'generate'", 
                     "'checker'", "'<'", "'>'", "'('", "')'", "','", "'['", 
                     "']'", "';'", "'int'", "'float'", "'double'", "'ll'", 
                     "'char'", "'string'", "'array'", "'print'", "'var'", 
                     "'tree'", "'graph'", "'input'", "'output'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "DOUBLE", 
                      "LL", "CHAR", "STRTYPE", "ARRAY", "PRINT", "VAR", 
                      "TREE", "GRAPH", "INPUT", "OUTPUT", "CPP_FILE", "NUMBER", 
                      "ID", "STR", "WS" ]

    RULE_program = 0
    RULE_subtaskBlock = 1
    RULE_subtaskName = 2
    RULE_configBlock = 3
    RULE_genBlock = 4
    RULE_checkerBlock = 5
    RULE_primitiveType = 6
    RULE_dataType = 7
    RULE_func = 8
    RULE_var = 9
    RULE_expr = 10
    RULE_printStmt = 11
    RULE_option = 12

    ruleNames =  [ "program", "subtaskBlock", "subtaskName", "configBlock", 
                   "genBlock", "checkerBlock", "primitiveType", "dataType", 
                   "func", "var", "expr", "printStmt", "option" ]

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
    T__11=12
    T__12=13
    INT=14
    FLOAT=15
    DOUBLE=16
    LL=17
    CHAR=18
    STRTYPE=19
    ARRAY=20
    PRINT=21
    VAR=22
    TREE=23
    GRAPH=24
    INPUT=25
    OUTPUT=26
    CPP_FILE=27
    NUMBER=28
    ID=29
    STR=30
    WS=31

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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.subtaskBlock()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 31
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
            self.state = 33
            self.subtaskName()
            self.state = 34
            self.match(CPPPParser.T__0)
            self.state = 35
            self.configBlock()
            self.state = 36
            self.genBlock()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPPPParser.T__4:
                self.state = 37
                self.checkerBlock()


            self.state = 40
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
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.match(CPPPParser.ID)
                self.state = 45 
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

        def INPUT(self):
            return self.getToken(CPPPParser.INPUT, 0)

        def CPP_FILE(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.CPP_FILE)
            else:
                return self.getToken(CPPPParser.CPP_FILE, i)

        def OUTPUT(self):
            return self.getToken(CPPPParser.OUTPUT, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(CPPPParser.T__2)
            self.state = 48
            self.match(CPPPParser.T__0)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INPUT]:
                self.state = 49
                self.match(CPPPParser.INPUT)
                self.state = 50
                self.match(CPPPParser.CPP_FILE)
                self.state = 51
                self.match(CPPPParser.OUTPUT)
                self.state = 52
                self.match(CPPPParser.CPP_FILE)
                pass
            elif token in [CPPPParser.OUTPUT]:
                self.state = 53
                self.match(CPPPParser.OUTPUT)
                self.state = 54
                self.match(CPPPParser.CPP_FILE)
                self.state = 55
                self.match(CPPPParser.INPUT)
                self.state = 56
                self.match(CPPPParser.CPP_FILE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 59
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

        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.FuncContext)
            else:
                return self.getTypedRuleContext(CPPPParser.FuncContext,i)


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
            self.state = 61
            self.match(CPPPParser.T__3)
            self.state = 62
            self.match(CPPPParser.T__0)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.func()
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.PRINT or _la==CPPPParser.VAR):
                    break

            self.state = 68
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
            self.state = 70
            self.match(CPPPParser.T__4)
            self.state = 71
            self.match(CPPPParser.T__0)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.match(CPPPParser.ID)
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 77
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
            self.state = 79
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


        def TREE(self):
            return self.getToken(CPPPParser.TREE, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.NUMBER)
            else:
                return self.getToken(CPPPParser.NUMBER, i)

        def GRAPH(self):
            return self.getToken(CPPPParser.GRAPH, 0)

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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INT, CPPPParser.FLOAT, CPPPParser.DOUBLE, CPPPParser.LL, CPPPParser.CHAR, CPPPParser.STRTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.primitiveType()
                pass
            elif token in [CPPPParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(CPPPParser.ARRAY)
                self.state = 83
                self.match(CPPPParser.T__5)
                self.state = 84
                self.dataType()
                self.state = 85
                self.match(CPPPParser.T__6)
                pass
            elif token in [CPPPParser.TREE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(CPPPParser.TREE)
                self.state = 88
                self.match(CPPPParser.T__7)
                self.state = 89
                self.match(CPPPParser.NUMBER)
                self.state = 90
                self.match(CPPPParser.T__8)
                pass
            elif token in [CPPPParser.GRAPH]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(CPPPParser.GRAPH)
                self.state = 92
                self.match(CPPPParser.T__7)
                self.state = 93
                self.match(CPPPParser.NUMBER)
                self.state = 94
                self.match(CPPPParser.T__9)
                self.state = 95
                self.match(CPPPParser.NUMBER)
                self.state = 96
                self.match(CPPPParser.T__8)
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


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(CPPPParser.VarContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(CPPPParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return CPPPParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = CPPPParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.var()
                pass
            elif token in [CPPPParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.printStmt()
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

        def VAR(self):
            return self.getToken(CPPPParser.VAR, 0)

        def dataType(self):
            return self.getTypedRuleContext(CPPPParser.DataTypeContext,0)


        def ID(self):
            return self.getToken(CPPPParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ExprContext,i)


        def option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.OptionContext)
            else:
                return self.getTypedRuleContext(CPPPParser.OptionContext,i)


        def getRuleIndex(self):
            return CPPPParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = CPPPParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(CPPPParser.VAR)
            self.state = 104
            self.dataType()
            self.state = 105
            self.match(CPPPParser.ID)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.T__10:
                self.state = 106
                self.match(CPPPParser.T__10)
                self.state = 107
                self.expr()
                self.state = 108
                self.match(CPPPParser.T__11)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.ID:
                self.state = 115
                self.option()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self.match(CPPPParser.T__12)
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
        self.enterRule(localctx, 20, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
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


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(CPPPParser.PRINT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CPPPParser.ID)
            else:
                return self.getToken(CPPPParser.ID, i)

        def getRuleIndex(self):
            return CPPPParser.RULE_printStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = CPPPParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(CPPPParser.PRINT)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.ID:
                self.state = 126
                self.match(CPPPParser.ID)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(ParserRuleContext):
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
            return CPPPParser.RULE_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOption" ):
                return visitor.visitOption(self)
            else:
                return visitor.visitChildren(self)




    def option(self):

        localctx = CPPPParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 132
                    self.match(CPPPParser.ID)

                else:
                    raise NoViableAltException(self)
                self.state = 135 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





