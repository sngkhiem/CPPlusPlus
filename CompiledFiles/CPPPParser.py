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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u00c1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\6\2\"\n\2\r\2\16\2#\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\6\4/\n\4\r\4\16\4\60")
        buf.write("\3\5\3\5\3\5\6\5\66\n\5\r\5\16\5\67\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6G\n\6\3\7\3\7\3")
        buf.write("\7\6\7L\n\7\r\7\16\7M\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\tf\n\t\3\n\3\n\3\n\5\nk\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\7\13t\n\13\f\13\16\13w\13\13\3\13\7\13z")
        buf.write("\n\13\f\13\16\13}\13\13\3\13\3\13\3\f\3\f\6\f\u0083\n")
        buf.write("\f\r\f\16\f\u0084\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\7\r")
        buf.write("\u008f\n\r\f\r\16\r\u0092\13\r\3\r\3\r\3\16\3\16\5\16")
        buf.write("\u0098\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00a2\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00ae\n\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00bc\n\20\f\20")
        buf.write("\16\20\u00bf\13\20\3\20\2\3\36\21\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36\2\7\3\2\33 \3\2\21\23\4\2\20\20\24")
        buf.write("\24\4\2\7\b\25\30\3\2\31\32\2\u00cd\2!\3\2\2\2\4\'\3\2")
        buf.write("\2\2\6.\3\2\2\2\b\62\3\2\2\2\nF\3\2\2\2\fH\3\2\2\2\16")
        buf.write("Q\3\2\2\2\20e\3\2\2\2\22j\3\2\2\2\24l\3\2\2\2\26\u0080")
        buf.write("\3\2\2\2\30\u0088\3\2\2\2\32\u0095\3\2\2\2\34\u00a1\3")
        buf.write("\2\2\2\36\u00ad\3\2\2\2 \"\5\4\3\2! \3\2\2\2\"#\3\2\2")
        buf.write("\2#!\3\2\2\2#$\3\2\2\2$%\3\2\2\2%&\7\2\2\3&\3\3\2\2\2")
        buf.write("\'(\5\6\4\2()\7\3\2\2)*\5\b\5\2*+\5\f\7\2+,\7\4\2\2,\5")
        buf.write("\3\2\2\2-/\7.\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\7\3\2\2\2\62\63\7\5\2\2\63\65\7\3\2\2\64")
        buf.write("\66\5\n\6\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2")
        buf.write("\678\3\2\2\289\3\2\2\29:\7\4\2\2:\t\3\2\2\2;<\7&\2\2<")
        buf.write("G\7/\2\2=>\7\'\2\2>G\7/\2\2?@\7(\2\2@G\7-\2\2AB\7*\2\2")
        buf.write("BG\7/\2\2CD\7)\2\2DG\7/\2\2EG\5\32\16\2F;\3\2\2\2F=\3")
        buf.write("\2\2\2F?\3\2\2\2FA\3\2\2\2FC\3\2\2\2FE\3\2\2\2G\13\3\2")
        buf.write("\2\2HI\7\6\2\2IK\7\3\2\2JL\5\22\n\2KJ\3\2\2\2LM\3\2\2")
        buf.write("\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\7\4\2\2P\r\3\2\2\2")
        buf.write("QR\t\2\2\2R\17\3\2\2\2Sf\5\16\b\2TU\7!\2\2UV\7\7\2\2V")
        buf.write("W\5\20\t\2WX\7\b\2\2Xf\3\2\2\2YZ\7$\2\2Z[\7\t\2\2[\\\5")
        buf.write("\36\20\2\\]\7\n\2\2]f\3\2\2\2^_\7%\2\2_`\7\t\2\2`a\5\36")
        buf.write("\20\2ab\7\13\2\2bc\5\36\20\2cd\7\n\2\2df\3\2\2\2eS\3\2")
        buf.write("\2\2eT\3\2\2\2eY\3\2\2\2e^\3\2\2\2f\21\3\2\2\2gk\5\24")
        buf.write("\13\2hk\5\26\f\2ik\5\30\r\2jg\3\2\2\2jh\3\2\2\2ji\3\2")
        buf.write("\2\2k\23\3\2\2\2lm\7#\2\2mn\5\20\t\2nu\7.\2\2op\7\f\2")
        buf.write("\2pq\5\36\20\2qr\7\r\2\2rt\3\2\2\2so\3\2\2\2tw\3\2\2\2")
        buf.write("us\3\2\2\2uv\3\2\2\2v{\3\2\2\2wu\3\2\2\2xz\5\34\17\2y")
        buf.write("x\3\2\2\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|~\3\2\2\2}{\3")
        buf.write("\2\2\2~\177\7\16\2\2\177\25\3\2\2\2\u0080\u0082\7\"\2")
        buf.write("\2\u0081\u0083\5\36\20\2\u0082\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0087\7\16\2\2\u0087\27\3\2\2\2\u0088")
        buf.write("\u0089\7\17\2\2\u0089\u008a\7\t\2\2\u008a\u008b\5\36\20")
        buf.write("\2\u008b\u008c\7\n\2\2\u008c\u0090\7\3\2\2\u008d\u008f")
        buf.write("\5\22\n\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2\u0090")
        buf.write("\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3\2\2\2")
        buf.write("\u0092\u0090\3\2\2\2\u0093\u0094\7\4\2\2\u0094\31\3\2")
        buf.write("\2\2\u0095\u0097\7+\2\2\u0096\u0098\5\36\20\2\u0097\u0096")
        buf.write("\3\2\2\2\u0097\u0098\3\2\2\2\u0098\33\3\2\2\2\u0099\u00a2")
        buf.write("\7.\2\2\u009a\u009b\7,\2\2\u009b\u009c\7\t\2\2\u009c\u009d")
        buf.write("\5\36\20\2\u009d\u009e\7\13\2\2\u009e\u009f\5\36\20\2")
        buf.write("\u009f\u00a0\7\n\2\2\u00a0\u00a2\3\2\2\2\u00a1\u0099\3")
        buf.write("\2\2\2\u00a1\u009a\3\2\2\2\u00a2\35\3\2\2\2\u00a3\u00a4")
        buf.write("\b\20\1\2\u00a4\u00a5\7\20\2\2\u00a5\u00ae\5\36\20\13")
        buf.write("\u00a6\u00a7\7\t\2\2\u00a7\u00a8\5\36\20\2\u00a8\u00a9")
        buf.write("\7\n\2\2\u00a9\u00ae\3\2\2\2\u00aa\u00ae\7.\2\2\u00ab")
        buf.write("\u00ae\7-\2\2\u00ac\u00ae\7/\2\2\u00ad\u00a3\3\2\2\2\u00ad")
        buf.write("\u00a6\3\2\2\2\u00ad\u00aa\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ac\3\2\2\2\u00ae\u00bd\3\2\2\2\u00af\u00b0\f")
        buf.write("\t\2\2\u00b0\u00b1\t\3\2\2\u00b1\u00bc\5\36\20\n\u00b2")
        buf.write("\u00b3\f\b\2\2\u00b3\u00b4\t\4\2\2\u00b4\u00bc\5\36\20")
        buf.write("\t\u00b5\u00b6\f\7\2\2\u00b6\u00b7\t\5\2\2\u00b7\u00bc")
        buf.write("\5\36\20\b\u00b8\u00b9\f\6\2\2\u00b9\u00ba\t\6\2\2\u00ba")
        buf.write("\u00bc\5\36\20\7\u00bb\u00af\3\2\2\2\u00bb\u00b2\3\2\2")
        buf.write("\2\u00bb\u00b5\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bc\u00bf")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\37\3\2\2\2\u00bf\u00bd\3\2\2\2\22#\60\67FMeju{\u0084")
        buf.write("\u0090\u0097\u00a1\u00ad\u00bb\u00bd")
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
    RULE_compare = 12
    RULE_option = 13
    RULE_expr = 14

    ruleNames =  [ "program", "subtaskBlock", "subtaskName", "configBlock", 
                   "configItem", "genBlock", "primitiveType", "dataType", 
                   "func", "var", "printStmt", "loopStmt", "compare", "option", 
                   "expr" ]

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
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.subtaskBlock()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 35
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
            self.state = 37
            self.subtaskName()
            self.state = 38
            self.match(CPPPParser.T__0)
            self.state = 39
            self.configBlock()
            self.state = 40
            self.genBlock()
            self.state = 41
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
            self.state = 48
            self.match(CPPPParser.T__2)
            self.state = 49
            self.match(CPPPParser.T__0)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.configItem()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.INPUT) | (1 << CPPPParser.OUTPUT) | (1 << CPPPParser.TESTS) | (1 << CPPPParser.TEST_SOL) | (1 << CPPPParser.SOL) | (1 << CPPPParser.COMPARE))) != 0)):
                    break

            self.state = 55
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

        def compare(self):
            return self.getTypedRuleContext(CPPPParser.CompareContext,0)


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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INPUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(CPPPParser.INPUT)
                self.state = 58
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.OUTPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(CPPPParser.OUTPUT)
                self.state = 60
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.TESTS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(CPPPParser.TESTS)
                self.state = 62
                self.match(CPPPParser.NUMBER)
                pass
            elif token in [CPPPParser.SOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(CPPPParser.SOL)
                self.state = 64
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.TEST_SOL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 65
                self.match(CPPPParser.TEST_SOL)
                self.state = 66
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.COMPARE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.compare()
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
            self.state = 70
            self.match(CPPPParser.T__3)
            self.state = 71
            self.match(CPPPParser.T__0)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.func()
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__12) | (1 << CPPPParser.PRINT) | (1 << CPPPParser.VAR))) != 0)):
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
            self.state = 99
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
                self.match(CPPPParser.T__4)
                self.state = 84
                self.dataType()
                self.state = 85
                self.match(CPPPParser.T__5)
                pass
            elif token in [CPPPParser.TREE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.match(CPPPParser.TREE)
                self.state = 88
                self.match(CPPPParser.T__6)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(CPPPParser.T__7)
                pass
            elif token in [CPPPParser.GRAPH]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.match(CPPPParser.GRAPH)
                self.state = 93
                self.match(CPPPParser.T__6)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(CPPPParser.T__8)
                self.state = 96
                self.expr(0)
                self.state = 97
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
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.var()
                pass
            elif token in [CPPPParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.printStmt()
                pass
            elif token in [CPPPParser.T__12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
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
            self.state = 106
            self.match(CPPPParser.VAR)
            self.state = 107
            self.dataType()
            self.state = 108
            self.match(CPPPParser.ID)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.T__9:
                self.state = 109
                self.match(CPPPParser.T__9)
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(CPPPParser.T__10)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.RANGE or _la==CPPPParser.ID:
                self.state = 118
                self.option()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 124
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
            self.state = 126
            self.match(CPPPParser.PRINT)
            self.state = 128 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 127
                self.expr(0)
                self.state = 130 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__6) | (1 << CPPPParser.T__13) | (1 << CPPPParser.NUMBER) | (1 << CPPPParser.ID) | (1 << CPPPParser.STR))) != 0)):
                    break

            self.state = 132
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
            self.state = 134
            self.match(CPPPParser.T__12)
            self.state = 135
            self.match(CPPPParser.T__6)
            self.state = 136
            self.expr(0)
            self.state = 137
            self.match(CPPPParser.T__7)
            self.state = 138
            self.match(CPPPParser.T__0)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__12) | (1 << CPPPParser.PRINT) | (1 << CPPPParser.VAR))) != 0):
                self.state = 139
                self.func()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPARE(self):
            return self.getToken(CPPPParser.COMPARE, 0)

        def expr(self):
            return self.getTypedRuleContext(CPPPParser.ExprContext,0)


        def getRuleIndex(self):
            return CPPPParser.RULE_compare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)




    def compare(self):

        localctx = CPPPParser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(CPPPParser.COMPARE)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__6) | (1 << CPPPParser.T__13) | (1 << CPPPParser.NUMBER) | (1 << CPPPParser.ID) | (1 << CPPPParser.STR))) != 0):
                self.state = 148
                self.expr(0)


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
        self.enterRule(localctx, 26, self.RULE_option)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.match(CPPPParser.ID)
                pass
            elif token in [CPPPParser.RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(CPPPParser.RANGE)
                self.state = 153
                self.match(CPPPParser.T__6)
                self.state = 154
                self.expr(0)
                self.state = 155
                self.match(CPPPParser.T__8)
                self.state = 156
                self.expr(0)
                self.state = 157
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.T__13]:
                self.state = 162
                self.match(CPPPParser.T__13)
                self.state = 163
                self.expr(9)
                pass
            elif token in [CPPPParser.T__6]:
                self.state = 164
                self.match(CPPPParser.T__6)
                self.state = 165
                self.expr(0)
                self.state = 166
                self.match(CPPPParser.T__7)
                pass
            elif token in [CPPPParser.ID]:
                self.state = 168
                self.match(CPPPParser.ID)
                pass
            elif token in [CPPPParser.NUMBER]:
                self.state = 169
                self.match(CPPPParser.NUMBER)
                pass
            elif token in [CPPPParser.STR]:
                self.state = 170
                self.match(CPPPParser.STR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 187
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 185
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 174
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__14) | (1 << CPPPParser.T__15) | (1 << CPPPParser.T__16))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 177
                        _la = self._input.LA(1)
                        if not(_la==CPPPParser.T__13 or _la==CPPPParser.T__17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 180
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__4) | (1 << CPPPParser.T__5) | (1 << CPPPParser.T__18) | (1 << CPPPParser.T__19) | (1 << CPPPParser.T__20) | (1 << CPPPParser.T__21))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 181
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 182
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 183
                        _la = self._input.LA(1)
                        if not(_la==CPPPParser.T__22 or _la==CPPPParser.T__23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 184
                        self.expr(5)
                        pass

             
                self.state = 189
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self._predicates[14] = self.expr_sempred
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
         




