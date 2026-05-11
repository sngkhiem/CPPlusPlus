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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u012d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3")
        buf.write("+\3+\3+\3+\3+\3,\6,\u0111\n,\r,\16,\u0112\3-\3-\7-\u0117")
        buf.write("\n-\f-\16-\u011a\13-\3.\3.\3.\3.\7.\u0120\n.\f.\16.\u0123")
        buf.write("\13.\3.\3.\3/\6/\u0128\n/\r/\16/\u0129\3/\3/\2\2\60\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60\3\2\7\3\2\62;\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\4\2$$^^\5\2\13\f\17\17\"\"\2\u0131\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W")
        buf.write("\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5")
        buf.write("a\3\2\2\2\7c\3\2\2\2\tj\3\2\2\2\13s\3\2\2\2\ru\3\2\2\2")
        buf.write("\17w\3\2\2\2\21y\3\2\2\2\23{\3\2\2\2\25}\3\2\2\2\27\177")
        buf.write("\3\2\2\2\31\u0081\3\2\2\2\33\u0083\3\2\2\2\35\u008a\3")
        buf.write("\2\2\2\37\u008c\3\2\2\2!\u008e\3\2\2\2#\u0090\3\2\2\2")
        buf.write("%\u0092\3\2\2\2\'\u0094\3\2\2\2)\u0097\3\2\2\2+\u009a")
        buf.write("\3\2\2\2-\u009d\3\2\2\2/\u00a0\3\2\2\2\61\u00a3\3\2\2")
        buf.write("\2\63\u00a6\3\2\2\2\65\u00aa\3\2\2\2\67\u00b0\3\2\2\2")
        buf.write("9\u00b7\3\2\2\2;\u00ba\3\2\2\2=\u00bf\3\2\2\2?\u00c6\3")
        buf.write("\2\2\2A\u00cc\3\2\2\2C\u00d2\3\2\2\2E\u00d6\3\2\2\2G\u00db")
        buf.write("\3\2\2\2I\u00e1\3\2\2\2K\u00e7\3\2\2\2M\u00ee\3\2\2\2")
        buf.write("O\u00f4\3\2\2\2Q\u00fd\3\2\2\2S\u0101\3\2\2\2U\u0109\3")
        buf.write("\2\2\2W\u0110\3\2\2\2Y\u0114\3\2\2\2[\u011b\3\2\2\2]\u0127")
        buf.write("\3\2\2\2_`\7}\2\2`\4\3\2\2\2ab\7\177\2\2b\6\3\2\2\2cd")
        buf.write("\7e\2\2de\7q\2\2ef\7p\2\2fg\7h\2\2gh\7k\2\2hi\7i\2\2i")
        buf.write("\b\3\2\2\2jk\7i\2\2kl\7g\2\2lm\7p\2\2mn\7g\2\2no\7t\2")
        buf.write("\2op\7c\2\2pq\7v\2\2qr\7g\2\2r\n\3\2\2\2st\7>\2\2t\f\3")
        buf.write("\2\2\2uv\7@\2\2v\16\3\2\2\2wx\7*\2\2x\20\3\2\2\2yz\7+")
        buf.write("\2\2z\22\3\2\2\2{|\7.\2\2|\24\3\2\2\2}~\7]\2\2~\26\3\2")
        buf.write("\2\2\177\u0080\7_\2\2\u0080\30\3\2\2\2\u0081\u0082\7=")
        buf.write("\2\2\u0082\32\3\2\2\2\u0083\u0084\7t\2\2\u0084\u0085\7")
        buf.write("g\2\2\u0085\u0086\7r\2\2\u0086\u0087\7g\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7v\2\2\u0089\34\3\2\2\2\u008a\u008b")
        buf.write("\7/\2\2\u008b\36\3\2\2\2\u008c\u008d\7,\2\2\u008d \3\2")
        buf.write("\2\2\u008e\u008f\7\61\2\2\u008f\"\3\2\2\2\u0090\u0091")
        buf.write("\7\'\2\2\u0091$\3\2\2\2\u0092\u0093\7-\2\2\u0093&\3\2")
        buf.write("\2\2\u0094\u0095\7@\2\2\u0095\u0096\7?\2\2\u0096(\3\2")
        buf.write("\2\2\u0097\u0098\7>\2\2\u0098\u0099\7?\2\2\u0099*\3\2")
        buf.write("\2\2\u009a\u009b\7?\2\2\u009b\u009c\7?\2\2\u009c,\3\2")
        buf.write("\2\2\u009d\u009e\7#\2\2\u009e\u009f\7?\2\2\u009f.\3\2")
        buf.write("\2\2\u00a0\u00a1\7(\2\2\u00a1\u00a2\7(\2\2\u00a2\60\3")
        buf.write("\2\2\2\u00a3\u00a4\7~\2\2\u00a4\u00a5\7~\2\2\u00a5\62")
        buf.write("\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9")
        buf.write("\7v\2\2\u00a9\64\3\2\2\2\u00aa\u00ab\7h\2\2\u00ab\u00ac")
        buf.write("\7n\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af")
        buf.write("\7v\2\2\u00af\66\3\2\2\2\u00b0\u00b1\7f\2\2\u00b1\u00b2")
        buf.write("\7q\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7d\2\2\u00b4\u00b5")
        buf.write("\7n\2\2\u00b5\u00b6\7g\2\2\u00b68\3\2\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7n\2\2\u00b9:\3\2\2\2\u00ba\u00bb")
        buf.write("\7e\2\2\u00bb\u00bc\7j\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be<\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7v\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4")
        buf.write("\7p\2\2\u00c4\u00c5\7i\2\2\u00c5>\3\2\2\2\u00c6\u00c7")
        buf.write("\7c\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca")
        buf.write("\7c\2\2\u00ca\u00cb\7{\2\2\u00cb@\3\2\2\2\u00cc\u00cd")
        buf.write("\7r\2\2\u00cd\u00ce\7t\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7v\2\2\u00d1B\3\2\2\2\u00d2\u00d3")
        buf.write("\7x\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7t\2\2\u00d5D\3")
        buf.write("\2\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7g\2\2\u00daF\3\2\2\2\u00db\u00dc")
        buf.write("\7i\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de\7c\2\2\u00de\u00df")
        buf.write("\7r\2\2\u00df\u00e0\7j\2\2\u00e0H\3\2\2\2\u00e1\u00e2")
        buf.write("\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7r\2\2\u00e4\u00e5")
        buf.write("\7w\2\2\u00e5\u00e6\7v\2\2\u00e6J\3\2\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7r\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7v\2\2\u00edL\3")
        buf.write("\2\2\2\u00ee\u00ef\7v\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1")
        buf.write("\7u\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7u\2\2\u00f3N\3")
        buf.write("\2\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7u\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7a\2\2\u00f9\u00fa")
        buf.write("\7u\2\2\u00fa\u00fb\7q\2\2\u00fb\u00fc\7n\2\2\u00fcP\3")
        buf.write("\2\2\2\u00fd\u00fe\7u\2\2\u00fe\u00ff\7q\2\2\u00ff\u0100")
        buf.write("\7n\2\2\u0100R\3\2\2\2\u0101\u0102\7e\2\2\u0102\u0103")
        buf.write("\7q\2\2\u0103\u0104\7o\2\2\u0104\u0105\7r\2\2\u0105\u0106")
        buf.write("\7c\2\2\u0106\u0107\7t\2\2\u0107\u0108\7g\2\2\u0108T\3")
        buf.write("\2\2\2\u0109\u010a\7t\2\2\u010a\u010b\7c\2\2\u010b\u010c")
        buf.write("\7p\2\2\u010c\u010d\7i\2\2\u010d\u010e\7g\2\2\u010eV\3")
        buf.write("\2\2\2\u010f\u0111\t\2\2\2\u0110\u010f\3\2\2\2\u0111\u0112")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("X\3\2\2\2\u0114\u0118\t\3\2\2\u0115\u0117\t\4\2\2\u0116")
        buf.write("\u0115\3\2\2\2\u0117\u011a\3\2\2\2\u0118\u0116\3\2\2\2")
        buf.write("\u0118\u0119\3\2\2\2\u0119Z\3\2\2\2\u011a\u0118\3\2\2")
        buf.write("\2\u011b\u0121\7$\2\2\u011c\u0120\n\5\2\2\u011d\u011e")
        buf.write("\7^\2\2\u011e\u0120\13\2\2\2\u011f\u011c\3\2\2\2\u011f")
        buf.write("\u011d\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f\3\2\2\2")
        buf.write("\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123\u0121\3")
        buf.write("\2\2\2\u0124\u0125\7$\2\2\u0125\\\3\2\2\2\u0126\u0128")
        buf.write("\t\6\2\2\u0127\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129")
        buf.write("\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\b/\2\2\u012c^\3\2\2\2\b\2\u0112\u0118\u011f")
        buf.write("\u0121\u0129\3\b\2\2")
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
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    INT = 25
    FLOAT = 26
    DOUBLE = 27
    LL = 28
    CHAR = 29
    STRTYPE = 30
    ARRAY = 31
    PRINT = 32
    VAR = 33
    TREE = 34
    GRAPH = 35
    INPUT = 36
    OUTPUT = 37
    TESTS = 38
    TEST_SOL = 39
    SOL = 40
    COMPARE = 41
    RANGE = 42
    NUMBER = 43
    ID = 44
    STR = 45
    WS = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{'", "'}'", "'config'", "'generate'", "'<'", "'>'", "'('", 
            "')'", "','", "'['", "']'", "';'", "'repeat'", "'-'", "'*'", 
            "'/'", "'%'", "'+'", "'>='", "'<='", "'=='", "'!='", "'&&'", 
            "'||'", "'int'", "'float'", "'double'", "'ll'", "'char'", "'string'", 
            "'array'", "'print'", "'var'", "'tree'", "'graph'", "'input'", 
            "'output'", "'tests'", "'test_sol'", "'sol'", "'compare'", "'range'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "DOUBLE", "LL", "CHAR", "STRTYPE", "ARRAY", 
            "PRINT", "VAR", "TREE", "GRAPH", "INPUT", "OUTPUT", "TESTS", 
            "TEST_SOL", "SOL", "COMPARE", "RANGE", "NUMBER", "ID", "STR", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "INT", "FLOAT", "DOUBLE", 
                  "LL", "CHAR", "STRTYPE", "ARRAY", "PRINT", "VAR", "TREE", 
                  "GRAPH", "INPUT", "OUTPUT", "TESTS", "TEST_SOL", "SOL", 
                  "COMPARE", "RANGE", "NUMBER", "ID", "STR", "WS" ]

    grammarFileName = "CPPP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


