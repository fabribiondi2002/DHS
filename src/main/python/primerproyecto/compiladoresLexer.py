# Generated from /home/fabri/Escritorio/dhs/proyecto/primerproyeco/src/main/python/primerproyecto/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,31,188,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,
        7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,
        14,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,
        19,1,19,1,20,1,20,3,20,114,8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,3,29,159,8,
        29,1,29,1,29,1,29,5,29,164,8,29,10,29,12,29,167,9,29,1,30,4,30,170,
        8,30,11,30,12,30,171,1,31,4,31,175,8,31,11,31,12,31,176,1,31,1,31,
        4,31,181,8,31,11,31,12,31,182,1,32,1,32,1,32,1,32,0,0,33,1,0,3,0,
        5,1,7,2,9,3,11,4,13,5,15,6,17,7,19,8,21,9,23,10,25,11,27,12,29,13,
        31,14,33,15,35,16,37,17,39,18,41,19,43,20,45,21,47,22,49,23,51,24,
        53,25,55,26,57,27,59,28,61,29,63,30,65,31,1,0,3,2,0,65,90,97,122,
        1,0,48,57,3,0,9,10,13,13,32,32,193,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,
        0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,
        0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,
        0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,
        0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,
        0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,
        0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,1,67,1,0,0,0,3,69,1,
        0,0,0,5,71,1,0,0,0,7,73,1,0,0,0,9,75,1,0,0,0,11,77,1,0,0,0,13,79,
        1,0,0,0,15,81,1,0,0,0,17,83,1,0,0,0,19,85,1,0,0,0,21,87,1,0,0,0,
        23,89,1,0,0,0,25,91,1,0,0,0,27,93,1,0,0,0,29,95,1,0,0,0,31,97,1,
        0,0,0,33,99,1,0,0,0,35,102,1,0,0,0,37,105,1,0,0,0,39,108,1,0,0,0,
        41,113,1,0,0,0,43,115,1,0,0,0,45,119,1,0,0,0,47,126,1,0,0,0,49,131,
        1,0,0,0,51,136,1,0,0,0,53,143,1,0,0,0,55,149,1,0,0,0,57,153,1,0,
        0,0,59,158,1,0,0,0,61,169,1,0,0,0,63,174,1,0,0,0,65,184,1,0,0,0,
        67,68,7,0,0,0,68,2,1,0,0,0,69,70,7,1,0,0,70,4,1,0,0,0,71,72,5,40,
        0,0,72,6,1,0,0,0,73,74,5,41,0,0,74,8,1,0,0,0,75,76,5,123,0,0,76,
        10,1,0,0,0,77,78,5,125,0,0,78,12,1,0,0,0,79,80,5,59,0,0,80,14,1,
        0,0,0,81,82,5,46,0,0,82,16,1,0,0,0,83,84,5,43,0,0,84,18,1,0,0,0,
        85,86,5,45,0,0,86,20,1,0,0,0,87,88,5,42,0,0,88,22,1,0,0,0,89,90,
        5,47,0,0,90,24,1,0,0,0,91,92,5,37,0,0,92,26,1,0,0,0,93,94,5,61,0,
        0,94,28,1,0,0,0,95,96,5,60,0,0,96,30,1,0,0,0,97,98,5,62,0,0,98,32,
        1,0,0,0,99,100,5,61,0,0,100,101,5,61,0,0,101,34,1,0,0,0,102,103,
        5,60,0,0,103,104,5,61,0,0,104,36,1,0,0,0,105,106,5,62,0,0,106,107,
        5,61,0,0,107,38,1,0,0,0,108,109,5,61,0,0,109,110,5,33,0,0,110,40,
        1,0,0,0,111,114,3,61,30,0,112,114,3,63,31,0,113,111,1,0,0,0,113,
        112,1,0,0,0,114,42,1,0,0,0,115,116,5,105,0,0,116,117,5,110,0,0,117,
        118,5,116,0,0,118,44,1,0,0,0,119,120,5,100,0,0,120,121,5,111,0,0,
        121,122,5,117,0,0,122,123,5,98,0,0,123,124,5,108,0,0,124,125,5,101,
        0,0,125,46,1,0,0,0,126,127,5,108,0,0,127,128,5,111,0,0,128,129,5,
        110,0,0,129,130,5,103,0,0,130,48,1,0,0,0,131,132,5,99,0,0,132,133,
        5,104,0,0,133,134,5,97,0,0,134,135,5,114,0,0,135,50,1,0,0,0,136,
        137,5,115,0,0,137,138,5,116,0,0,138,139,5,114,0,0,139,140,5,105,
        0,0,140,141,5,110,0,0,141,142,5,103,0,0,142,52,1,0,0,0,143,144,5,
        119,0,0,144,145,5,104,0,0,145,146,5,105,0,0,146,147,5,108,0,0,147,
        148,5,101,0,0,148,54,1,0,0,0,149,150,5,102,0,0,150,151,5,111,0,0,
        151,152,5,114,0,0,152,56,1,0,0,0,153,154,5,105,0,0,154,155,5,102,
        0,0,155,58,1,0,0,0,156,159,3,1,0,0,157,159,5,95,0,0,158,156,1,0,
        0,0,158,157,1,0,0,0,159,165,1,0,0,0,160,164,3,1,0,0,161,164,3,3,
        1,0,162,164,5,95,0,0,163,160,1,0,0,0,163,161,1,0,0,0,163,162,1,0,
        0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,60,1,0,0,
        0,167,165,1,0,0,0,168,170,3,3,1,0,169,168,1,0,0,0,170,171,1,0,0,
        0,171,169,1,0,0,0,171,172,1,0,0,0,172,62,1,0,0,0,173,175,3,3,1,0,
        174,173,1,0,0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,
        177,178,1,0,0,0,178,180,3,15,7,0,179,181,3,3,1,0,180,179,1,0,0,0,
        181,182,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,64,1,0,0,0,184,
        185,7,2,0,0,185,186,1,0,0,0,186,187,6,32,0,0,187,66,1,0,0,0,8,0,
        113,158,163,165,171,176,182,1,6,0,0
    ]

class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PA = 1
    PC = 2
    LLA = 3
    LLC = 4
    PYC = 5
    PUNTO = 6
    SUMA = 7
    RESTA = 8
    MULT = 9
    DIV = 10
    MOD = 11
    ASIG = 12
    MENOR = 13
    MAYOR = 14
    IGUAL = 15
    MENORIG = 16
    MAYORIG = 17
    DIF = 18
    NUMERO = 19
    INT = 20
    DOUBLE = 21
    LONG = 22
    CHAR = 23
    STRING = 24
    WHILE = 25
    FOR = 26
    IF = 27
    ID = 28
    ENTERO = 29
    DECIMAL = 30
    WS = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'.'", "'+'", "'-'", "'*'", 
            "'/'", "'%'", "'='", "'<'", "'>'", "'=='", "'<='", "'>='", "'=!'", 
            "'int'", "'double'", "'long'", "'char'", "'string'", "'while'", 
            "'for'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "PA", "PC", "LLA", "LLC", "PYC", "PUNTO", "SUMA", "RESTA", "MULT", 
            "DIV", "MOD", "ASIG", "MENOR", "MAYOR", "IGUAL", "MENORIG", 
            "MAYORIG", "DIF", "NUMERO", "INT", "DOUBLE", "LONG", "CHAR", 
            "STRING", "WHILE", "FOR", "IF", "ID", "ENTERO", "DECIMAL", "WS" ]

    ruleNames = [ "LETRA", "DIGITO", "PA", "PC", "LLA", "LLC", "PYC", "PUNTO", 
                  "SUMA", "RESTA", "MULT", "DIV", "MOD", "ASIG", "MENOR", 
                  "MAYOR", "IGUAL", "MENORIG", "MAYORIG", "DIF", "NUMERO", 
                  "INT", "DOUBLE", "LONG", "CHAR", "STRING", "WHILE", "FOR", 
                  "IF", "ID", "ENTERO", "DECIMAL", "WS" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


