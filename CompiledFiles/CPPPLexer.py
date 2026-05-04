# Generated from ./grammar/CPPP.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u009d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\6\24\u0081\n\24\r\24\16")
        buf.write("\24\u0082\3\25\3\25\7\25\u0087\n\25\f\25\16\25\u008a\13")
        buf.write("\25\3\26\3\26\3\26\3\26\7\26\u0090\n\26\f\26\16\26\u0093")
        buf.write("\13\26\3\26\3\26\3\27\6\27\u0098\n\27\r\27\16\27\u0099")
        buf.write("\3\27\3\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30\3\2\7\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\4")
        buf.write("\2$$^^\5\2\13\f\17\17\"\"\2\u00a1\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\3/\3\2\2\2\5\61\3\2")
        buf.write("\2\2\7\63\3\2\2\2\t:\3\2\2\2\13C\3\2\2\2\rK\3\2\2\2\17")
        buf.write("M\3\2\2\2\21O\3\2\2\2\23S\3\2\2\2\25U\3\2\2\2\27W\3\2")
        buf.write("\2\2\31Y\3\2\2\2\33]\3\2\2\2\35c\3\2\2\2\37j\3\2\2\2!")
        buf.write("m\3\2\2\2#r\3\2\2\2%y\3\2\2\2\'\u0080\3\2\2\2)\u0084\3")
        buf.write("\2\2\2+\u008b\3\2\2\2-\u0097\3\2\2\2/\60\7}\2\2\60\4\3")
        buf.write("\2\2\2\61\62\7\177\2\2\62\6\3\2\2\2\63\64\7e\2\2\64\65")
        buf.write("\7q\2\2\65\66\7p\2\2\66\67\7h\2\2\678\7k\2\289\7i\2\2")
        buf.write("9\b\3\2\2\2:;\7i\2\2;<\7g\2\2<=\7p\2\2=>\7g\2\2>?\7t\2")
        buf.write("\2?@\7c\2\2@A\7v\2\2AB\7g\2\2B\n\3\2\2\2CD\7e\2\2DE\7")
        buf.write("j\2\2EF\7g\2\2FG\7e\2\2GH\7m\2\2HI\7g\2\2IJ\7t\2\2J\f")
        buf.write("\3\2\2\2KL\7>\2\2L\16\3\2\2\2MN\7@\2\2N\20\3\2\2\2OP\7")
        buf.write("x\2\2PQ\7c\2\2QR\7t\2\2R\22\3\2\2\2ST\7]\2\2T\24\3\2\2")
        buf.write("\2UV\7_\2\2V\26\3\2\2\2WX\7=\2\2X\30\3\2\2\2YZ\7k\2\2")
        buf.write("Z[\7p\2\2[\\\7v\2\2\\\32\3\2\2\2]^\7h\2\2^_\7n\2\2_`\7")
        buf.write("q\2\2`a\7c\2\2ab\7v\2\2b\34\3\2\2\2cd\7f\2\2de\7q\2\2")
        buf.write("ef\7w\2\2fg\7d\2\2gh\7n\2\2hi\7g\2\2i\36\3\2\2\2jk\7n")
        buf.write("\2\2kl\7n\2\2l \3\2\2\2mn\7e\2\2no\7j\2\2op\7c\2\2pq\7")
        buf.write("t\2\2q\"\3\2\2\2rs\7u\2\2st\7v\2\2tu\7t\2\2uv\7k\2\2v")
        buf.write("w\7p\2\2wx\7i\2\2x$\3\2\2\2yz\7c\2\2z{\7t\2\2{|\7t\2\2")
        buf.write("|}\7c\2\2}~\7{\2\2~&\3\2\2\2\177\u0081\t\2\2\2\u0080\177")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083(\3\2\2\2\u0084\u0088\t\3\2\2\u0085")
        buf.write("\u0087\t\4\2\2\u0086\u0085\3\2\2\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089*\3\2\2")
        buf.write("\2\u008a\u0088\3\2\2\2\u008b\u0091\7$\2\2\u008c\u0090")
        buf.write("\n\5\2\2\u008d\u008e\7^\2\2\u008e\u0090\13\2\2\2\u008f")
        buf.write("\u008c\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0093\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\3")
        buf.write("\2\2\2\u0093\u0091\3\2\2\2\u0094\u0095\7$\2\2\u0095,\3")
        buf.write("\2\2\2\u0096\u0098\t\6\2\2\u0097\u0096\3\2\2\2\u0098\u0099")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a")
        buf.write("\u009b\3\2\2\2\u009b\u009c\b\27\2\2\u009c.\3\2\2\2\b\2")
        buf.write("\u0082\u0088\u008f\u0091\u0099\3\b\2\2")
        return buf.getvalue()


class CPPPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    INT = 12
    FLOAT = 13
    DOUBLE = 14
    LL = 15
    CHAR = 16
    STRTYPE = 17
    ARRAY = 18
    NUMBER = 19
    ID = 20
    STR = 21
    WS = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'config'", "'generate'", "'checker'", "'<'", 
            "'>'", "'var'", "'['", "']'", "';'", "'int'", "'float'", "'double'", 
            "'ll'", "'char'", "'string'", "'array'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "DOUBLE", "LL", "CHAR", "STRTYPE", "ARRAY", 
            "NUMBER", "ID", "STR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "INT", "FLOAT", "DOUBLE", 
                  "LL", "CHAR", "STRTYPE", "ARRAY", "NUMBER", "ID", "STR", 
                  "WS" ]

    grammarFileName = "CPPP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


