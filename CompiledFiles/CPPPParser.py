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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u00e2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\6\2")
        buf.write("&\n\2\r\2\16\2\'\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\61\n")
        buf.write("\3\3\3\3\3\3\4\6\4\66\n\4\r\4\16\4\67\3\5\3\5\3\5\6\5")
        buf.write("=\n\5\r\5\16\5>\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6M\n\6\3\7\3\7\3\7\6\7R\n\7\r\7\16\7S\3\7")
        buf.write("\3\7\3\b\3\b\3\b\7\b[\n\b\f\b\16\b^\13\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\nv\n\n\3\13\3\13\3\13\5\13{\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u0084\n\f\f\f\16\f\u0087")
        buf.write("\13\f\3\f\7\f\u008a\n\f\f\f\16\f\u008d\13\f\3\f\3\f\3")
        buf.write("\r\3\r\6\r\u0093\n\r\r\r\16\r\u0094\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\7\16\u009f\n\16\f\16\16\16\u00a2")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17\u00ab\n")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00b7\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\5\21\u00c3\n\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u00cf\n\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22")
        buf.write("\u00dd\n\22\f\22\16\22\u00e0\13\22\3\22\2\3\"\23\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"\2\b\3\2 %\3\2\23")
        buf.write("\24\3\2\26\30\4\2\25\25\31\31\4\2\b\t\32\35\3\2\36\37")
        buf.write("\2\u00ee\2%\3\2\2\2\4+\3\2\2\2\6\65\3\2\2\2\b9\3\2\2\2")
        buf.write("\nL\3\2\2\2\fN\3\2\2\2\16W\3\2\2\2\20a\3\2\2\2\22u\3\2")
        buf.write("\2\2\24z\3\2\2\2\26|\3\2\2\2\30\u0090\3\2\2\2\32\u0098")
        buf.write("\3\2\2\2\34\u00b6\3\2\2\2\36\u00b8\3\2\2\2 \u00c2\3\2")
        buf.write("\2\2\"\u00ce\3\2\2\2$&\5\4\3\2%$\3\2\2\2&\'\3\2\2\2\'")
        buf.write("%\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\2\2\3*\3\3\2\2\2+,")
        buf.write("\5\6\4\2,-\7\3\2\2-.\5\b\5\2.\60\5\f\7\2/\61\5\16\b\2")
        buf.write("\60/\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\7\4\2\2")
        buf.write("\63\5\3\2\2\2\64\66\7\62\2\2\65\64\3\2\2\2\66\67\3\2\2")
        buf.write("\2\67\65\3\2\2\2\678\3\2\2\28\7\3\2\2\29:\7\5\2\2:<\7")
        buf.write("\3\2\2;=\5\n\6\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2")
        buf.write("\2?@\3\2\2\2@A\7\4\2\2A\t\3\2\2\2BC\7+\2\2CM\7\63\2\2")
        buf.write("DE\7,\2\2EM\7\63\2\2FG\7-\2\2GM\7\61\2\2HI\7/\2\2IM\7")
        buf.write("\63\2\2JK\7.\2\2KM\7\63\2\2LB\3\2\2\2LD\3\2\2\2LF\3\2")
        buf.write("\2\2LH\3\2\2\2LJ\3\2\2\2M\13\3\2\2\2NO\7\6\2\2OQ\7\3\2")
        buf.write("\2PR\5\24\13\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2")
        buf.write("TU\3\2\2\2UV\7\4\2\2V\r\3\2\2\2WX\7\7\2\2X\\\7\3\2\2Y")
        buf.write("[\5\34\17\2ZY\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2")
        buf.write("]_\3\2\2\2^\\\3\2\2\2_`\7\4\2\2`\17\3\2\2\2ab\t\2\2\2")
        buf.write("b\21\3\2\2\2cv\5\20\t\2de\7&\2\2ef\7\b\2\2fg\5\22\n\2")
        buf.write("gh\7\t\2\2hv\3\2\2\2ij\7)\2\2jk\7\n\2\2kl\5\"\22\2lm\7")
        buf.write("\13\2\2mv\3\2\2\2no\7*\2\2op\7\n\2\2pq\5\"\22\2qr\7\f")
        buf.write("\2\2rs\5\"\22\2st\7\13\2\2tv\3\2\2\2uc\3\2\2\2ud\3\2\2")
        buf.write("\2ui\3\2\2\2un\3\2\2\2v\23\3\2\2\2w{\5\26\f\2x{\5\30\r")
        buf.write("\2y{\5\32\16\2zw\3\2\2\2zx\3\2\2\2zy\3\2\2\2{\25\3\2\2")
        buf.write("\2|}\7(\2\2}~\5\22\n\2~\u0085\7\62\2\2\177\u0080\7\r\2")
        buf.write("\2\u0080\u0081\5\"\22\2\u0081\u0082\7\16\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\177\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u008b\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\u008a\5 \21\2\u0089\u0088\3\2\2\2")
        buf.write("\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f")
        buf.write("\7\17\2\2\u008f\27\3\2\2\2\u0090\u0092\7\'\2\2\u0091\u0093")
        buf.write("\5\"\22\2\u0092\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2")
        buf.write("\u0096\u0097\7\17\2\2\u0097\31\3\2\2\2\u0098\u0099\7\20")
        buf.write("\2\2\u0099\u009a\7\n\2\2\u009a\u009b\5\"\22\2\u009b\u009c")
        buf.write("\7\13\2\2\u009c\u00a0\7\3\2\2\u009d\u009f\5\24\13\2\u009e")
        buf.write("\u009d\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a0\3")
        buf.write("\2\2\2\u00a3\u00a4\7\4\2\2\u00a4\33\3\2\2\2\u00a5\u00a6")
        buf.write("\7\21\2\2\u00a6\u00a7\7\n\2\2\u00a7\u00aa\5\"\22\2\u00a8")
        buf.write("\u00a9\7\f\2\2\u00a9\u00ab\7\63\2\2\u00aa\u00a8\3\2\2")
        buf.write("\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad")
        buf.write("\7\13\2\2\u00ad\u00ae\7\17\2\2\u00ae\u00b7\3\2\2\2\u00af")
        buf.write("\u00b0\7(\2\2\u00b0\u00b1\5\22\n\2\u00b1\u00b2\7\62\2")
        buf.write("\2\u00b2\u00b3\7\22\2\2\u00b3\u00b4\5\36\20\2\u00b4\u00b5")
        buf.write("\7\17\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00a5\3\2\2\2\u00b6")
        buf.write("\u00af\3\2\2\2\u00b7\35\3\2\2\2\u00b8\u00b9\t\3\2\2\u00b9")
        buf.write("\37\3\2\2\2\u00ba\u00c3\7\62\2\2\u00bb\u00bc\7\60\2\2")
        buf.write("\u00bc\u00bd\7\n\2\2\u00bd\u00be\5\"\22\2\u00be\u00bf")
        buf.write("\7\f\2\2\u00bf\u00c0\5\"\22\2\u00c0\u00c1\7\13\2\2\u00c1")
        buf.write("\u00c3\3\2\2\2\u00c2\u00ba\3\2\2\2\u00c2\u00bb\3\2\2\2")
        buf.write("\u00c3!\3\2\2\2\u00c4\u00c5\b\22\1\2\u00c5\u00c6\7\25")
        buf.write("\2\2\u00c6\u00cf\5\"\22\13\u00c7\u00c8\7\n\2\2\u00c8\u00c9")
        buf.write("\5\"\22\2\u00c9\u00ca\7\13\2\2\u00ca\u00cf\3\2\2\2\u00cb")
        buf.write("\u00cf\7\62\2\2\u00cc\u00cf\7\61\2\2\u00cd\u00cf\7\63")
        buf.write("\2\2\u00ce\u00c4\3\2\2\2\u00ce\u00c7\3\2\2\2\u00ce\u00cb")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\u00de\3\2\2\2\u00d0\u00d1\f\t\2\2\u00d1\u00d2\t\4\2\2")
        buf.write("\u00d2\u00dd\5\"\22\n\u00d3\u00d4\f\b\2\2\u00d4\u00d5")
        buf.write("\t\5\2\2\u00d5\u00dd\5\"\22\t\u00d6\u00d7\f\7\2\2\u00d7")
        buf.write("\u00d8\t\6\2\2\u00d8\u00dd\5\"\22\b\u00d9\u00da\f\6\2")
        buf.write("\2\u00da\u00db\t\7\2\2\u00db\u00dd\5\"\22\7\u00dc\u00d0")
        buf.write("\3\2\2\2\u00dc\u00d3\3\2\2\2\u00dc\u00d6\3\2\2\2\u00dc")
        buf.write("\u00d9\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df#\3\2\2\2\u00e0\u00de\3\2\2")
        buf.write("\2\25\'\60\67>LS\\uz\u0085\u008b\u0094\u00a0\u00aa\u00b6")
        buf.write("\u00c2\u00ce\u00dc\u00de")
        return buf.getvalue()


class CPPPParser ( Parser ):

    grammarFileName = "CPPP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'config'", "'generate'", 
                     "'checker'", "'<'", "'>'", "'('", "')'", "','", "'['", 
                     "']'", "';'", "'repeat'", "'assert'", "'='", "'read_user()'", 
                     "'read_ans()'", "'-'", "'*'", "'/'", "'%'", "'+'", 
                     "'>='", "'<='", "'=='", "'!='", "'&&'", "'||'", "'int'", 
                     "'float'", "'double'", "'ll'", "'char'", "'string'", 
                     "'array'", "'print'", "'var'", "'tree'", "'graph'", 
                     "'input'", "'output'", "'tests'", "'test_sol'", "'sol'", 
                     "'range'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "DOUBLE", 
                      "LL", "CHAR", "STRTYPE", "ARRAY", "PRINT", "VAR", 
                      "TREE", "GRAPH", "INPUT", "OUTPUT", "TESTS", "TEST_SOL", 
                      "SOL", "RANGE", "NUMBER", "ID", "STR", "WS" ]

    RULE_program = 0
    RULE_subtaskBlock = 1
    RULE_subtaskName = 2
    RULE_configBlock = 3
    RULE_configItem = 4
    RULE_genBlock = 5
    RULE_checkerBlock = 6
    RULE_primitiveType = 7
    RULE_dataType = 8
    RULE_func = 9
    RULE_var = 10
    RULE_printStmt = 11
    RULE_loopStmt = 12
    RULE_check = 13
    RULE_checkRead = 14
    RULE_option = 15
    RULE_expr = 16

    ruleNames =  [ "program", "subtaskBlock", "subtaskName", "configBlock", 
                   "configItem", "genBlock", "checkerBlock", "primitiveType", 
                   "dataType", "func", "var", "printStmt", "loopStmt", "check", 
                   "checkRead", "option", "expr" ]

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
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    INT=30
    FLOAT=31
    DOUBLE=32
    LL=33
    CHAR=34
    STRTYPE=35
    ARRAY=36
    PRINT=37
    VAR=38
    TREE=39
    GRAPH=40
    INPUT=41
    OUTPUT=42
    TESTS=43
    TEST_SOL=44
    SOL=45
    RANGE=46
    NUMBER=47
    ID=48
    STR=49
    WS=50

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
            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 34
                self.subtaskBlock()
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CPPPParser.ID):
                    break

            self.state = 39
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
            self.state = 41
            self.subtaskName()
            self.state = 42
            self.match(CPPPParser.T__0)
            self.state = 43
            self.configBlock()
            self.state = 44
            self.genBlock()
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPPPParser.T__4:
                self.state = 45
                self.checkerBlock()


            self.state = 48
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
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.match(CPPPParser.ID)
                self.state = 53 
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
            self.state = 55
            self.match(CPPPParser.T__2)
            self.state = 56
            self.match(CPPPParser.T__0)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                self.configItem()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.INPUT) | (1 << CPPPParser.OUTPUT) | (1 << CPPPParser.TESTS) | (1 << CPPPParser.TEST_SOL) | (1 << CPPPParser.SOL))) != 0)):
                    break

            self.state = 62
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INPUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(CPPPParser.INPUT)
                self.state = 65
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.OUTPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(CPPPParser.OUTPUT)
                self.state = 67
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.TESTS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(CPPPParser.TESTS)
                self.state = 69
                self.match(CPPPParser.NUMBER)
                pass
            elif token in [CPPPParser.SOL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(CPPPParser.SOL)
                self.state = 71
                self.match(CPPPParser.STR)
                pass
            elif token in [CPPPParser.TEST_SOL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(CPPPParser.TEST_SOL)
                self.state = 73
                self.match(CPPPParser.STR)
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
            self.state = 76
            self.match(CPPPParser.T__3)
            self.state = 77
            self.match(CPPPParser.T__0)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.func()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__13) | (1 << CPPPParser.PRINT) | (1 << CPPPParser.VAR))) != 0)):
                    break

            self.state = 83
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

        def check(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPPParser.CheckContext)
            else:
                return self.getTypedRuleContext(CPPPParser.CheckContext,i)


        def getRuleIndex(self):
            return CPPPParser.RULE_checkerBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckerBlock" ):
                return visitor.visitCheckerBlock(self)
            else:
                return visitor.visitChildren(self)




    def checkerBlock(self):

        localctx = CPPPParser.CheckerBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_checkerBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(CPPPParser.T__4)
            self.state = 86
            self.match(CPPPParser.T__0)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.T__14 or _la==CPPPParser.VAR:
                self.state = 87
                self.check()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
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
        self.enterRule(localctx, 14, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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
        self.enterRule(localctx, 16, self.RULE_dataType)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.INT, CPPPParser.FLOAT, CPPPParser.DOUBLE, CPPPParser.LL, CPPPParser.CHAR, CPPPParser.STRTYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.primitiveType()
                pass
            elif token in [CPPPParser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
                self.match(CPPPParser.ARRAY)
                self.state = 99
                self.match(CPPPParser.T__5)
                self.state = 100
                self.dataType()
                self.state = 101
                self.match(CPPPParser.T__6)
                pass
            elif token in [CPPPParser.TREE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(CPPPParser.TREE)
                self.state = 104
                self.match(CPPPParser.T__7)
                self.state = 105
                self.expr(0)
                self.state = 106
                self.match(CPPPParser.T__8)
                pass
            elif token in [CPPPParser.GRAPH]:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
                self.match(CPPPParser.GRAPH)
                self.state = 109
                self.match(CPPPParser.T__7)
                self.state = 110
                self.expr(0)
                self.state = 111
                self.match(CPPPParser.T__9)
                self.state = 112
                self.expr(0)
                self.state = 113
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
        self.enterRule(localctx, 18, self.RULE_func)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.var()
                pass
            elif token in [CPPPParser.PRINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.printStmt()
                pass
            elif token in [CPPPParser.T__13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
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
        self.enterRule(localctx, 20, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(CPPPParser.VAR)
            self.state = 123
            self.dataType()
            self.state = 124
            self.match(CPPPParser.ID)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.T__10:
                self.state = 125
                self.match(CPPPParser.T__10)
                self.state = 126
                self.expr(0)
                self.state = 127
                self.match(CPPPParser.T__11)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPPParser.RANGE or _la==CPPPParser.ID:
                self.state = 134
                self.option()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(CPPPParser.T__12)
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
        self.enterRule(localctx, 22, self.RULE_printStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(CPPPParser.PRINT)
            self.state = 144 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 143
                self.expr(0)
                self.state = 146 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__7) | (1 << CPPPParser.T__18) | (1 << CPPPParser.NUMBER) | (1 << CPPPParser.ID) | (1 << CPPPParser.STR))) != 0)):
                    break

            self.state = 148
            self.match(CPPPParser.T__12)
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
        self.enterRule(localctx, 24, self.RULE_loopStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(CPPPParser.T__13)
            self.state = 151
            self.match(CPPPParser.T__7)
            self.state = 152
            self.expr(0)
            self.state = 153
            self.match(CPPPParser.T__8)
            self.state = 154
            self.match(CPPPParser.T__0)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__13) | (1 << CPPPParser.PRINT) | (1 << CPPPParser.VAR))) != 0):
                self.state = 155
                self.func()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(CPPPParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CheckContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CPPPParser.ExprContext,0)


        def STR(self):
            return self.getToken(CPPPParser.STR, 0)

        def VAR(self):
            return self.getToken(CPPPParser.VAR, 0)

        def dataType(self):
            return self.getTypedRuleContext(CPPPParser.DataTypeContext,0)


        def ID(self):
            return self.getToken(CPPPParser.ID, 0)

        def checkRead(self):
            return self.getTypedRuleContext(CPPPParser.CheckReadContext,0)


        def getRuleIndex(self):
            return CPPPParser.RULE_check

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheck" ):
                return visitor.visitCheck(self)
            else:
                return visitor.visitChildren(self)




    def check(self):

        localctx = CPPPParser.CheckContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_check)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(CPPPParser.T__14)
                self.state = 164
                self.match(CPPPParser.T__7)
                self.state = 165
                self.expr(0)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CPPPParser.T__9:
                    self.state = 166
                    self.match(CPPPParser.T__9)
                    self.state = 167
                    self.match(CPPPParser.STR)


                self.state = 170
                self.match(CPPPParser.T__8)
                self.state = 171
                self.match(CPPPParser.T__12)
                pass
            elif token in [CPPPParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(CPPPParser.VAR)
                self.state = 174
                self.dataType()
                self.state = 175
                self.match(CPPPParser.ID)
                self.state = 176
                self.match(CPPPParser.T__15)
                self.state = 177
                self.checkRead()
                self.state = 178
                self.match(CPPPParser.T__12)
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


    class CheckReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPPPParser.RULE_checkRead

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCheckRead" ):
                return visitor.visitCheckRead(self)
            else:
                return visitor.visitChildren(self)




    def checkRead(self):

        localctx = CPPPParser.CheckReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_checkRead)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==CPPPParser.T__16 or _la==CPPPParser.T__17):
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
        self.enterRule(localctx, 30, self.RULE_option)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(CPPPParser.ID)
                pass
            elif token in [CPPPParser.RANGE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(CPPPParser.RANGE)
                self.state = 186
                self.match(CPPPParser.T__7)
                self.state = 187
                self.expr(0)
                self.state = 188
                self.match(CPPPParser.T__9)
                self.state = 189
                self.expr(0)
                self.state = 190
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPPParser.T__18]:
                self.state = 195
                self.match(CPPPParser.T__18)
                self.state = 196
                self.expr(9)
                pass
            elif token in [CPPPParser.T__7]:
                self.state = 197
                self.match(CPPPParser.T__7)
                self.state = 198
                self.expr(0)
                self.state = 199
                self.match(CPPPParser.T__8)
                pass
            elif token in [CPPPParser.ID]:
                self.state = 201
                self.match(CPPPParser.ID)
                pass
            elif token in [CPPPParser.NUMBER]:
                self.state = 202
                self.match(CPPPParser.NUMBER)
                pass
            elif token in [CPPPParser.STR]:
                self.state = 203
                self.match(CPPPParser.STR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 218
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 207
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__19) | (1 << CPPPParser.T__20) | (1 << CPPPParser.T__21))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 208
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 209
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 210
                        _la = self._input.LA(1)
                        if not(_la==CPPPParser.T__18 or _la==CPPPParser.T__22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 211
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 212
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 213
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPPParser.T__5) | (1 << CPPPParser.T__6) | (1 << CPPPParser.T__23) | (1 << CPPPParser.T__24) | (1 << CPPPParser.T__25) | (1 << CPPPParser.T__26))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 214
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = CPPPParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 215
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 216
                        _la = self._input.LA(1)
                        if not(_la==CPPPParser.T__27 or _la==CPPPParser.T__28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 217
                        self.expr(5)
                        pass

             
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self._predicates[16] = self.expr_sempred
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
         




