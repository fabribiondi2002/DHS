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
        4,1,38,311,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,1,1,1,1,2,5,2,72,8,2,10,2,12,2,75,9,2,1,2,5,2,78,8,2,10,2,
        12,2,81,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,92,8,3,1,4,1,
        4,1,4,1,4,1,4,3,4,99,8,4,1,5,1,5,1,5,1,5,1,5,3,5,106,8,5,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,3,7,116,8,7,1,8,1,8,1,8,1,8,1,8,3,8,123,
        8,8,1,9,1,9,1,9,1,9,3,9,129,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,141,8,10,1,11,1,11,1,11,1,11,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,157,8,12,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,17,1,
        17,1,17,1,17,1,17,3,17,178,8,17,1,18,1,18,1,18,1,19,1,19,1,19,1,
        19,1,19,3,19,188,8,19,1,20,1,20,1,20,1,20,1,20,3,20,195,8,20,1,21,
        1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,209,
        8,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,3,24,227,8,24,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,3,25,236,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        3,26,247,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,
        258,8,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,3,28,273,8,28,1,29,1,29,1,29,1,29,3,29,279,8,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,290,8,29,3,29,292,8,29,
        1,30,1,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,3,32,303,8,32,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        0,3,1,0,16,21,3,0,23,24,26,26,28,28,2,0,22,22,35,35,315,0,66,1,0,
        0,0,2,68,1,0,0,0,4,73,1,0,0,0,6,84,1,0,0,0,8,98,1,0,0,0,10,105,1,
        0,0,0,12,107,1,0,0,0,14,115,1,0,0,0,16,122,1,0,0,0,18,128,1,0,0,
        0,20,140,1,0,0,0,22,142,1,0,0,0,24,156,1,0,0,0,26,158,1,0,0,0,28,
        163,1,0,0,0,30,167,1,0,0,0,32,169,1,0,0,0,34,177,1,0,0,0,36,179,
        1,0,0,0,38,187,1,0,0,0,40,194,1,0,0,0,42,196,1,0,0,0,44,208,1,0,
        0,0,46,210,1,0,0,0,48,226,1,0,0,0,50,235,1,0,0,0,52,237,1,0,0,0,
        54,248,1,0,0,0,56,259,1,0,0,0,58,291,1,0,0,0,60,293,1,0,0,0,62,295,
        1,0,0,0,64,299,1,0,0,0,66,67,7,0,0,0,67,1,1,0,0,0,68,69,7,1,0,0,
        69,3,1,0,0,0,70,72,3,24,12,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,
        0,0,0,73,74,1,0,0,0,74,79,1,0,0,0,75,73,1,0,0,0,76,78,3,6,3,0,77,
        76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,
        0,81,79,1,0,0,0,82,83,5,0,0,1,83,5,1,0,0,0,84,85,3,2,1,0,85,86,5,
        35,0,0,86,87,5,1,0,0,87,88,3,8,4,0,88,91,5,2,0,0,89,92,3,22,11,0,
        90,92,5,5,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,7,1,0,0,0,93,94,3,2,
        1,0,94,95,5,35,0,0,95,96,3,10,5,0,96,99,1,0,0,0,97,99,1,0,0,0,98,
        93,1,0,0,0,98,97,1,0,0,0,99,9,1,0,0,0,100,101,5,7,0,0,101,102,3,
        8,4,0,102,103,3,10,5,0,103,106,1,0,0,0,104,106,1,0,0,0,105,100,1,
        0,0,0,105,104,1,0,0,0,106,11,1,0,0,0,107,108,5,35,0,0,108,109,5,
        1,0,0,109,110,3,14,7,0,110,111,5,2,0,0,111,13,1,0,0,0,112,113,7,
        2,0,0,113,116,3,16,8,0,114,116,1,0,0,0,115,112,1,0,0,0,115,114,1,
        0,0,0,116,15,1,0,0,0,117,118,5,7,0,0,118,119,3,14,7,0,119,120,3,
        16,8,0,120,123,1,0,0,0,121,123,1,0,0,0,122,117,1,0,0,0,122,121,1,
        0,0,0,123,17,1,0,0,0,124,125,3,20,10,0,125,126,3,18,9,0,126,129,
        1,0,0,0,127,129,1,0,0,0,128,124,1,0,0,0,128,127,1,0,0,0,129,19,1,
        0,0,0,130,141,3,24,12,0,131,141,3,52,26,0,132,141,3,56,28,0,133,
        141,3,54,27,0,134,141,3,22,11,0,135,141,3,26,13,0,136,141,3,12,6,
        0,137,141,3,30,15,0,138,141,3,28,14,0,139,141,5,5,0,0,140,130,1,
        0,0,0,140,131,1,0,0,0,140,132,1,0,0,0,140,133,1,0,0,0,140,134,1,
        0,0,0,140,135,1,0,0,0,140,136,1,0,0,0,140,137,1,0,0,0,140,138,1,
        0,0,0,140,139,1,0,0,0,141,21,1,0,0,0,142,143,5,3,0,0,143,144,3,18,
        9,0,144,145,5,4,0,0,145,23,1,0,0,0,146,147,3,2,1,0,147,148,5,35,
        0,0,148,149,5,5,0,0,149,157,1,0,0,0,150,151,3,2,1,0,151,152,5,35,
        0,0,152,153,5,13,0,0,153,154,3,30,15,0,154,155,5,5,0,0,155,157,1,
        0,0,0,156,146,1,0,0,0,156,150,1,0,0,0,157,25,1,0,0,0,158,159,5,35,
        0,0,159,160,5,13,0,0,160,161,3,30,15,0,161,162,5,5,0,0,162,27,1,
        0,0,0,163,164,5,33,0,0,164,165,3,30,15,0,165,166,5,5,0,0,166,29,
        1,0,0,0,167,168,3,32,16,0,168,31,1,0,0,0,169,170,3,36,18,0,170,171,
        3,34,17,0,171,33,1,0,0,0,172,173,5,15,0,0,173,174,3,36,18,0,174,
        175,3,34,17,0,175,178,1,0,0,0,176,178,1,0,0,0,177,172,1,0,0,0,177,
        176,1,0,0,0,178,35,1,0,0,0,179,180,3,40,20,0,180,181,3,38,19,0,181,
        37,1,0,0,0,182,183,5,14,0,0,183,184,3,40,20,0,184,185,3,38,19,0,
        185,188,1,0,0,0,186,188,1,0,0,0,187,182,1,0,0,0,187,186,1,0,0,0,
        188,39,1,0,0,0,189,190,3,42,21,0,190,191,3,0,0,0,191,192,3,42,21,
        0,192,195,1,0,0,0,193,195,3,42,21,0,194,189,1,0,0,0,194,193,1,0,
        0,0,195,41,1,0,0,0,196,197,3,46,23,0,197,198,3,44,22,0,198,43,1,
        0,0,0,199,200,5,8,0,0,200,201,3,46,23,0,201,202,3,44,22,0,202,209,
        1,0,0,0,203,204,5,9,0,0,204,205,3,46,23,0,205,206,3,44,22,0,206,
        209,1,0,0,0,207,209,1,0,0,0,208,199,1,0,0,0,208,203,1,0,0,0,208,
        207,1,0,0,0,209,45,1,0,0,0,210,211,3,50,25,0,211,212,3,48,24,0,212,
        47,1,0,0,0,213,214,5,10,0,0,214,215,3,50,25,0,215,216,3,48,24,0,
        216,227,1,0,0,0,217,218,5,11,0,0,218,219,3,50,25,0,219,220,3,48,
        24,0,220,227,1,0,0,0,221,222,5,12,0,0,222,223,3,50,25,0,223,224,
        3,48,24,0,224,227,1,0,0,0,225,227,1,0,0,0,226,213,1,0,0,0,226,217,
        1,0,0,0,226,221,1,0,0,0,226,225,1,0,0,0,227,49,1,0,0,0,228,236,5,
        22,0,0,229,236,5,35,0,0,230,236,3,12,6,0,231,232,5,1,0,0,232,233,
        3,42,21,0,233,234,5,2,0,0,234,236,1,0,0,0,235,228,1,0,0,0,235,229,
        1,0,0,0,235,230,1,0,0,0,235,231,1,0,0,0,236,51,1,0,0,0,237,238,5,
        29,0,0,238,239,5,1,0,0,239,240,3,60,30,0,240,246,5,2,0,0,241,242,
        5,3,0,0,242,243,3,18,9,0,243,244,5,4,0,0,244,247,1,0,0,0,245,247,
        3,20,10,0,246,241,1,0,0,0,246,245,1,0,0,0,247,53,1,0,0,0,248,249,
        5,31,0,0,249,250,5,1,0,0,250,251,3,60,30,0,251,257,5,2,0,0,252,253,
        5,3,0,0,253,254,3,18,9,0,254,255,5,4,0,0,255,258,1,0,0,0,256,258,
        3,20,10,0,257,252,1,0,0,0,257,256,1,0,0,0,258,55,1,0,0,0,259,260,
        5,30,0,0,260,261,5,1,0,0,261,262,3,58,29,0,262,263,5,5,0,0,263,264,
        3,60,30,0,264,265,5,5,0,0,265,266,3,62,31,0,266,272,5,2,0,0,267,
        268,5,3,0,0,268,269,3,18,9,0,269,270,5,4,0,0,270,273,1,0,0,0,271,
        273,3,20,10,0,272,267,1,0,0,0,272,271,1,0,0,0,273,57,1,0,0,0,274,
        275,5,35,0,0,275,278,5,13,0,0,276,279,3,12,6,0,277,279,3,30,15,0,
        278,276,1,0,0,0,278,277,1,0,0,0,279,292,1,0,0,0,280,292,5,35,0,0,
        281,282,3,2,1,0,282,283,5,35,0,0,283,292,1,0,0,0,284,285,3,2,1,0,
        285,286,5,35,0,0,286,289,5,13,0,0,287,290,3,12,6,0,288,290,3,30,
        15,0,289,287,1,0,0,0,289,288,1,0,0,0,290,292,1,0,0,0,291,274,1,0,
        0,0,291,280,1,0,0,0,291,281,1,0,0,0,291,284,1,0,0,0,292,59,1,0,0,
        0,293,294,3,30,15,0,294,61,1,0,0,0,295,296,7,2,0,0,296,297,5,13,
        0,0,297,298,3,42,21,0,298,63,1,0,0,0,299,302,5,34,0,0,300,303,3,
        22,11,0,301,303,3,20,10,0,302,300,1,0,0,0,302,301,1,0,0,0,303,304,
        1,0,0,0,304,305,5,29,0,0,305,306,5,1,0,0,306,307,3,30,15,0,307,308,
        5,2,0,0,308,309,5,5,0,0,309,65,1,0,0,0,23,73,79,91,98,105,115,122,
        128,140,156,177,187,194,208,226,235,246,257,272,278,289,291,302
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
    RULE_parametros = 4
    RULE_parametrosp = 5
    RULE_usofuncion = 6
    RULE_argumentos = 7
    RULE_argumentosp = 8
    RULE_instrucciones = 9
    RULE_instruccion = 10
    RULE_bloque = 11
    RULE_declaracion = 12
    RULE_asignacion = 13
    RULE_return = 14
    RULE_opal = 15
    RULE_lor = 16
    RULE_lorp = 17
    RULE_land = 18
    RULE_landp = 19
    RULE_comp = 20
    RULE_exp = 21
    RULE_e = 22
    RULE_term = 23
    RULE_t = 24
    RULE_factor = 25
    RULE_iwhile = 26
    RULE_iif = 27
    RULE_ifor = 28
    RULE_init = 29
    RULE_cond = 30
    RULE_iter = 31
    RULE_ido = 32

    ruleNames =  [ "comparadores", "tdato", "programa", "funcion", "parametros", 
                   "parametrosp", "usofuncion", "argumentos", "argumentosp", 
                   "instrucciones", "instruccion", "bloque", "declaracion", 
                   "asignacion", "return", "opal", "lor", "lorp", "land", 
                   "landp", "comp", "exp", "e", "term", "t", "factor", "iwhile", 
                   "iif", "ifor", "init", "cond", "iter", "ido" ]

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
            self.state = 66
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

        def CHAR(self):
            return self.getToken(compiladoresParser.CHAR, 0)

        def VOID(self):
            return self.getToken(compiladoresParser.VOID, 0)

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
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 360710144) != 0)):
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
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 70
                    self.declaracion() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 360710144) != 0):
                self.state = 76
                self.funcion()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
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

        def bloque(self):
            return self.getTypedRuleContext(compiladoresParser.BloqueContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.tdato()
            self.state = 85
            self.match(compiladoresParser.ID)
            self.state = 86
            self.match(compiladoresParser.PA)
            self.state = 87
            self.parametros()
            self.state = 88
            self.match(compiladoresParser.PC)
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 89
                self.bloque()
                pass
            elif token in [5]:
                self.state = 90
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
        self.enterRule(localctx, 8, self.RULE_parametros)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 26, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.tdato()
                self.state = 94
                self.match(compiladoresParser.ID)
                self.state = 95
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
        self.enterRule(localctx, 10, self.RULE_parametrosp)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(compiladoresParser.COMA)
                self.state = 101
                self.parametros()
                self.state = 102
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
        self.enterRule(localctx, 12, self.RULE_usofuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(compiladoresParser.ID)
            self.state = 108
            self.match(compiladoresParser.PA)

            self.state = 109
            self.argumentos()
            self.state = 110
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

        def argumentosp(self):
            return self.getTypedRuleContext(compiladoresParser.ArgumentospContext,0)


        def NUMERO(self):
            return self.getToken(compiladoresParser.NUMERO, 0)

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

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
        self.enterRule(localctx, 14, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                _la = self._input.LA(1)
                if not(_la==22 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 113
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
        self.enterRule(localctx, 16, self.RULE_argumentosp)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(compiladoresParser.COMA)
                self.state = 118
                self.argumentos()
                self.state = 119
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
        self.enterRule(localctx, 18, self.RULE_instrucciones)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.instruccion()
                self.state = 125
                self.instrucciones()
                pass
            elif token in [4]:
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


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def return_(self):
            return self.getTypedRuleContext(compiladoresParser.ReturnContext,0)


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
        self.enterRule(localctx, 20, self.RULE_instruccion)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.iwhile()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.ifor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 133
                self.iif()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 134
                self.bloque()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 135
                self.asignacion()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 136
                self.usofuncion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 137
                self.opal()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 138
                self.return_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 139
                self.match(compiladoresParser.PYC)
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
        self.enterRule(localctx, 22, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(compiladoresParser.LLA)
            self.state = 143
            self.instrucciones()
            self.state = 144
            self.match(compiladoresParser.LLC)
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

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        self.enterRule(localctx, 24, self.RULE_declaracion)
        try:
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.tdato()
                self.state = 147
                self.match(compiladoresParser.ID)
                self.state = 148
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.tdato()
                self.state = 151
                self.match(compiladoresParser.ID)
                self.state = 152
                self.match(compiladoresParser.ASIG)
                self.state = 153
                self.opal()
                self.state = 154
                self.match(compiladoresParser.PYC)
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

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

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
        self.enterRule(localctx, 26, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(compiladoresParser.ID)
            self.state = 159
            self.match(compiladoresParser.ASIG)
            self.state = 160
            self.opal()
            self.state = 161
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(compiladoresParser.RETURN, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

        def getRuleIndex(self):
            return compiladoresParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)




    def return_(self):

        localctx = compiladoresParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(compiladoresParser.RETURN)
            self.state = 164
            self.opal()
            self.state = 165
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
        self.enterRule(localctx, 30, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 32, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.land()
            self.state = 170
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
        self.enterRule(localctx, 34, self.RULE_lorp)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(compiladoresParser.OR)
                self.state = 173
                self.land()
                self.state = 174
                self.lorp()
                pass
            elif token in [1, 2, 3, 4, 5, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 36, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.comp()
            self.state = 180
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
        self.enterRule(localctx, 38, self.RULE_landp)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(compiladoresParser.AND)
                self.state = 183
                self.comp()
                self.state = 184
                self.landp()
                pass
            elif token in [1, 2, 3, 4, 5, 15, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 40, self.RULE_comp)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.exp()
                self.state = 190
                self.comparadores()
                self.state = 191
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
        self.enterRule(localctx, 42, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.term()
            self.state = 197
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
        self.enterRule(localctx, 44, self.RULE_e)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.match(compiladoresParser.SUMA)
                self.state = 200
                self.term()
                self.state = 201
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(compiladoresParser.RESTA)
                self.state = 204
                self.term()
                self.state = 205
                self.e()
                pass
            elif token in [1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 46, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.factor()
            self.state = 211
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
        self.enterRule(localctx, 48, self.RULE_t)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(compiladoresParser.MULT)
                self.state = 214
                self.factor()
                self.state = 215
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(compiladoresParser.DIV)
                self.state = 218
                self.factor()
                self.state = 219
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(compiladoresParser.MOD)
                self.state = 222
                self.factor()
                self.state = 223
                self.t()
                pass
            elif token in [1, 2, 3, 4, 5, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 50, self.RULE_factor)
        try:
            self.state = 235
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.match(compiladoresParser.PA)
                self.state = 232
                self.exp()
                self.state = 233
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

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

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
        self.enterRule(localctx, 52, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(compiladoresParser.WHILE)
            self.state = 238
            self.match(compiladoresParser.PA)
            self.state = 239
            self.cond()
            self.state = 240
            self.match(compiladoresParser.PC)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(compiladoresParser.LLA)
                self.state = 242
                self.instrucciones()
                self.state = 243
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.state = 245
                self.instruccion()
                pass


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

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

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
        self.enterRule(localctx, 54, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(compiladoresParser.IF)
            self.state = 249
            self.match(compiladoresParser.PA)
            self.state = 250
            self.cond()
            self.state = 251
            self.match(compiladoresParser.PC)
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 252
                self.match(compiladoresParser.LLA)
                self.state = 253
                self.instrucciones()
                self.state = 254
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.state = 256
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

        def LLA(self):
            return self.getToken(compiladoresParser.LLA, 0)

        def instrucciones(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionesContext,0)


        def LLC(self):
            return self.getToken(compiladoresParser.LLC, 0)

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
        self.enterRule(localctx, 56, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(compiladoresParser.FOR)
            self.state = 260
            self.match(compiladoresParser.PA)
            self.state = 261
            self.init()
            self.state = 262
            self.match(compiladoresParser.PYC)
            self.state = 263
            self.cond()
            self.state = 264
            self.match(compiladoresParser.PYC)
            self.state = 265
            self.iter_()
            self.state = 266
            self.match(compiladoresParser.PC)
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 267
                self.match(compiladoresParser.LLA)
                self.state = 268
                self.instrucciones()
                self.state = 269
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.state = 271
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
        self.enterRule(localctx, 58, self.RULE_init)
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(compiladoresParser.ID)
                self.state = 275
                self.match(compiladoresParser.ASIG)
                self.state = 278
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 276
                    self.usofuncion()
                    pass

                elif la_ == 2:
                    self.state = 277
                    self.opal()
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.tdato()
                self.state = 282
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 284
                self.tdato()
                self.state = 285
                self.match(compiladoresParser.ID)
                self.state = 286
                self.match(compiladoresParser.ASIG)
                self.state = 289
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 287
                    self.usofuncion()
                    pass

                elif la_ == 2:
                    self.state = 288
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
        self.enterRule(localctx, 60, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
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
        self.enterRule(localctx, 62, self.RULE_iter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            _la = self._input.LA(1)
            if not(_la==22 or _la==35):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 296
            self.match(compiladoresParser.ASIG)
            self.state = 297
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
        self.enterRule(localctx, 64, self.RULE_ido)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(compiladoresParser.DO)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 300
                self.bloque()
                pass

            elif la_ == 2:
                self.state = 301
                self.instruccion()
                pass


            self.state = 304
            self.match(compiladoresParser.WHILE)
            self.state = 305
            self.match(compiladoresParser.PA)
            self.state = 306
            self.opal()
            self.state = 307
            self.match(compiladoresParser.PC)
            self.state = 308
            self.match(compiladoresParser.PYC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





