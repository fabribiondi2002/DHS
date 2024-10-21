# Generated from /home/fabri/Escritorio/DHS/proyecto/DHS/src/main/python/primerproyecto/compiladores.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,325,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,1,1,1,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,
        2,5,2,82,8,2,10,2,12,2,85,9,2,1,2,1,2,1,3,1,3,3,3,91,8,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,3,4,100,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,
        109,8,5,1,6,1,6,1,6,1,6,1,6,3,6,116,8,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,3,7,127,8,7,1,8,1,8,1,8,1,8,1,8,3,8,134,8,8,1,9,1,9,
        1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,145,8,10,1,11,1,11,1,11,1,11,
        1,11,3,11,152,8,11,1,12,1,12,1,12,1,12,3,12,158,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,3,13,168,8,13,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,3,14,177,8,14,1,15,1,15,1,15,1,15,3,15,183,8,15,1,15,
        1,15,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,197,
        8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,20,207,8,20,1,21,
        1,21,1,21,1,21,1,21,3,21,214,8,21,1,22,1,22,1,22,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,3,23,228,8,23,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,
        246,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,255,8,26,1,27,1,
        27,1,27,1,27,1,27,1,27,3,27,263,8,27,1,28,1,28,1,28,1,28,1,29,1,
        29,1,29,1,29,1,29,1,29,3,29,275,8,29,1,30,1,30,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,3,30,287,8,30,1,31,1,31,1,31,1,31,3,31,293,
        8,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,31,304,8,31,
        3,31,306,8,31,1,32,1,32,1,33,1,33,1,33,1,33,1,34,1,34,1,34,3,34,
        317,8,34,1,34,1,34,1,34,1,34,1,34,1,34,1,34,0,0,35,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,0,3,1,0,16,21,1,0,23,27,2,0,22,22,35,35,329,
        0,70,1,0,0,0,2,72,1,0,0,0,4,77,1,0,0,0,6,90,1,0,0,0,8,92,1,0,0,0,
        10,101,1,0,0,0,12,110,1,0,0,0,14,126,1,0,0,0,16,133,1,0,0,0,18,135,
        1,0,0,0,20,144,1,0,0,0,22,151,1,0,0,0,24,157,1,0,0,0,26,167,1,0,
        0,0,28,176,1,0,0,0,30,178,1,0,0,0,32,186,1,0,0,0,34,188,1,0,0,0,
        36,196,1,0,0,0,38,198,1,0,0,0,40,206,1,0,0,0,42,213,1,0,0,0,44,215,
        1,0,0,0,46,227,1,0,0,0,48,229,1,0,0,0,50,245,1,0,0,0,52,254,1,0,
        0,0,54,256,1,0,0,0,56,264,1,0,0,0,58,268,1,0,0,0,60,276,1,0,0,0,
        62,305,1,0,0,0,64,307,1,0,0,0,66,309,1,0,0,0,68,313,1,0,0,0,70,71,
        7,0,0,0,71,1,1,0,0,0,72,73,7,1,0,0,73,3,1,0,0,0,74,76,3,28,14,0,
        75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,83,1,
        0,0,0,79,77,1,0,0,0,80,82,3,6,3,0,81,80,1,0,0,0,82,85,1,0,0,0,83,
        81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,0,0,
        1,87,5,1,0,0,0,88,91,3,8,4,0,89,91,3,10,5,0,90,88,1,0,0,0,90,89,
        1,0,0,0,91,7,1,0,0,0,92,93,5,28,0,0,93,94,5,35,0,0,94,95,5,1,0,0,
        95,96,3,14,7,0,96,99,5,2,0,0,97,100,3,56,28,0,98,100,5,5,0,0,99,
        97,1,0,0,0,99,98,1,0,0,0,100,9,1,0,0,0,101,102,3,2,1,0,102,103,5,
        35,0,0,103,104,5,1,0,0,104,105,3,14,7,0,105,108,5,2,0,0,106,109,
        3,12,6,0,107,109,5,5,0,0,108,106,1,0,0,0,108,107,1,0,0,0,109,11,
        1,0,0,0,110,115,5,3,0,0,111,112,3,24,12,0,112,113,5,33,0,0,113,116,
        1,0,0,0,114,116,5,33,0,0,115,111,1,0,0,0,115,114,1,0,0,0,116,117,
        1,0,0,0,117,118,3,32,16,0,118,119,5,5,0,0,119,120,5,4,0,0,120,13,
        1,0,0,0,121,122,3,2,1,0,122,123,5,35,0,0,123,124,3,16,8,0,124,127,
        1,0,0,0,125,127,1,0,0,0,126,121,1,0,0,0,126,125,1,0,0,0,127,15,1,
        0,0,0,128,129,5,7,0,0,129,130,3,14,7,0,130,131,3,16,8,0,131,134,
        1,0,0,0,132,134,1,0,0,0,133,128,1,0,0,0,133,132,1,0,0,0,134,17,1,
        0,0,0,135,136,5,35,0,0,136,137,5,1,0,0,137,138,3,20,10,0,138,139,
        5,2,0,0,139,19,1,0,0,0,140,141,3,32,16,0,141,142,3,22,11,0,142,145,
        1,0,0,0,143,145,1,0,0,0,144,140,1,0,0,0,144,143,1,0,0,0,145,21,1,
        0,0,0,146,147,5,7,0,0,147,148,3,20,10,0,148,149,3,22,11,0,149,152,
        1,0,0,0,150,152,1,0,0,0,151,146,1,0,0,0,151,150,1,0,0,0,152,23,1,
        0,0,0,153,154,3,26,13,0,154,155,3,24,12,0,155,158,1,0,0,0,156,158,
        1,0,0,0,157,153,1,0,0,0,157,156,1,0,0,0,158,25,1,0,0,0,159,168,3,
        28,14,0,160,168,3,54,27,0,161,168,3,60,30,0,162,168,3,58,29,0,163,
        168,3,56,28,0,164,168,3,30,15,0,165,168,3,18,9,0,166,168,5,5,0,0,
        167,159,1,0,0,0,167,160,1,0,0,0,167,161,1,0,0,0,167,162,1,0,0,0,
        167,163,1,0,0,0,167,164,1,0,0,0,167,165,1,0,0,0,167,166,1,0,0,0,
        168,27,1,0,0,0,169,170,3,2,1,0,170,171,5,35,0,0,171,172,5,5,0,0,
        172,177,1,0,0,0,173,174,3,2,1,0,174,175,3,30,15,0,175,177,1,0,0,
        0,176,169,1,0,0,0,176,173,1,0,0,0,177,29,1,0,0,0,178,179,5,35,0,
        0,179,182,5,13,0,0,180,183,3,18,9,0,181,183,3,32,16,0,182,180,1,
        0,0,0,182,181,1,0,0,0,183,184,1,0,0,0,184,185,5,5,0,0,185,31,1,0,
        0,0,186,187,3,34,17,0,187,33,1,0,0,0,188,189,3,38,19,0,189,190,3,
        36,18,0,190,35,1,0,0,0,191,192,5,15,0,0,192,193,3,38,19,0,193,194,
        3,36,18,0,194,197,1,0,0,0,195,197,1,0,0,0,196,191,1,0,0,0,196,195,
        1,0,0,0,197,37,1,0,0,0,198,199,3,42,21,0,199,200,3,40,20,0,200,39,
        1,0,0,0,201,202,5,14,0,0,202,203,3,42,21,0,203,204,3,40,20,0,204,
        207,1,0,0,0,205,207,1,0,0,0,206,201,1,0,0,0,206,205,1,0,0,0,207,
        41,1,0,0,0,208,209,3,44,22,0,209,210,3,0,0,0,210,211,3,44,22,0,211,
        214,1,0,0,0,212,214,3,44,22,0,213,208,1,0,0,0,213,212,1,0,0,0,214,
        43,1,0,0,0,215,216,3,48,24,0,216,217,3,46,23,0,217,45,1,0,0,0,218,
        219,5,8,0,0,219,220,3,48,24,0,220,221,3,46,23,0,221,228,1,0,0,0,
        222,223,5,9,0,0,223,224,3,48,24,0,224,225,3,46,23,0,225,228,1,0,
        0,0,226,228,1,0,0,0,227,218,1,0,0,0,227,222,1,0,0,0,227,226,1,0,
        0,0,228,47,1,0,0,0,229,230,3,52,26,0,230,231,3,50,25,0,231,49,1,
        0,0,0,232,233,5,10,0,0,233,234,3,52,26,0,234,235,3,50,25,0,235,246,
        1,0,0,0,236,237,5,11,0,0,237,238,3,52,26,0,238,239,3,50,25,0,239,
        246,1,0,0,0,240,241,5,12,0,0,241,242,3,52,26,0,242,243,3,50,25,0,
        243,246,1,0,0,0,244,246,1,0,0,0,245,232,1,0,0,0,245,236,1,0,0,0,
        245,240,1,0,0,0,245,244,1,0,0,0,246,51,1,0,0,0,247,255,5,22,0,0,
        248,255,5,35,0,0,249,255,3,18,9,0,250,251,5,1,0,0,251,252,3,44,22,
        0,252,253,5,2,0,0,253,255,1,0,0,0,254,247,1,0,0,0,254,248,1,0,0,
        0,254,249,1,0,0,0,254,250,1,0,0,0,255,53,1,0,0,0,256,257,5,29,0,
        0,257,258,5,1,0,0,258,259,3,64,32,0,259,262,5,2,0,0,260,263,3,56,
        28,0,261,263,3,26,13,0,262,260,1,0,0,0,262,261,1,0,0,0,263,55,1,
        0,0,0,264,265,5,3,0,0,265,266,3,24,12,0,266,267,5,4,0,0,267,57,1,
        0,0,0,268,269,5,31,0,0,269,270,5,1,0,0,270,271,3,64,32,0,271,274,
        5,2,0,0,272,275,3,56,28,0,273,275,3,26,13,0,274,272,1,0,0,0,274,
        273,1,0,0,0,275,59,1,0,0,0,276,277,5,30,0,0,277,278,5,1,0,0,278,
        279,3,62,31,0,279,280,5,5,0,0,280,281,3,64,32,0,281,282,5,5,0,0,
        282,283,3,66,33,0,283,286,5,2,0,0,284,287,3,56,28,0,285,287,3,26,
        13,0,286,284,1,0,0,0,286,285,1,0,0,0,287,61,1,0,0,0,288,289,5,35,
        0,0,289,292,5,13,0,0,290,293,3,18,9,0,291,293,3,32,16,0,292,290,
        1,0,0,0,292,291,1,0,0,0,293,306,1,0,0,0,294,306,5,35,0,0,295,296,
        3,2,1,0,296,297,5,35,0,0,297,306,1,0,0,0,298,299,3,2,1,0,299,300,
        5,35,0,0,300,303,5,13,0,0,301,304,3,18,9,0,302,304,3,32,16,0,303,
        301,1,0,0,0,303,302,1,0,0,0,304,306,1,0,0,0,305,288,1,0,0,0,305,
        294,1,0,0,0,305,295,1,0,0,0,305,298,1,0,0,0,306,63,1,0,0,0,307,308,
        3,32,16,0,308,65,1,0,0,0,309,310,7,2,0,0,310,311,5,13,0,0,311,312,
        3,44,22,0,312,67,1,0,0,0,313,316,5,34,0,0,314,317,3,56,28,0,315,
        317,3,26,13,0,316,314,1,0,0,0,316,315,1,0,0,0,317,318,1,0,0,0,318,
        319,5,29,0,0,319,320,5,1,0,0,320,321,3,32,16,0,321,322,5,2,0,0,322,
        323,5,5,0,0,323,69,1,0,0,0,27,77,83,90,99,108,115,126,133,144,151,
        157,167,176,182,196,206,213,227,245,254,262,274,286,292,303,305,
        316
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'.'", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'&&'", 
                     "'||'", "'<'", "'>'", "'=='", "'<='", "'>='", "'=!'", 
                     "<INVALID>", "'int'", "'double'", "'long'", "'char'", 
                     "'string'", "'void'", "'while'", "'for'", "'if'", "'else'", 
                     "'return'", "'do'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "PUNTO", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "ASIG", 
                      "AND", "OR", "MENOR", "MAYOR", "IGUAL", "MENORIG", 
                      "MAYORIG", "DIF", "NUMERO", "INT", "DOUBLE", "LONG", 
                      "CHAR", "STRING", "VOID", "WHILE", "FOR", "IF", "ELSE", 
                      "RETURN", "DO", "ID", "ENTERO", "DECIMAL", "WS" ]

    RULE_comparadores = 0
    RULE_tdato = 1
    RULE_programa = 2
    RULE_funcion = 3
    RULE_funcionvoid = 4
    RULE_funcionreturn = 5
    RULE_bloquereturn = 6
    RULE_parametros = 7
    RULE_parametrosp = 8
    RULE_usofuncion = 9
    RULE_argumentos = 10
    RULE_argumentosp = 11
    RULE_instrucciones = 12
    RULE_instruccion = 13
    RULE_declaracion = 14
    RULE_asignacion = 15
    RULE_opal = 16
    RULE_lor = 17
    RULE_lorp = 18
    RULE_land = 19
    RULE_landp = 20
    RULE_comp = 21
    RULE_exp = 22
    RULE_e = 23
    RULE_term = 24
    RULE_t = 25
    RULE_factor = 26
    RULE_iwhile = 27
    RULE_bloque = 28
    RULE_iif = 29
    RULE_ifor = 30
    RULE_init = 31
    RULE_cond = 32
    RULE_iter = 33
    RULE_ido = 34

    ruleNames =  [ "comparadores", "tdato", "programa", "funcion", "funcionvoid", 
                   "funcionreturn", "bloquereturn", "parametros", "parametrosp", 
                   "usofuncion", "argumentos", "argumentosp", "instrucciones", 
                   "instruccion", "declaracion", "asignacion", "opal", "lor", 
                   "lorp", "land", "landp", "comp", "exp", "e", "term", 
                   "t", "factor", "iwhile", "bloque", "iif", "ifor", "init", 
                   "cond", "iter", "ido" ]

    EOF = Token.EOF
    PA=1
    PC=2
    LLA=3
    LLC=4
    PYC=5
    PUNTO=6
    COMA=7
    SUMA=8
    RESTA=9
    MULT=10
    DIV=11
    MOD=12
    ASIG=13
    AND=14
    OR=15
    MENOR=16
    MAYOR=17
    IGUAL=18
    MENORIG=19
    MAYORIG=20
    DIF=21
    NUMERO=22
    INT=23
    DOUBLE=24
    LONG=25
    CHAR=26
    STRING=27
    VOID=28
    WHILE=29
    FOR=30
    IF=31
    ELSE=32
    RETURN=33
    DO=34
    ID=35
    ENTERO=36
    DECIMAL=37
    WS=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ComparadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOR(self):
            return self.getToken(compiladoresParser.MENOR, 0)

        def MAYOR(self):
            return self.getToken(compiladoresParser.MAYOR, 0)

        def IGUAL(self):
            return self.getToken(compiladoresParser.IGUAL, 0)

        def MENORIG(self):
            return self.getToken(compiladoresParser.MENORIG, 0)

        def MAYORIG(self):
            return self.getToken(compiladoresParser.MAYORIG, 0)

        def DIF(self):
            return self.getToken(compiladoresParser.DIF, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_comparadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparadores" ):
                listener.enterComparadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparadores" ):
                listener.exitComparadores(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparadores" ):
                return visitor.visitComparadores(self)
            else:
                return visitor.visitChildren(self)




    def comparadores(self):

        localctx = compiladoresParser.ComparadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_comparadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0)):
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


    class TdatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(compiladoresParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(compiladoresParser.DOUBLE, 0)

        def LONG(self):
            return self.getToken(compiladoresParser.LONG, 0)

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def STRING(self):
            return self.getToken(compiladoresParser.STRING, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_tdato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTdato" ):
                listener.enterTdato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTdato" ):
                listener.exitTdato(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTdato" ):
                return visitor.visitTdato(self)
            else:
                return visitor.visitChildren(self)




    def tdato(self):

        localctx = compiladoresParser.TdatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tdato)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 260046848) != 0)):
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


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(compiladoresParser.EOF, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,i)


        def funcion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.FuncionContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.FuncionContext,i)


        def getRuleIndex(self):
            return compiladoresParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = compiladoresParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.declaracion() 
                self.state = 79
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 528482304) != 0):
                self.state = 80
                self.funcion()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(compiladoresParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcionvoid(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionvoidContext,0)


        def funcionreturn(self):
            return self.getTypedRuleContext(compiladoresParser.FuncionreturnContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncion" ):
                return visitor.visitFuncion(self)
            else:
                return visitor.visitChildren(self)




    def funcion(self):

        localctx = compiladoresParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcion)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.funcionvoid()
                pass
            elif token in [23, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.funcionreturn()
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


    class FuncionvoidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funcionvoid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionvoid" ):
                listener.enterFuncionvoid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionvoid" ):
                listener.exitFuncionvoid(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionvoid" ):
                return visitor.visitFuncionvoid(self)
            else:
                return visitor.visitChildren(self)




    def funcionvoid(self):

        localctx = compiladoresParser.FuncionvoidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcionvoid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(compiladoresParser.VOID)
            self.state = 93
            self.match(compiladoresParser.ID)
            self.state = 94
            self.match(compiladoresParser.PA)
            self.state = 95
            self.parametros()
            self.state = 96
            self.match(compiladoresParser.PC)
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 97
                self.bloque()
                pass
            elif token in [5]:
                self.state = 98
                self.match(compiladoresParser.PYC)
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


    class FuncionreturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloquereturn(self):
            return self.getTypedRuleContext(compiladoresParser.BloquereturnContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_funcionreturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionreturn" ):
                listener.enterFuncionreturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionreturn" ):
                listener.exitFuncionreturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionreturn" ):
                return visitor.visitFuncionreturn(self)
            else:
                return visitor.visitChildren(self)




    def funcionreturn(self):

        localctx = compiladoresParser.FuncionreturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcionreturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.tdato()
            self.state = 102
            self.match(compiladoresParser.ID)
            self.state = 103
            self.match(compiladoresParser.PA)
            self.state = 104
            self.parametros()
            self.state = 105
            self.match(compiladoresParser.PC)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 106
                self.bloquereturn()
                pass
            elif token in [5]:
                self.state = 107
                self.match(compiladoresParser.PYC)
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


    class BloquereturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloquereturn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloquereturn" ):
                listener.enterBloquereturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloquereturn" ):
                listener.exitBloquereturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloquereturn" ):
                return visitor.visitBloquereturn(self)
            else:
                return visitor.visitChildren(self)




    def bloquereturn(self):

        localctx = compiladoresParser.BloquereturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bloquereturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(compiladoresParser.LLA)
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 111
                self.instrucciones()
                self.state = 112
                self.match(compiladoresParser.RETURN)
                pass

            elif la_ == 2:
                self.state = 114
                self.match(compiladoresParser.RETURN)
                pass


            self.state = 117
            self.opal()
            self.state = 118
            self.match(compiladoresParser.PYC)
            self.state = 119
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def parametrosp(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametros" ):
                return visitor.visitParametros(self)
            else:
                return visitor.visitChildren(self)




    def parametros(self):

        localctx = compiladoresParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parametros)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25, 26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.tdato()
                self.state = 122
                self.match(compiladoresParser.ID)
                self.state = 123
                self.parametrosp()
                pass
            elif token in [2, 7]:
                self.enterOuterAlt(localctx, 2)

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


    class ParametrospContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def parametros(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrosContext,0)


        def parametrosp(self):
            return self.getTypedRuleContext(compiladoresParser.ParametrospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_parametrosp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametrosp" ):
                listener.enterParametrosp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametrosp" ):
                listener.exitParametrosp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametrosp" ):
                return visitor.visitParametrosp(self)
            else:
                return visitor.visitChildren(self)




    def parametrosp(self):

        localctx = compiladoresParser.ParametrospContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametrosp)
        try:
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.match(compiladoresParser.COMA)
                self.state = 129
                self.parametros()
                self.state = 130
                self.parametrosp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UsofuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_usofuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUsofuncion" ):
                listener.enterUsofuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUsofuncion" ):
                listener.exitUsofuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUsofuncion" ):
                return visitor.visitUsofuncion(self)
            else:
                return visitor.visitChildren(self)




    def usofuncion(self):

        localctx = compiladoresParser.UsofuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_usofuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(compiladoresParser.ID)
            self.state = 136
            self.match(compiladoresParser.PA)

            self.state = 137
            self.argumentos()
            self.state = 138
            self.match(compiladoresParser.PC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = compiladoresParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argumentos)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.opal()
                self.state = 141
                self.argumentosp()
                pass
            elif token in [2, 7]:
                self.enterOuterAlt(localctx, 2)

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


    class ArgumentospContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(compiladoresParser.COMA, 0)

        def argumentos(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentosContext,0)


        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_argumentosp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentosp" ):
                listener.enterArgumentosp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentosp" ):
                listener.exitArgumentosp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentosp" ):
                return visitor.visitArgumentosp(self)
            else:
                return visitor.visitChildren(self)




    def argumentosp(self):

        localctx = compiladoresParser.ArgumentospContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_argumentosp)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(compiladoresParser.COMA)
                self.state = 147
                self.argumentos()
                self.state = 148
                self.argumentosp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_instrucciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstrucciones" ):
                listener.enterInstrucciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstrucciones" ):
                listener.exitInstrucciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstrucciones" ):
                return visitor.visitInstrucciones(self)
            else:
                return visitor.visitChildren(self)




    def instrucciones(self):

        localctx = compiladoresParser.InstruccionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_instrucciones)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 5, 23, 24, 25, 26, 27, 29, 30, 31, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.instruccion()
                self.state = 154
                self.instrucciones()
                pass
            elif token in [4, 33]:
                self.enterOuterAlt(localctx, 2)

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


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(compiladoresParser.DeclaracionContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccion" ):
                return visitor.visitInstruccion(self)
            else:
                return visitor.visitChildren(self)




    def instruccion(self):

        localctx = compiladoresParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_instruccion)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 161
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 163
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 164
                self.asignacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 165
                self.usofuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 166
                self.match(compiladoresParser.PYC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = compiladoresParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_declaracion)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.tdato()
                self.state = 170
                self.match(compiladoresParser.ID)
                self.state = 171
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.tdato()
                self.state = 174
                self.asignacion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = compiladoresParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(compiladoresParser.ID)
            self.state = 179
            self.match(compiladoresParser.ASIG)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 180
                self.usofuncion()
                pass

            elif la_ == 2:
                self.state = 181
                self.opal()
                pass


            self.state = 184
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lor(self):
            return self.getTypedRuleContext(compiladoresParser.LorContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_opal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpal" ):
                listener.enterOpal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpal" ):
                listener.exitOpal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpal" ):
                return visitor.visitOpal(self)
            else:
                return visitor.visitChildren(self)




    def opal(self):

        localctx = compiladoresParser.OpalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.lor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def lorp(self):
            return self.getTypedRuleContext(compiladoresParser.LorpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLor" ):
                listener.enterLor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLor" ):
                listener.exitLor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLor" ):
                return visitor.visitLor(self)
            else:
                return visitor.visitChildren(self)




    def lor(self):

        localctx = compiladoresParser.LorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.land()
            self.state = 189
            self.lorp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LorpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(compiladoresParser.OR, 0)

        def land(self):
            return self.getTypedRuleContext(compiladoresParser.LandContext,0)


        def lorp(self):
            return self.getTypedRuleContext(compiladoresParser.LorpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_lorp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLorp" ):
                listener.enterLorp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLorp" ):
                listener.exitLorp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLorp" ):
                return visitor.visitLorp(self)
            else:
                return visitor.visitChildren(self)




    def lorp(self):

        localctx = compiladoresParser.LorpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_lorp)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(compiladoresParser.OR)
                self.state = 192
                self.land()
                self.state = 193
                self.lorp()
                pass
            elif token in [2, 5, 7]:
                self.enterOuterAlt(localctx, 2)

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


    class LandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def landp(self):
            return self.getTypedRuleContext(compiladoresParser.LandpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_land

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLand" ):
                listener.enterLand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLand" ):
                listener.exitLand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLand" ):
                return visitor.visitLand(self)
            else:
                return visitor.visitChildren(self)




    def land(self):

        localctx = compiladoresParser.LandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.comp()
            self.state = 199
            self.landp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LandpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(compiladoresParser.AND, 0)

        def comp(self):
            return self.getTypedRuleContext(compiladoresParser.CompContext,0)


        def landp(self):
            return self.getTypedRuleContext(compiladoresParser.LandpContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_landp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLandp" ):
                listener.enterLandp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLandp" ):
                listener.exitLandp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLandp" ):
                return visitor.visitLandp(self)
            else:
                return visitor.visitChildren(self)




    def landp(self):

        localctx = compiladoresParser.LandpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_landp)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(compiladoresParser.AND)
                self.state = 202
                self.comp()
                self.state = 203
                self.landp()
                pass
            elif token in [2, 5, 7, 15]:
                self.enterOuterAlt(localctx, 2)

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


    class CompContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(compiladoresParser.ExpContext)
            else:
                return self.getTypedRuleContext(compiladoresParser.ExpContext,i)


        def comparadores(self):
            return self.getTypedRuleContext(compiladoresParser.ComparadoresContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_comp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComp" ):
                listener.enterComp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComp" ):
                listener.exitComp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp" ):
                return visitor.visitComp(self)
            else:
                return visitor.visitChildren(self)




    def comp(self):

        localctx = compiladoresParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comp)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.exp()
                self.state = 209
                self.comparadores()
                self.state = 210
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = compiladoresParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.term()
            self.state = 216
            self.e()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(compiladoresParser.SUMA, 0)

        def term(self):
            return self.getTypedRuleContext(compiladoresParser.TermContext,0)


        def e(self):
            return self.getTypedRuleContext(compiladoresParser.EContext,0)


        def RESTA(self):
            return self.getToken(compiladoresParser.RESTA, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = compiladoresParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_e)
        try:
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.match(compiladoresParser.SUMA)
                self.state = 219
                self.term()
                self.state = 220
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.match(compiladoresParser.RESTA)
                self.state = 223
                self.term()
                self.state = 224
                self.e()
                pass
            elif token in [2, 5, 7, 14, 15, 16, 17, 18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 3)

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


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = compiladoresParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.factor()
            self.state = 230
            self.t()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(compiladoresParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(compiladoresParser.FactorContext,0)


        def t(self):
            return self.getTypedRuleContext(compiladoresParser.TContext,0)


        def DIV(self):
            return self.getToken(compiladoresParser.DIV, 0)

        def MOD(self):
            return self.getToken(compiladoresParser.MOD, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_t

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT" ):
                listener.enterT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT" ):
                listener.exitT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT" ):
                return visitor.visitT(self)
            else:
                return visitor.visitChildren(self)




    def t(self):

        localctx = compiladoresParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_t)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(compiladoresParser.MULT)
                self.state = 233
                self.factor()
                self.state = 234
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(compiladoresParser.DIV)
                self.state = 237
                self.factor()
                self.state = 238
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.match(compiladoresParser.MOD)
                self.state = 241
                self.factor()
                self.state = 242
                self.t()
                pass
            elif token in [2, 5, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21]:
                self.enterOuterAlt(localctx, 4)

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


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = compiladoresParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_factor)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 250
                self.match(compiladoresParser.PA)
                self.state = 251
                self.exp()
                self.state = 252
                self.match(compiladoresParser.PC)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIwhile" ):
                listener.enterIwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIwhile" ):
                listener.exitIwhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIwhile" ):
                return visitor.visitIwhile(self)
            else:
                return visitor.visitChildren(self)




    def iwhile(self):

        localctx = compiladoresParser.IwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(compiladoresParser.WHILE)
            self.state = 257
            self.match(compiladoresParser.PA)
            self.state = 258
            self.cond()
            self.state = 259
            self.match(compiladoresParser.PC)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 260
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 261
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = compiladoresParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(compiladoresParser.LLA)
            self.state = 265
            self.instrucciones()
            self.state = 266
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(compiladoresParser.IF, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_iif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIif" ):
                listener.enterIif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIif" ):
                listener.exitIif(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIif" ):
                return visitor.visitIif(self)
            else:
                return visitor.visitChildren(self)




    def iif(self):

        localctx = compiladoresParser.IifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(compiladoresParser.IF)
            self.state = 269
            self.match(compiladoresParser.PA)
            self.state = 270
            self.cond()
            self.state = 271
            self.match(compiladoresParser.PC)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 272
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 273
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(compiladoresParser.FOR, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def init(self):
            return self.getTypedRuleContext(compiladoresParser.InitContext,0)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

        def cond(self):
            return self.getTypedRuleContext(compiladoresParser.CondContext,0)


        def iter_(self):
            return self.getTypedRuleContext(compiladoresParser.IterContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ifor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfor" ):
                listener.enterIfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfor" ):
                listener.exitIfor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfor" ):
                return visitor.visitIfor(self)
            else:
                return visitor.visitChildren(self)




    def ifor(self):

        localctx = compiladoresParser.IforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(compiladoresParser.FOR)
            self.state = 277
            self.match(compiladoresParser.PA)
            self.state = 278
            self.init()
            self.state = 279
            self.match(compiladoresParser.PYC)
            self.state = 280
            self.cond()
            self.state = 281
            self.match(compiladoresParser.PYC)
            self.state = 282
            self.iter_()
            self.state = 283
            self.match(compiladoresParser.PC)
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 284
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 285
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def usofuncion(self):
            return self.getTypedRuleContext(compiladoresParser.UsofuncionContext,0)


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def tdato(self):
            return self.getTypedRuleContext(compiladoresParser.TdatoContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInit" ):
                listener.enterInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInit" ):
                listener.exitInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = compiladoresParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_init)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(compiladoresParser.ID)
                self.state = 289
                self.match(compiladoresParser.ASIG)
                self.state = 292
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 290
                    self.usofuncion()
                    pass

                elif la_ == 2:
                    self.state = 291
                    self.opal()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.tdato()
                self.state = 296
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 298
                self.tdato()
                self.state = 299
                self.match(compiladoresParser.ID)
                self.state = 300
                self.match(compiladoresParser.ASIG)
                self.state = 303
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 301
                    self.usofuncion()
                    pass

                elif la_ == 2:
                    self.state = 302
                    self.opal()
                    pass


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond" ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond" ):
                listener.exitCond(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)




    def cond(self):

        localctx = compiladoresParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.opal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def exp(self):
            return self.getTypedRuleContext(compiladoresParser.ExpContext,0)


        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_iter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIter" ):
                listener.enterIter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIter" ):
                listener.exitIter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIter" ):
                return visitor.visitIter(self)
            else:
                return visitor.visitChildren(self)




    def iter_(self):

        localctx = compiladoresParser.IterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_iter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not(_la==22 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 310
            self.match(compiladoresParser.ASIG)
            self.state = 311
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(compiladoresParser.DO, 0)

        def WHILE(self):
            return self.getToken(compiladoresParser.WHILE, 0)

        def PA(self):
            return self.getToken(compiladoresParser.PA, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PC(self):
            return self.getToken(compiladoresParser.PC, 0)

        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ido

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdo" ):
                listener.enterIdo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdo" ):
                listener.exitIdo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdo" ):
                return visitor.visitIdo(self)
            else:
                return visitor.visitChildren(self)




    def ido(self):

        localctx = compiladoresParser.IdoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ido)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(compiladoresParser.DO)
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 314
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 315
                self.instruccion()
                pass


            self.state = 318
            self.match(compiladoresParser.WHILE)
            self.state = 319
            self.match(compiladoresParser.PA)
            self.state = 320
            self.opal()
            self.state = 321
            self.match(compiladoresParser.PC)
            self.state = 322
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





