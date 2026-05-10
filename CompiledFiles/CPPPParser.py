# Generated from .\grammar\CPPP.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u00bb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\6\2 \n\2\r\2\16\2!\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\6\4-\n\4\r\4\16\4.\3\5\3\5\3\5\6")
        buf.write("\5\64\n\5\r\5\16\5\65\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6E\n\6\3\7\3\7\3\7\6\7J\n\7\r\7")
        buf.write("\16\7K\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\td\n\t\3\n")
        buf.write("\3\n\3\n\5\ni\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7")
        buf.write("\13r\n\13\f\13\16\13u\13\13\3\13\7\13x\n\13\f\13\16\13")
        buf.write("{\13\13\3\13\3\13\3\f\3\f\6\f\u0081\n\f\r\f\16\f\u0082")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u008d\n\r\f\r\16")
        buf.write("\r\u0090\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u009c\n\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00a8\n\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\7\17\u00b6")
        buf.write("\n\17\f\17\16\17\u00b9\13\17\3\17\2\3\34\20\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\2\7\3\2\33 \3\2\21\23\4\2\20")
        buf.write("\20\24\24\4\2\7\b\25\30\3\2\31\32\2\u00c7\2\37\3\2\2\2")
        buf.write("\4%\3\2\2\2\6,\3\2\2\2\b\60\3\2\2\2\nD\3\2\2\2\fF\3\2")
        buf.write("\2\2\16O\3\2\2\2\20c\3\2\2\2\22h\3\2\2\2\24j\3\2\2\2\26")
        buf.write("~\3\2\2\2\30\u0086\3\2\2\2\32\u009b\3\2\2\2\34\u00a7\3")
        buf.write("\2\2\2\36 \5\4\3\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2\2\2")
        buf.write("!\"\3\2\2\2\"#\3\2\2\2#$\7\2\2\3$\3\3\2\2\2%&\5\6\4\2")
        buf.write("&\'\7\3\2\2\'(\5\b\5\2()\5\f\7\2)*\7\4\2\2*\5\3\2\2\2")
        buf.write("+-\7.\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\7\3")
        buf.write("\2\2\2\60\61\7\5\2\2\61\63\7\3\2\2\62\64\5\n\6\2\63\62")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66")
        buf.write("\67\3\2\2\2\678\7\4\2\28\t\3\2\2\29:\7&\2\2:E\7/\2\2;")
        buf.write("<\7\'\2\2<E\7/\2\2=>\7(\2\2>E\7-\2\2?@\7*\2\2@E\7/\2\2")
        buf.write("AB\7)\2\2BE\7/\2\2CE\7+\2\2D9\3\2\2\2D;\3\2\2\2D=\3\2")
        buf.write("\2\2D?\3\2\2\2DA\3\2\2\2DC\3\2\2\2E\13\3\2\2\2FG\7\6\2")
        buf.write("\2GI\7\3\2\2HJ\5\22\n\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2")
        buf.write("KL\3\2\2\2LM\3\2\2\2MN\7\4\2\2N\r\3\2\2\2OP\t\2\2\2P\17")
        buf.write("\3\2\2\2Qd\5\16\b\2RS\7!\2\2ST\7\7\2\2TU\5\20\t\2UV\7")
        buf.write("\b\2\2Vd\3\2\2\2WX\7$\2\2XY\7\t\2\2YZ\5\34\17\2Z[\7\n")
        buf.write("\2\2[d\3\2\2\2\\]\7%\2\2]^\7\t\2\2^_\5\34\17\2_`\7\13")
        buf.write("\2\2`a\5\34\17\2ab\7\n\2\2bd\3\2\2\2cQ\3\2\2\2cR\3\2\2")
        buf.write("\2cW\3\2\2\2c\\\3\2\2\2d\21\3\2\2\2ei\5\24\13\2fi\5\26")
        buf.write("\f\2gi\5\30\r\2he\3\2\2\2hf\3\2\2\2hg\3\2\2\2i\23\3\2")
        buf.write("\2\2jk\7#\2\2kl\5\20\t\2ls\7.\2\2mn\7\f\2\2no\5\34\17")
        buf.write("\2op\7\r\2\2pr\3\2\2\2qm\3\2\2\2ru\3\2\2\2sq\3\2\2\2s")
        buf.write("t\3\2\2\2ty\3\2\2\2us\3\2\2\2vx\5\32\16\2wv\3\2\2\2x{")
        buf.write("\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2\2{y\3\2\2\2|}\7\16")
        buf.write("\2\2}\25\3\2\2\2~\u0080\7\"\2\2\177\u0081\5\34\17\2\u0080")
        buf.write("\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\7\16\2")
        buf.write("\2\u0085\27\3\2\2\2\u0086\u0087\7\17\2\2\u0087\u0088\7")
        buf.write("\t\2\2\u0088\u0089\5\34\17\2\u0089\u008a\7\n\2\2\u008a")
        buf.write("\u008e\7\3\2\2\u008b\u008d\5\22\n\2\u008c\u008b\3\2\2")
        buf.write("\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\u0091\3\2\2\2\u0090\u008e\3\2\2\2\u0091")
        buf.write("\u0092\7\4\2\2\u0092\31\3\2\2\2\u0093\u009c\7.\2\2\u0094")
        buf.write("\u0095\7,\2\2\u0095\u0096\7\t\2\2\u0096\u0097\5\34\17")
        buf.write("\2\u0097\u0098\7\13\2\2\u0098\u0099\5\34\17\2\u0099\u009a")
        buf.write("\7\n\2\2\u009a\u009c\3\2\2\2\u009b\u0093\3\2\2\2\u009b")
        buf.write("\u0094\3\2\2\2\u009c\33\3\2\2\2\u009d\u009e\b\17\1\2\u009e")
        buf.write("\u009f\7\20\2\2\u009f\u00a8\5\34\17\13\u00a0\u00a1\7\t")
        buf.write("\2\2\u00a1\u00a2\5\34\17\2\u00a2\u00a3\7\n\2\2\u00a3\u00a8")
        buf.write("\3\2\2\2\u00a4\u00a8\7.\2\2\u00a5\u00a8\7-\2\2\u00a6\u00a8")
        buf.write("\7/\2\2\u00a7\u009d\3\2\2\2\u00a7\u00a0\3\2\2\2\u00a7")
        buf.write("\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a6\3\2\2\2")
        buf.write("\u00a8\u00b7\3\2\2\2\u00a9\u00aa\f\t\2\2\u00aa\u00ab\t")
        buf.write("\3\2\2\u00ab\u00b6\5\34\17\n\u00ac\u00ad\f\b\2\2\u00ad")
        buf.write("\u00ae\t\4\2\2\u00ae\u00b6\5\34\17\t\u00af\u00b0\f\7\2")
        buf.write("\2\u00b0\u00b1\t\5\2\2\u00b1\u00b6\5\34\17\b\u00b2\u00b3")
        buf.write("\f\6\2\2\u00b3\u00b4\t\6\2\2\u00b4\u00b6\5\34\17\7\u00b5")
        buf.write("\u00a9\3\2\2\2\u00b5\u00ac\3\2\2\2\u00b5\u00af\3\2\2\2")
        buf.write("\u00b5\u00b2\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3")
        buf.write("\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\35\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\21!.\65DKchsy\u0082\u008e\u009b\u00a7\u00b5\u00b7")
        return buf.getvalue()


class CPPPParser ( Parser ):

    grammarFileName = "CPPP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'config'", "'generate'", 
                     "'<'", "'>'", "'('", "')'", "','", "'['", "']'", "';'", 
                     "'repeat'", "'-'", "'*'", "'/'", "'%'", "'+'", "'>='", 
                     "'<='", "'=='", "'!='", "'&&'", "'||'", "'int'", "'float'", 
                     "'double'", "'ll'", "'char'", "'string'", "'array'", 
                     "'print'", "'var'", "'tree'", "'graph'", "'input'", 
                     "'output'", "'tests'", "'test_sol'", "'sol'", "'compare'", 
                     "'range'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "FLOAT", "DOUBLE", "LL", "CHAR", 
                      "STRTYPE", "ARRAY", "PRINT", "VAR", "TREE", "GRAPH", 
                      "INPUT", "OUTPUT", "TESTS", "TEST_SOL", "SOL", "COMPARE", 
                      "RANGE", "NUMBER", "ID", "STR", "WS" ]

    RULE_program = 0
    RULE_subtaskBlock = 1
    RULE_subtaskName = 2
    RULE_configBlock = 3
    RULE_configItem = 4
    RULE_genBlock = 5
    RULE_primitiveType = 6
    RULE_dataType = 7
    RULE_func = 8
    RULE_var = 9
    RULE_printStmt = 10
    RULE_loopStmt = 11
    RULE_option = 12
    RULE_expr = 13

    ruleNames =  [ "program", "subtaskBlock", "subtaskName", "configBlock", 
                   "configItem", "genBlock", "primitiveType", "dataType", 
                   "func", "var", "printStmt", "loopStmt", "option", "expr" ]

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
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    INT=25
    FLOAT=26
    DOUBLE=27
    LL=28
    CHAR=29
    STRTYPE=30
    ARRAY=31
    PRINT=32
    VAR=33
    TREE=34
    GRAPH=35
    INPUT=36
    OUTPUT=37
    TESTS=38
    TEST_SOL=39
    SOL=40
    COMPARE=41
    RANGE=42
    NUMBER=43
    ID=44
    STR=45
    WS=46

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.subtaskBlock()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 33
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.subtaskName()
            self.state = 36
            self.match(CPPPParser.T__0)
            self.state = 37
            self.configBlock()
            self.state = 38
            self.genBlock()
            self.state = 39
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
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.match(CPPPParser.ID)
                self.state = 44 
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

        def configItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ConfigItemContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ConfigItemContext,i)


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
            self.state = 46
            self.match(CPPPParser.T__2)
            self.state = 47
            self.match(CPPPParser.T__0)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.configItem()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.INPUT) | (1 << CPPPParser.OUTPUT) | (1 << CPPPParser.TESTS) | (1 << CPPPParser.TEST_SOL) | (1 << CPPPParser.SOL) | (1 << CPPPParser.COMPARE))) != 0)):
                    break

            self.state = 53
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(CPPPParser.INPUT, 0)

        def STR(self):
            return self.getToken(CPPPParser.STR, 0)

        def OUTPUT(self):
            return self.getToken(CPPPParser.OUTPUT, 0)

        def TESTS(self):
            return self.getToken(CPPPParser.TESTS, 0)

        def NUMBER(self):
            return self.getToken(CPPPParser.NUMBER, 0)

        def SOL(self):
            return self.getToken(CPPPParser.SOL, 0)

        def TEST_SOL(self):
            return self.getToken(CPPPParser.TEST_SOL, 0)

        def COMPARE(self):
            return self.getToken(CPPPParser.COMPARE, 0)

        def getRuleIndex(self):
            return CPPPParser.RULE_configItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigItem" ):
                return visitor.visitConfigItem(self)
            else:
                return visitor.visitChildren(self)




    def configItem(self):

        localctx = CPPPParser.ConfigItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_configItem)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INPUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(CPPPParser.INPUT)
                self.state = 56
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.OUTPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.match(CPPPParser.OUTPUT)
                self.state = 58
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.TESTS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(CPPPParser.TESTS)
                self.state = 60
                self.match(CPPPParser.NUMBER)
                pass
            elif token in [CPPPParser.SOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.match(CPPPParser.SOL)
                self.state = 62
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.TEST_SOL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.match(CPPPParser.TEST_SOL)
                self.state = 64
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.COMPARE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.match(CPPPParser.COMPARE)
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
        self.enterRule(localctx, 10, self.RULE_genBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(CPPPParser.T__3)
            self.state = 69
            self.match(CPPPParser.T__0)
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.func()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__12) | (1 << CPPPParser.PRINT) | (1 << CPPPParser.VAR))) != 0)):
                    break

            self.state = 75
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
            self.state = 77
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ExprContext,i)


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
                self.state = 79
                self.primitiveType()
                pass
            elif token in [CPPPParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(CPPPParser.ARRAY)
                self.state = 81
                self.match(CPPPParser.T__4)
                self.state = 82
                self.dataType()
                self.state = 83
                self.match(CPPPParser.T__5)
                pass
            elif token in [CPPPParser.TREE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.match(CPPPParser.TREE)
                self.state = 86
                self.match(CPPPParser.T__6)
                self.state = 87
                self.expr(0)
                self.state = 88
                self.match(CPPPParser.T__7)
                pass
            elif token in [CPPPParser.GRAPH]:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(CPPPParser.GRAPH)
                self.state = 91
                self.match(CPPPParser.T__6)
                self.state = 92
                self.expr(0)
                self.state = 93
                self.match(CPPPParser.T__8)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(CPPPParser.T__7)
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


        def loopStmt(self):
            return self.getTypedRuleContext(CPPPParser.LoopStmtContext,0)


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
            self.state = 102
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
            elif token in [CPPPParser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 101
                self.loopStmt()
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
            self.state = 104
            self.match(CPPPParser.VAR)
            self.state = 105
            self.dataType()
            self.state = 106
            self.match(CPPPParser.ID)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.T__9:
                self.state = 107
                self.match(CPPPParser.T__9)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(CPPPParser.T__10)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.RANGE or _la==CPPPParser.ID:
                self.state = 116
                self.option()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(CPPPParser.T__11)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ExprContext,i)


        def getRuleIndex(self):
            return CPPPParser.RULE_printStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = CPPPParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(CPPPParser.PRINT)
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 125
                self.expr(0)
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__6) | (1 << CPPPParser.T__13) | (1 << CPPPParser.NUMBER) | (1 << CPPPParser.ID) | (1 << CPPPParser.STR))) != 0)):
                    break

            self.state = 130
            self.match(CPPPParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CPPPParser.ExprContext,0)


        def func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.FuncContext)
            else:
                return self.getTypedRuleContext(CPPPParser.FuncContext,i)


        def getRuleIndex(self):
            return CPPPParser.RULE_loopStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopStmt" ):
                return visitor.visitLoopStmt(self)
            else:
                return visitor.visitChildren(self)




    def loopStmt(self):

        localctx = CPPPParser.LoopStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_loopStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CPPPParser.T__12)
            self.state = 133
            self.match(CPPPParser.T__6)
            self.state = 134
            self.expr(0)
            self.state = 135
            self.match(CPPPParser.T__7)
            self.state = 136
            self.match(CPPPParser.T__0)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__12) | (1 << CPPPParser.PRINT) | (1 << CPPPParser.VAR))) != 0):
                self.state = 137
                self.func()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(CPPPParser.T__1)
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

        def ID(self):
            return self.getToken(CPPPParser.ID, 0)

        def RANGE(self):
            return self.getToken(CPPPParser.RANGE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ExprContext,i)


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
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.match(CPPPParser.ID)
                pass
            elif token in [CPPPParser.RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(CPPPParser.RANGE)
                self.state = 147
                self.match(CPPPParser.T__6)
                self.state = 148
                self.expr(0)
                self.state = 149
                self.match(CPPPParser.T__8)
                self.state = 150
                self.expr(0)
                self.state = 151
                self.match(CPPPParser.T__7)
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.ExprContext)
            else:
                return self.getTypedRuleContext(CPPPParser.ExprContext,i)


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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CPPPParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.T__13]:
                self.state = 156
                self.match(CPPPParser.T__13)
                self.state = 157
                self.expr(9)
                pass
            elif token in [CPPPParser.T__6]:
                self.state = 158
                self.match(CPPPParser.T__6)
                self.state = 159
                self.expr(0)
                self.state = 160
                self.match(CPPPParser.T__7)
                pass
            elif token in [CPPPParser.ID]:
                self.state = 162
                self.match(CPPPParser.ID)
                pass
            elif token in [CPPPParser.NUMBER]:
                self.state = 163
                self.match(CPPPParser.NUMBER)
                pass
            elif token in [CPPPParser.STR]:
                self.state = 164
                self.match(CPPPParser.STR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 179
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 168
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__14) | (1 << CPPPParser.T__15) | (1 << CPPPParser.T__16))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 171
                        _la = self._input.LA(1)
                        if not(_la==CPPPParser.T__13 or _la==CPPPParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 174
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__4) | (1 << CPPPParser.T__5) | (1 << CPPPParser.T__18) | (1 << CPPPParser.T__19) | (1 << CPPPParser.T__20) | (1 << CPPPParser.T__21))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 177
                        _la = self._input.LA(1)
                        if not(_la==CPPPParser.T__22 or _la==CPPPParser.T__23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        self.expr(5)
                        pass

             
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




