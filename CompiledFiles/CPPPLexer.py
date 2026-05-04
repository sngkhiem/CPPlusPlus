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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2!")
        buf.write("\u00e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u00ba\n\34\f")
        buf.write("\34\16\34\u00bd\13\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\6\35\u00c6\n\35\r\35\16\35\u00c7\3\36\3\36\7\36\u00cc")
        buf.write("\n\36\f\36\16\36\u00cf\13\36\3\37\3\37\3\37\3\37\7\37")
        buf.write("\u00d5\n\37\f\37\16\37\u00d8\13\37\3\37\3\37\3 \6 \u00dd")
        buf.write("\n \r \16 \u00de\3 \3 \2\2!\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!\3\2\b\6\2\f\f\17\17$$^^\3\2\62;\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\4\2$$^^\5\2\13\f\17\17\"\"\2\u00e8\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\3A\3")
        buf.write("\2\2\2\5C\3\2\2\2\7E\3\2\2\2\tL\3\2\2\2\13U\3\2\2\2\r")
        buf.write("]\3\2\2\2\17_\3\2\2\2\21a\3\2\2\2\23c\3\2\2\2\25e\3\2")
        buf.write("\2\2\27g\3\2\2\2\31i\3\2\2\2\33k\3\2\2\2\35m\3\2\2\2\37")
        buf.write("q\3\2\2\2!w\3\2\2\2#~\3\2\2\2%\u0081\3\2\2\2\'\u0086\3")
        buf.write("\2\2\2)\u008d\3\2\2\2+\u0093\3\2\2\2-\u0099\3\2\2\2/\u009d")
        buf.write("\3\2\2\2\61\u00a2\3\2\2\2\63\u00a8\3\2\2\2\65\u00ae\3")
        buf.write("\2\2\2\67\u00b5\3\2\2\29\u00c5\3\2\2\2;\u00c9\3\2\2\2")
        buf.write("=\u00d0\3\2\2\2?\u00dc\3\2\2\2AB\7}\2\2B\4\3\2\2\2CD\7")
        buf.write("\177\2\2D\6\3\2\2\2EF\7e\2\2FG\7q\2\2GH\7p\2\2HI\7h\2")
        buf.write("\2IJ\7k\2\2JK\7i\2\2K\b\3\2\2\2LM\7i\2\2MN\7g\2\2NO\7")
        buf.write("p\2\2OP\7g\2\2PQ\7t\2\2QR\7c\2\2RS\7v\2\2ST\7g\2\2T\n")
        buf.write("\3\2\2\2UV\7e\2\2VW\7j\2\2WX\7g\2\2XY\7e\2\2YZ\7m\2\2")
        buf.write("Z[\7g\2\2[\\\7t\2\2\\\f\3\2\2\2]^\7>\2\2^\16\3\2\2\2_")
        buf.write("`\7@\2\2`\20\3\2\2\2ab\7*\2\2b\22\3\2\2\2cd\7+\2\2d\24")
        buf.write("\3\2\2\2ef\7.\2\2f\26\3\2\2\2gh\7]\2\2h\30\3\2\2\2ij\7")
        buf.write("_\2\2j\32\3\2\2\2kl\7=\2\2l\34\3\2\2\2mn\7k\2\2no\7p\2")
        buf.write("\2op\7v\2\2p\36\3\2\2\2qr\7h\2\2rs\7n\2\2st\7q\2\2tu\7")
        buf.write("c\2\2uv\7v\2\2v \3\2\2\2wx\7f\2\2xy\7q\2\2yz\7w\2\2z{")
        buf.write("\7d\2\2{|\7n\2\2|}\7g\2\2}\"\3\2\2\2~\177\7n\2\2\177\u0080")
        buf.write("\7n\2\2\u0080$\3\2\2\2\u0081\u0082\7e\2\2\u0082\u0083")
        buf.write("\7j\2\2\u0083\u0084\7c\2\2\u0084\u0085\7t\2\2\u0085&\3")
        buf.write("\2\2\2\u0086\u0087\7u\2\2\u0087\u0088\7v\2\2\u0088\u0089")
        buf.write("\7t\2\2\u0089\u008a\7k\2\2\u008a\u008b\7p\2\2\u008b\u008c")
        buf.write("\7i\2\2\u008c(\3\2\2\2\u008d\u008e\7c\2\2\u008e\u008f")
        buf.write("\7t\2\2\u008f\u0090\7t\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7{\2\2\u0092*\3\2\2\2\u0093\u0094\7r\2\2\u0094\u0095")
        buf.write("\7t\2\2\u0095\u0096\7k\2\2\u0096\u0097\7p\2\2\u0097\u0098")
        buf.write("\7v\2\2\u0098,\3\2\2\2\u0099\u009a\7x\2\2\u009a\u009b")
        buf.write("\7c\2\2\u009b\u009c\7t\2\2\u009c.\3\2\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7t\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1")
        buf.write("\7g\2\2\u00a1\60\3\2\2\2\u00a2\u00a3\7i\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7")
        buf.write("\7j\2\2\u00a7\62\3\2\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7r\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\64\3\2\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7w\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7r\2\2\u00b2\u00b3")
        buf.write("\7w\2\2\u00b3\u00b4\7v\2\2\u00b4\66\3\2\2\2\u00b5\u00bb")
        buf.write("\7$\2\2\u00b6\u00ba\n\2\2\2\u00b7\u00b8\7^\2\2\u00b8\u00ba")
        buf.write("\13\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba")
        buf.write("\u00bd\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00be\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\7")
        buf.write("\60\2\2\u00bf\u00c0\7e\2\2\u00c0\u00c1\7r\2\2\u00c1\u00c2")
        buf.write("\7r\2\2\u00c2\u00c3\7$\2\2\u00c38\3\2\2\2\u00c4\u00c6")
        buf.write("\t\3\2\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8:\3\2\2\2\u00c9")
        buf.write("\u00cd\t\4\2\2\u00ca\u00cc\t\5\2\2\u00cb\u00ca\3\2\2\2")
        buf.write("\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3")
        buf.write("\2\2\2\u00ce<\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d6")
        buf.write("\7$\2\2\u00d1\u00d5\n\6\2\2\u00d2\u00d3\7^\2\2\u00d3\u00d5")
        buf.write("\13\2\2\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7\u00d9\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00da\7")
        buf.write("$\2\2\u00da>\3\2\2\2\u00db\u00dd\t\7\2\2\u00dc\u00db\3")
        buf.write("\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\b \2\2\u00e1")
        buf.write("@\3\2\2\2\n\2\u00b9\u00bb\u00c7\u00cd\u00d4\u00d6\u00de")
        buf.write("\3\b\2\2")
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
    T__11 = 12
    T__12 = 13
    INT = 14
    FLOAT = 15
    DOUBLE = 16
    LL = 17
    CHAR = 18
    STRTYPE = 19
    ARRAY = 20
    PRINT = 21
    VAR = 22
    TREE = 23
    GRAPH = 24
    INPUT = 25
    OUTPUT = 26
    CPP_FILE = 27
    NUMBER = 28
    ID = 29
    STR = 30
    WS = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'config'", "'generate'", "'checker'", "'<'", 
            "'>'", "'('", "')'", "','", "'['", "']'", "';'", "'int'", "'float'", 
            "'double'", "'ll'", "'char'", "'string'", "'array'", "'print'", 
            "'var'", "'tree'", "'graph'", "'input'", "'output'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "DOUBLE", "LL", "CHAR", "STRTYPE", "ARRAY", 
            "PRINT", "VAR", "TREE", "GRAPH", "INPUT", "OUTPUT", "CPP_FILE", 
            "NUMBER", "ID", "STR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "INT", 
                  "FLOAT", "DOUBLE", "LL", "CHAR", "STRTYPE", "ARRAY", "PRINT", 
                  "VAR", "TREE", "GRAPH", "INPUT", "OUTPUT", "CPP_FILE", 
                  "NUMBER", "ID", "STR", "WS" ]

    grammarFileName = "CPPP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


