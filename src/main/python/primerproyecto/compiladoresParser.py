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
        4,1,38,305,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,1,1,1,1,2,1,2,1,3,5,3,76,8,3,10,3,12,3,79,9,3,1,3,
        5,3,82,8,3,10,3,12,3,85,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,3,5,101,8,5,1,6,1,6,1,6,1,6,1,6,3,6,108,8,6,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,119,8,8,1,9,1,9,1,9,1,9,
        1,9,3,9,126,8,9,1,10,1,10,1,10,1,10,3,10,132,8,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,142,8,11,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,3,13,151,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,3,14,163,8,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,184,
        8,19,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,3,21,194,8,21,1,22,
        1,22,1,22,1,22,1,22,3,22,201,8,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,3,24,215,8,24,1,25,1,25,1,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,
        233,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,242,8,27,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,253,8,28,1,29,1,29,1,
        29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,264,8,29,1,30,1,30,1,30,1,
        30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,279,8,30,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,3,
        31,294,8,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,3,33,303,8,33,1,33,
        0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,0,3,1,0,16,21,2,0,23,24,26,
        26,3,0,23,24,26,26,28,28,307,0,68,1,0,0,0,2,70,1,0,0,0,4,72,1,0,
        0,0,6,77,1,0,0,0,8,88,1,0,0,0,10,100,1,0,0,0,12,107,1,0,0,0,14,109,
        1,0,0,0,16,118,1,0,0,0,18,125,1,0,0,0,20,131,1,0,0,0,22,141,1,0,
        0,0,24,143,1,0,0,0,26,150,1,0,0,0,28,162,1,0,0,0,30,164,1,0,0,0,
        32,169,1,0,0,0,34,173,1,0,0,0,36,175,1,0,0,0,38,183,1,0,0,0,40,185,
        1,0,0,0,42,193,1,0,0,0,44,200,1,0,0,0,46,202,1,0,0,0,48,214,1,0,
        0,0,50,216,1,0,0,0,52,232,1,0,0,0,54,241,1,0,0,0,56,243,1,0,0,0,
        58,254,1,0,0,0,60,265,1,0,0,0,62,293,1,0,0,0,64,295,1,0,0,0,66,302,
        1,0,0,0,68,69,7,0,0,0,69,1,1,0,0,0,70,71,7,1,0,0,71,3,1,0,0,0,72,
        73,7,2,0,0,73,5,1,0,0,0,74,76,3,28,14,0,75,74,1,0,0,0,76,79,1,0,
        0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,83,1,0,0,0,79,77,1,0,0,0,80,82,
        3,8,4,0,81,80,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,
        84,86,1,0,0,0,85,83,1,0,0,0,86,87,5,0,0,1,87,7,1,0,0,0,88,89,3,4,
        2,0,89,90,5,35,0,0,90,91,5,1,0,0,91,92,3,10,5,0,92,93,5,2,0,0,93,
        94,3,24,12,0,94,9,1,0,0,0,95,96,3,2,1,0,96,97,5,35,0,0,97,98,3,12,
        6,0,98,101,1,0,0,0,99,101,1,0,0,0,100,95,1,0,0,0,100,99,1,0,0,0,
        101,11,1,0,0,0,102,103,5,7,0,0,103,104,3,10,5,0,104,105,3,12,6,0,
        105,108,1,0,0,0,106,108,1,0,0,0,107,102,1,0,0,0,107,106,1,0,0,0,
        108,13,1,0,0,0,109,110,5,35,0,0,110,111,5,1,0,0,111,112,3,16,8,0,
        112,113,5,2,0,0,113,15,1,0,0,0,114,115,3,34,17,0,115,116,3,18,9,
        0,116,119,1,0,0,0,117,119,1,0,0,0,118,114,1,0,0,0,118,117,1,0,0,
        0,119,17,1,0,0,0,120,121,5,7,0,0,121,122,3,16,8,0,122,123,3,18,9,
        0,123,126,1,0,0,0,124,126,1,0,0,0,125,120,1,0,0,0,125,124,1,0,0,
        0,126,19,1,0,0,0,127,128,3,22,11,0,128,129,3,20,10,0,129,132,1,0,
        0,0,130,132,1,0,0,0,131,127,1,0,0,0,131,130,1,0,0,0,132,21,1,0,0,
        0,133,142,3,28,14,0,134,142,3,26,13,0,135,142,3,24,12,0,136,142,
        3,30,15,0,137,142,3,14,7,0,138,142,3,34,17,0,139,142,3,32,16,0,140,
        142,5,5,0,0,141,133,1,0,0,0,141,134,1,0,0,0,141,135,1,0,0,0,141,
        136,1,0,0,0,141,137,1,0,0,0,141,138,1,0,0,0,141,139,1,0,0,0,141,
        140,1,0,0,0,142,23,1,0,0,0,143,144,5,3,0,0,144,145,3,20,10,0,145,
        146,5,4,0,0,146,25,1,0,0,0,147,151,3,56,28,0,148,151,3,60,30,0,149,
        151,3,58,29,0,150,147,1,0,0,0,150,148,1,0,0,0,150,149,1,0,0,0,151,
        27,1,0,0,0,152,153,3,2,1,0,153,154,5,35,0,0,154,155,5,5,0,0,155,
        163,1,0,0,0,156,157,3,2,1,0,157,158,5,35,0,0,158,159,5,13,0,0,159,
        160,3,34,17,0,160,161,5,5,0,0,161,163,1,0,0,0,162,152,1,0,0,0,162,
        156,1,0,0,0,163,29,1,0,0,0,164,165,5,35,0,0,165,166,5,13,0,0,166,
        167,3,34,17,0,167,168,5,5,0,0,168,31,1,0,0,0,169,170,5,33,0,0,170,
        171,3,34,17,0,171,172,5,5,0,0,172,33,1,0,0,0,173,174,3,36,18,0,174,
        35,1,0,0,0,175,176,3,40,20,0,176,177,3,38,19,0,177,37,1,0,0,0,178,
        179,5,15,0,0,179,180,3,40,20,0,180,181,3,38,19,0,181,184,1,0,0,0,
        182,184,1,0,0,0,183,178,1,0,0,0,183,182,1,0,0,0,184,39,1,0,0,0,185,
        186,3,44,22,0,186,187,3,42,21,0,187,41,1,0,0,0,188,189,5,14,0,0,
        189,190,3,44,22,0,190,191,3,42,21,0,191,194,1,0,0,0,192,194,1,0,
        0,0,193,188,1,0,0,0,193,192,1,0,0,0,194,43,1,0,0,0,195,196,3,46,
        23,0,196,197,3,0,0,0,197,198,3,46,23,0,198,201,1,0,0,0,199,201,3,
        46,23,0,200,195,1,0,0,0,200,199,1,0,0,0,201,45,1,0,0,0,202,203,3,
        50,25,0,203,204,3,48,24,0,204,47,1,0,0,0,205,206,5,8,0,0,206,207,
        3,50,25,0,207,208,3,48,24,0,208,215,1,0,0,0,209,210,5,9,0,0,210,
        211,3,50,25,0,211,212,3,48,24,0,212,215,1,0,0,0,213,215,1,0,0,0,
        214,205,1,0,0,0,214,209,1,0,0,0,214,213,1,0,0,0,215,49,1,0,0,0,216,
        217,3,54,27,0,217,218,3,52,26,0,218,51,1,0,0,0,219,220,5,10,0,0,
        220,221,3,54,27,0,221,222,3,52,26,0,222,233,1,0,0,0,223,224,5,11,
        0,0,224,225,3,54,27,0,225,226,3,52,26,0,226,233,1,0,0,0,227,228,
        5,12,0,0,228,229,3,54,27,0,229,230,3,52,26,0,230,233,1,0,0,0,231,
        233,1,0,0,0,232,219,1,0,0,0,232,223,1,0,0,0,232,227,1,0,0,0,232,
        231,1,0,0,0,233,53,1,0,0,0,234,242,5,22,0,0,235,242,5,35,0,0,236,
        242,3,14,7,0,237,238,5,1,0,0,238,239,3,46,23,0,239,240,5,2,0,0,240,
        242,1,0,0,0,241,234,1,0,0,0,241,235,1,0,0,0,241,236,1,0,0,0,241,
        237,1,0,0,0,242,55,1,0,0,0,243,244,5,29,0,0,244,245,5,1,0,0,245,
        246,3,64,32,0,246,252,5,2,0,0,247,248,5,3,0,0,248,249,3,20,10,0,
        249,250,5,4,0,0,250,253,1,0,0,0,251,253,3,22,11,0,252,247,1,0,0,
        0,252,251,1,0,0,0,253,57,1,0,0,0,254,255,5,31,0,0,255,256,5,1,0,
        0,256,257,3,64,32,0,257,263,5,2,0,0,258,259,5,3,0,0,259,260,3,20,
        10,0,260,261,5,4,0,0,261,264,1,0,0,0,262,264,3,22,11,0,263,258,1,
        0,0,0,263,262,1,0,0,0,264,59,1,0,0,0,265,266,5,30,0,0,266,267,5,
        1,0,0,267,268,3,62,31,0,268,269,5,5,0,0,269,270,3,64,32,0,270,271,
        5,5,0,0,271,272,3,66,33,0,272,278,5,2,0,0,273,274,5,3,0,0,274,275,
        3,20,10,0,275,276,5,4,0,0,276,279,1,0,0,0,277,279,3,22,11,0,278,
        273,1,0,0,0,278,277,1,0,0,0,279,61,1,0,0,0,280,281,5,35,0,0,281,
        282,5,13,0,0,282,294,3,34,17,0,283,284,3,2,1,0,284,285,5,35,0,0,
        285,294,1,0,0,0,286,287,3,2,1,0,287,288,5,35,0,0,288,289,5,13,0,
        0,289,290,3,34,17,0,290,294,1,0,0,0,291,294,3,34,17,0,292,294,1,
        0,0,0,293,280,1,0,0,0,293,283,1,0,0,0,293,286,1,0,0,0,293,291,1,
        0,0,0,293,292,1,0,0,0,294,63,1,0,0,0,295,296,3,34,17,0,296,65,1,
        0,0,0,297,298,5,35,0,0,298,299,5,13,0,0,299,303,3,34,17,0,300,303,
        3,34,17,0,301,303,1,0,0,0,302,297,1,0,0,0,302,300,1,0,0,0,302,301,
        1,0,0,0,303,67,1,0,0,0,21,77,83,100,107,118,125,131,141,150,162,
        183,193,200,214,232,241,252,263,278,293,302
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
    RULE_tfuncion = 2
    RULE_programa = 3
    RULE_funcion = 4
    RULE_parametros = 5
    RULE_parametrosp = 6
    RULE_usofuncion = 7
    RULE_argumentos = 8
    RULE_argumentosp = 9
    RULE_instrucciones = 10
    RULE_instruccion = 11
    RULE_bloque = 12
    RULE_icontrol = 13
    RULE_declaracion = 14
    RULE_asignacion = 15
    RULE_return = 16
    RULE_opal = 17
    RULE_lor = 18
    RULE_lorp = 19
    RULE_land = 20
    RULE_landp = 21
    RULE_comp = 22
    RULE_exp = 23
    RULE_e = 24
    RULE_term = 25
    RULE_t = 26
    RULE_factor = 27
    RULE_iwhile = 28
    RULE_iif = 29
    RULE_ifor = 30
    RULE_init = 31
    RULE_cond = 32
    RULE_iter = 33

    ruleNames =  [ "comparadores", "tdato", "tfuncion", "programa", "funcion", 
                   "parametros", "parametrosp", "usofuncion", "argumentos", 
                   "argumentosp", "instrucciones", "instruccion", "bloque", 
                   "icontrol", "declaracion", "asignacion", "return", "opal", 
                   "lor", "lorp", "land", "landp", "comp", "exp", "e", "term", 
                   "t", "factor", "iwhile", "iif", "ifor", "init", "cond", 
                   "iter" ]

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
            self.state = 68
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
            self.state = 70
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 92274688) != 0)):
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


    class TfuncionContext(ParserRuleContext):
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
            return compiladoresParser.RULE_tfuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTfuncion" ):
                listener.enterTfuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTfuncion" ):
                listener.exitTfuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTfuncion" ):
                return visitor.visitTfuncion(self)
            else:
                return visitor.visitChildren(self)




    def tfuncion(self):

        localctx = compiladoresParser.TfuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tfuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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
        self.enterRule(localctx, 6, self.RULE_programa)
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 360710144) != 0):
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

        def tfuncion(self):
            return self.getTypedRuleContext(compiladoresParser.TfuncionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.tfuncion()
            self.state = 89
            self.match(compiladoresParser.ID)
            self.state = 90
            self.match(compiladoresParser.PA)
            self.state = 91
            self.parametros()
            self.state = 92
            self.match(compiladoresParser.PC)
            self.state = 93
            self.bloque()
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
        self.enterRule(localctx, 10, self.RULE_parametros)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.tdato()
                self.state = 96
                self.match(compiladoresParser.ID)
                self.state = 97
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
        self.enterRule(localctx, 12, self.RULE_parametrosp)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(compiladoresParser.COMA)
                self.state = 103
                self.parametros()
                self.state = 104
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
        self.enterRule(localctx, 14, self.RULE_usofuncion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(compiladoresParser.ID)
            self.state = 110
            self.match(compiladoresParser.PA)

            self.state = 111
            self.argumentos()
            self.state = 112
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


        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        self.enterRule(localctx, 16, self.RULE_argumentos)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.opal()
                self.state = 115
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
        self.enterRule(localctx, 18, self.RULE_argumentosp)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(compiladoresParser.COMA)
                self.state = 121
                self.argumentos()
                self.state = 122
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
        self.enterRule(localctx, 20, self.RULE_instrucciones)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 22, 23, 24, 26, 29, 30, 31, 33, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.instruccion()
                self.state = 128
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


        def icontrol(self):
            return self.getTypedRuleContext(compiladoresParser.IcontrolContext,0)


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
        self.enterRule(localctx, 22, self.RULE_instruccion)
        try:
            self.state = 141
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.declaracion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.icontrol()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 135
                self.bloque()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                self.asignacion()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 137
                self.usofuncion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 138
                self.opal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 139
                self.return_()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 140
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
        self.enterRule(localctx, 24, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(compiladoresParser.LLA)
            self.state = 144
            self.instrucciones()
            self.state = 145
            self.match(compiladoresParser.LLC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IcontrolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_icontrol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIcontrol" ):
                listener.enterIcontrol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIcontrol" ):
                listener.exitIcontrol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIcontrol" ):
                return visitor.visitIcontrol(self)
            else:
                return visitor.visitChildren(self)




    def icontrol(self):

        localctx = compiladoresParser.IcontrolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_icontrol)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.iwhile()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.ifor()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.iif()
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
        self.enterRule(localctx, 28, self.RULE_declaracion)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.tdato()
                self.state = 153
                self.match(compiladoresParser.ID)
                self.state = 154
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.tdato()
                self.state = 157
                self.match(compiladoresParser.ID)
                self.state = 158
                self.match(compiladoresParser.ASIG)
                self.state = 159
                self.opal()
                self.state = 160
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
        self.enterRule(localctx, 30, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(compiladoresParser.ID)
            self.state = 165
            self.match(compiladoresParser.ASIG)
            self.state = 166
            self.opal()
            self.state = 167
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
        self.enterRule(localctx, 32, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(compiladoresParser.RETURN)
            self.state = 170
            self.opal()
            self.state = 171
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
        self.enterRule(localctx, 34, self.RULE_opal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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
        self.enterRule(localctx, 36, self.RULE_lor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.land()
            self.state = 176
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
        self.enterRule(localctx, 38, self.RULE_lorp)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(compiladoresParser.OR)
                self.state = 179
                self.land()
                self.state = 180
                self.lorp()
                pass
            elif token in [1, 2, 3, 4, 5, 7, 22, 23, 24, 26, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 40, self.RULE_land)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.comp()
            self.state = 186
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
        self.enterRule(localctx, 42, self.RULE_landp)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(compiladoresParser.AND)
                self.state = 189
                self.comp()
                self.state = 190
                self.landp()
                pass
            elif token in [1, 2, 3, 4, 5, 7, 15, 22, 23, 24, 26, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 44, self.RULE_comp)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.exp()
                self.state = 196
                self.comparadores()
                self.state = 197
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
        self.enterRule(localctx, 46, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.term()
            self.state = 203
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
        self.enterRule(localctx, 48, self.RULE_e)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(compiladoresParser.SUMA)
                self.state = 206
                self.term()
                self.state = 207
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.match(compiladoresParser.RESTA)
                self.state = 210
                self.term()
                self.state = 211
                self.e()
                pass
            elif token in [1, 2, 3, 4, 5, 7, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 50, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.factor()
            self.state = 217
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
        self.enterRule(localctx, 52, self.RULE_t)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(compiladoresParser.MULT)
                self.state = 220
                self.factor()
                self.state = 221
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.match(compiladoresParser.DIV)
                self.state = 224
                self.factor()
                self.state = 225
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(compiladoresParser.MOD)
                self.state = 228
                self.factor()
                self.state = 229
                self.t()
                pass
            elif token in [1, 2, 3, 4, 5, 7, 8, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 29, 30, 31, 33, 35]:
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
        self.enterRule(localctx, 54, self.RULE_factor)
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.match(compiladoresParser.PA)
                self.state = 238
                self.exp()
                self.state = 239
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
        self.enterRule(localctx, 56, self.RULE_iwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(compiladoresParser.WHILE)
            self.state = 244
            self.match(compiladoresParser.PA)
            self.state = 245
            self.cond()
            self.state = 246
            self.match(compiladoresParser.PC)
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 247
                self.match(compiladoresParser.LLA)
                self.state = 248
                self.instrucciones()
                self.state = 249
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.state = 251
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
        self.enterRule(localctx, 58, self.RULE_iif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(compiladoresParser.IF)
            self.state = 255
            self.match(compiladoresParser.PA)
            self.state = 256
            self.cond()
            self.state = 257
            self.match(compiladoresParser.PC)
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(compiladoresParser.LLA)
                self.state = 259
                self.instrucciones()
                self.state = 260
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.state = 262
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
        self.enterRule(localctx, 60, self.RULE_ifor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(compiladoresParser.FOR)
            self.state = 266
            self.match(compiladoresParser.PA)
            self.state = 267
            self.init()
            self.state = 268
            self.match(compiladoresParser.PYC)
            self.state = 269
            self.cond()
            self.state = 270
            self.match(compiladoresParser.PYC)
            self.state = 271
            self.iter_()
            self.state = 272
            self.match(compiladoresParser.PC)
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 273
                self.match(compiladoresParser.LLA)
                self.state = 274
                self.instrucciones()
                self.state = 275
                self.match(compiladoresParser.LLC)
                pass

            elif la_ == 2:
                self.state = 277
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
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(compiladoresParser.ID)
                self.state = 281
                self.match(compiladoresParser.ASIG)
                self.state = 282
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.tdato()
                self.state = 284
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.tdato()
                self.state = 287
                self.match(compiladoresParser.ID)
                self.state = 288
                self.match(compiladoresParser.ASIG)
                self.state = 289
                self.opal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 291
                self.opal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

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
            self.state = 295
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

        def ID(self):
            return self.getToken(compiladoresParser.ID, 0)

        def ASIG(self):
            return self.getToken(compiladoresParser.ASIG, 0)

        def opal(self):
            return self.getTypedRuleContext(compiladoresParser.OpalContext,0)


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
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(compiladoresParser.ID)
                self.state = 298
                self.match(compiladoresParser.ASIG)
                self.state = 299
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.opal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





