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
        4,1,35,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,5,3,78,8,3,10,3,12,3,81,
        9,3,1,3,5,3,84,8,3,10,3,12,3,87,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,103,8,5,1,6,1,6,1,6,1,6,1,6,3,6,
        110,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,121,8,8,1,9,1,9,
        1,9,1,9,1,9,3,9,128,8,9,1,10,1,10,1,10,1,10,3,10,134,8,10,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,3,11,156,8,11,1,12,1,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,170,8,13,1,14,1,14,1,
        14,1,14,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,18,3,18,189,8,18,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,3,
        20,199,8,20,1,21,1,21,1,21,1,21,1,21,3,21,206,8,21,1,22,1,22,1,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,220,8,23,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,
        1,25,1,25,3,25,238,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,
        247,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,268,8,28,1,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,
        3,31,285,8,31,1,32,1,32,1,33,1,33,1,33,1,33,1,33,3,33,294,8,33,1,
        33,0,0,34,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,0,3,1,0,16,21,1,0,23,25,
        1,0,23,26,293,0,68,1,0,0,0,2,70,1,0,0,0,4,72,1,0,0,0,6,79,1,0,0,
        0,8,90,1,0,0,0,10,102,1,0,0,0,12,109,1,0,0,0,14,111,1,0,0,0,16,120,
        1,0,0,0,18,127,1,0,0,0,20,133,1,0,0,0,22,155,1,0,0,0,24,157,1,0,
        0,0,26,169,1,0,0,0,28,171,1,0,0,0,30,175,1,0,0,0,32,178,1,0,0,0,
        34,180,1,0,0,0,36,188,1,0,0,0,38,190,1,0,0,0,40,198,1,0,0,0,42,205,
        1,0,0,0,44,207,1,0,0,0,46,219,1,0,0,0,48,221,1,0,0,0,50,237,1,0,
        0,0,52,246,1,0,0,0,54,248,1,0,0,0,56,267,1,0,0,0,58,269,1,0,0,0,
        60,272,1,0,0,0,62,284,1,0,0,0,64,286,1,0,0,0,66,293,1,0,0,0,68,69,
        7,0,0,0,69,1,1,0,0,0,70,71,7,1,0,0,71,3,1,0,0,0,72,73,7,2,0,0,73,
        5,1,0,0,0,74,75,3,26,13,0,75,76,5,5,0,0,76,78,1,0,0,0,77,74,1,0,
        0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,85,1,0,0,0,81,79,
        1,0,0,0,82,84,3,8,4,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,
        85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,0,0,1,89,7,1,0,
        0,0,90,91,3,4,2,0,91,92,5,32,0,0,92,93,5,1,0,0,93,94,3,10,5,0,94,
        95,5,2,0,0,95,96,3,24,12,0,96,9,1,0,0,0,97,98,3,2,1,0,98,99,5,32,
        0,0,99,100,3,12,6,0,100,103,1,0,0,0,101,103,1,0,0,0,102,97,1,0,0,
        0,102,101,1,0,0,0,103,11,1,0,0,0,104,105,5,7,0,0,105,106,3,10,5,
        0,106,107,3,12,6,0,107,110,1,0,0,0,108,110,1,0,0,0,109,104,1,0,0,
        0,109,108,1,0,0,0,110,13,1,0,0,0,111,112,5,32,0,0,112,113,5,1,0,
        0,113,114,3,16,8,0,114,115,5,2,0,0,115,15,1,0,0,0,116,117,3,32,16,
        0,117,118,3,18,9,0,118,121,1,0,0,0,119,121,1,0,0,0,120,116,1,0,0,
        0,120,119,1,0,0,0,121,17,1,0,0,0,122,123,5,7,0,0,123,124,3,16,8,
        0,124,125,3,18,9,0,125,128,1,0,0,0,126,128,1,0,0,0,127,122,1,0,0,
        0,127,126,1,0,0,0,128,19,1,0,0,0,129,130,3,22,11,0,130,131,3,20,
        10,0,131,134,1,0,0,0,132,134,1,0,0,0,133,129,1,0,0,0,133,132,1,0,
        0,0,134,21,1,0,0,0,135,136,3,26,13,0,136,137,5,5,0,0,137,156,1,0,
        0,0,138,156,3,24,12,0,139,140,3,28,14,0,140,141,5,5,0,0,141,156,
        1,0,0,0,142,143,3,14,7,0,143,144,5,5,0,0,144,156,1,0,0,0,145,146,
        3,32,16,0,146,147,5,5,0,0,147,156,1,0,0,0,148,149,3,30,15,0,149,
        150,5,5,0,0,150,156,1,0,0,0,151,156,3,60,30,0,152,156,3,54,27,0,
        153,156,3,56,28,0,154,156,5,5,0,0,155,135,1,0,0,0,155,138,1,0,0,
        0,155,139,1,0,0,0,155,142,1,0,0,0,155,145,1,0,0,0,155,148,1,0,0,
        0,155,151,1,0,0,0,155,152,1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,
        0,156,23,1,0,0,0,157,158,5,3,0,0,158,159,3,20,10,0,159,160,5,4,0,
        0,160,25,1,0,0,0,161,162,3,2,1,0,162,163,5,32,0,0,163,170,1,0,0,
        0,164,165,3,2,1,0,165,166,5,32,0,0,166,167,5,13,0,0,167,168,3,32,
        16,0,168,170,1,0,0,0,169,161,1,0,0,0,169,164,1,0,0,0,170,27,1,0,
        0,0,171,172,5,32,0,0,172,173,5,13,0,0,173,174,3,32,16,0,174,29,1,
        0,0,0,175,176,5,31,0,0,176,177,3,32,16,0,177,31,1,0,0,0,178,179,
        3,34,17,0,179,33,1,0,0,0,180,181,3,38,19,0,181,182,3,36,18,0,182,
        35,1,0,0,0,183,184,5,15,0,0,184,185,3,38,19,0,185,186,3,36,18,0,
        186,189,1,0,0,0,187,189,1,0,0,0,188,183,1,0,0,0,188,187,1,0,0,0,
        189,37,1,0,0,0,190,191,3,42,21,0,191,192,3,40,20,0,192,39,1,0,0,
        0,193,194,5,14,0,0,194,195,3,42,21,0,195,196,3,40,20,0,196,199,1,
        0,0,0,197,199,1,0,0,0,198,193,1,0,0,0,198,197,1,0,0,0,199,41,1,0,
        0,0,200,201,3,44,22,0,201,202,3,0,0,0,202,203,3,44,22,0,203,206,
        1,0,0,0,204,206,3,44,22,0,205,200,1,0,0,0,205,204,1,0,0,0,206,43,
        1,0,0,0,207,208,3,48,24,0,208,209,3,46,23,0,209,45,1,0,0,0,210,211,
        5,8,0,0,211,212,3,48,24,0,212,213,3,46,23,0,213,220,1,0,0,0,214,
        215,5,9,0,0,215,216,3,48,24,0,216,217,3,46,23,0,217,220,1,0,0,0,
        218,220,1,0,0,0,219,210,1,0,0,0,219,214,1,0,0,0,219,218,1,0,0,0,
        220,47,1,0,0,0,221,222,3,52,26,0,222,223,3,50,25,0,223,49,1,0,0,
        0,224,225,5,10,0,0,225,226,3,52,26,0,226,227,3,50,25,0,227,238,1,
        0,0,0,228,229,5,11,0,0,229,230,3,52,26,0,230,231,3,50,25,0,231,238,
        1,0,0,0,232,233,5,12,0,0,233,234,3,52,26,0,234,235,3,50,25,0,235,
        238,1,0,0,0,236,238,1,0,0,0,237,224,1,0,0,0,237,228,1,0,0,0,237,
        232,1,0,0,0,237,236,1,0,0,0,238,51,1,0,0,0,239,247,5,22,0,0,240,
        247,5,32,0,0,241,247,3,14,7,0,242,243,5,1,0,0,243,244,3,44,22,0,
        244,245,5,2,0,0,245,247,1,0,0,0,246,239,1,0,0,0,246,240,1,0,0,0,
        246,241,1,0,0,0,246,242,1,0,0,0,247,53,1,0,0,0,248,249,5,27,0,0,
        249,250,5,1,0,0,250,251,3,64,32,0,251,252,5,2,0,0,252,253,3,22,11,
        0,253,55,1,0,0,0,254,255,5,29,0,0,255,256,5,1,0,0,256,257,3,64,32,
        0,257,258,5,2,0,0,258,259,3,22,11,0,259,268,1,0,0,0,260,261,5,29,
        0,0,261,262,5,1,0,0,262,263,3,64,32,0,263,264,5,2,0,0,264,265,3,
        22,11,0,265,266,3,58,29,0,266,268,1,0,0,0,267,254,1,0,0,0,267,260,
        1,0,0,0,268,57,1,0,0,0,269,270,5,30,0,0,270,271,3,22,11,0,271,59,
        1,0,0,0,272,273,5,28,0,0,273,274,5,1,0,0,274,275,3,62,31,0,275,276,
        5,5,0,0,276,277,3,64,32,0,277,278,5,5,0,0,278,279,3,66,33,0,279,
        280,5,2,0,0,280,281,3,22,11,0,281,61,1,0,0,0,282,285,3,28,14,0,283,
        285,1,0,0,0,284,282,1,0,0,0,284,283,1,0,0,0,285,63,1,0,0,0,286,287,
        3,32,16,0,287,65,1,0,0,0,288,289,5,32,0,0,289,290,5,13,0,0,290,294,
        3,32,16,0,291,294,3,32,16,0,292,294,1,0,0,0,293,288,1,0,0,0,293,
        291,1,0,0,0,293,292,1,0,0,0,294,67,1,0,0,0,18,79,85,102,109,120,
        127,133,155,169,188,198,205,219,237,246,267,284,293
    ]

class compiladoresParser ( Parser ):

    grammarFileName = "compiladores.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'.'", 
                     "','", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'&&'", 
                     "'||'", "'<'", "'>'", "'=='", "'<='", "'>='", "'=!'", 
                     "<INVALID>", "'int'", "'double'", "'char'", "'void'", 
                     "'while'", "'for'", "'if'", "'else'", "'return'" ]

    symbolicNames = [ "<INVALID>", "PA", "PC", "LLA", "LLC", "PYC", "PUNTO", 
                      "COMA", "SUMA", "RESTA", "MULT", "DIV", "MOD", "ASIG", 
                      "AND", "OR", "MENOR", "MAYOR", "IGUAL", "MENORIG", 
                      "MAYORIG", "DIF", "NUMERO", "INT", "DOUBLE", "CHAR", 
                      "VOID", "WHILE", "FOR", "IF", "ELSE", "RETURN", "ID", 
                      "ENTERO", "DECIMAL", "WS" ]

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
    RULE_declaracion = 13
    RULE_asignacion = 14
    RULE_return = 15
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
    RULE_iif = 28
    RULE_ielse = 29
    RULE_ifor = 30
    RULE_init = 31
    RULE_cond = 32
    RULE_iter = 33

    ruleNames =  [ "comparadores", "tdato", "tfuncion", "programa", "funcion", 
                   "parametros", "parametrosp", "usofuncion", "argumentos", 
                   "argumentosp", "instrucciones", "instruccion", "bloque", 
                   "declaracion", "asignacion", "return", "opal", "lor", 
                   "lorp", "land", "landp", "comp", "exp", "e", "term", 
                   "t", "factor", "iwhile", "iif", "ielse", "ifor", "init", 
                   "cond", "iter" ]

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
    CHAR=25
    VOID=26
    WHILE=27
    FOR=28
    IF=29
    ELSE=30
    RETURN=31
    ID=32
    ENTERO=33
    DECIMAL=34
    WS=35

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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
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


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(compiladoresParser.PYC)
            else:
                return self.getToken(compiladoresParser.PYC, i)

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
            self.state = 79
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 74
                    self.declaracion()
                    self.state = 75
                    self.match(compiladoresParser.PYC) 
                self.state = 81
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 82
                self.funcion()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
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
            self.state = 90
            self.tfuncion()
            self.state = 91
            self.match(compiladoresParser.ID)
            self.state = 92
            self.match(compiladoresParser.PA)
            self.state = 93
            self.parametros()
            self.state = 94
            self.match(compiladoresParser.PC)
            self.state = 95
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
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.tdato()
                self.state = 98
                self.match(compiladoresParser.ID)
                self.state = 99
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(compiladoresParser.COMA)
                self.state = 105
                self.parametros()
                self.state = 106
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
            self.state = 111
            self.match(compiladoresParser.ID)
            self.state = 112
            self.match(compiladoresParser.PA)

            self.state = 113
            self.argumentos()
            self.state = 114
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
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 22, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.opal()
                self.state = 117
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(compiladoresParser.COMA)
                self.state = 123
                self.argumentos()
                self.state = 124
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
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 5, 22, 23, 24, 25, 27, 28, 29, 31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.instruccion()
                self.state = 130
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


        def PYC(self):
            return self.getToken(compiladoresParser.PYC, 0)

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


        def ifor(self):
            return self.getTypedRuleContext(compiladoresParser.IforContext,0)


        def iwhile(self):
            return self.getTypedRuleContext(compiladoresParser.IwhileContext,0)


        def iif(self):
            return self.getTypedRuleContext(compiladoresParser.IifContext,0)


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
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.declaracion()
                self.state = 136
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.bloque()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.asignacion()
                self.state = 140
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.usofuncion()
                self.state = 143
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 145
                self.opal()
                self.state = 146
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.return_()
                self.state = 149
                self.match(compiladoresParser.PYC)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.ifor()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 152
                self.iwhile()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 153
                self.iif()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
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
            self.state = 157
            self.match(compiladoresParser.LLA)
            self.state = 158
            self.instrucciones()
            self.state = 159
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
        self.enterRule(localctx, 26, self.RULE_declaracion)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.tdato()
                self.state = 162
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.tdato()
                self.state = 165
                self.match(compiladoresParser.ID)
                self.state = 166
                self.match(compiladoresParser.ASIG)
                self.state = 167
                self.opal()
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
        self.enterRule(localctx, 28, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(compiladoresParser.ID)
            self.state = 172
            self.match(compiladoresParser.ASIG)
            self.state = 173
            self.opal()
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
        self.enterRule(localctx, 30, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(compiladoresParser.RETURN)
            self.state = 176
            self.opal()
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
            self.state = 178
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
            self.state = 180
            self.land()
            self.state = 181
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
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(compiladoresParser.OR)
                self.state = 184
                self.land()
                self.state = 185
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
            self.state = 190
            self.comp()
            self.state = 191
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
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(compiladoresParser.AND)
                self.state = 194
                self.comp()
                self.state = 195
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
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.exp()
                self.state = 201
                self.comparadores()
                self.state = 202
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
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
            self.state = 207
            self.term()
            self.state = 208
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
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(compiladoresParser.SUMA)
                self.state = 211
                self.term()
                self.state = 212
                self.e()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(compiladoresParser.RESTA)
                self.state = 215
                self.term()
                self.state = 216
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
            self.state = 221
            self.factor()
            self.state = 222
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.match(compiladoresParser.MULT)
                self.state = 225
                self.factor()
                self.state = 226
                self.t()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(compiladoresParser.DIV)
                self.state = 229
                self.factor()
                self.state = 230
                self.t()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.match(compiladoresParser.MOD)
                self.state = 233
                self.factor()
                self.state = 234
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
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(compiladoresParser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(compiladoresParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.usofuncion()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.match(compiladoresParser.PA)
                self.state = 243
                self.exp()
                self.state = 244
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
            self.state = 248
            self.match(compiladoresParser.WHILE)
            self.state = 249
            self.match(compiladoresParser.PA)
            self.state = 250
            self.cond()
            self.state = 251
            self.match(compiladoresParser.PC)
            self.state = 252
            self.instruccion()
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

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def ielse(self):
            return self.getTypedRuleContext(compiladoresParser.IelseContext,0)


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
        self.enterRule(localctx, 56, self.RULE_iif)
        try:
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(compiladoresParser.IF)
                self.state = 255
                self.match(compiladoresParser.PA)
                self.state = 256
                self.cond()
                self.state = 257
                self.match(compiladoresParser.PC)
                self.state = 258
                self.instruccion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(compiladoresParser.IF)
                self.state = 261
                self.match(compiladoresParser.PA)
                self.state = 262
                self.cond()
                self.state = 263
                self.match(compiladoresParser.PC)
                self.state = 264
                self.instruccion()
                self.state = 265
                self.ielse()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IelseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(compiladoresParser.ELSE, 0)

        def instruccion(self):
            return self.getTypedRuleContext(compiladoresParser.InstruccionContext,0)


        def getRuleIndex(self):
            return compiladoresParser.RULE_ielse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIelse" ):
                listener.enterIelse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIelse" ):
                listener.exitIelse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIelse" ):
                return visitor.visitIelse(self)
            else:
                return visitor.visitChildren(self)




    def ielse(self):

        localctx = compiladoresParser.IelseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_ielse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(compiladoresParser.ELSE)
            self.state = 270
            self.instruccion()
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
            self.state = 272
            self.match(compiladoresParser.FOR)
            self.state = 273
            self.match(compiladoresParser.PA)
            self.state = 274
            self.init()
            self.state = 275
            self.match(compiladoresParser.PYC)
            self.state = 276
            self.cond()
            self.state = 277
            self.match(compiladoresParser.PYC)
            self.state = 278
            self.iter_()
            self.state = 279
            self.match(compiladoresParser.PC)
            self.state = 280
            self.instruccion()
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

        def asignacion(self):
            return self.getTypedRuleContext(compiladoresParser.AsignacionContext,0)


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
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.asignacion()
                pass
            elif token in [5]:
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
            self.state = 286
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
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(compiladoresParser.ID)
                self.state = 289
                self.match(compiladoresParser.ASIG)
                self.state = 290
                self.opal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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





