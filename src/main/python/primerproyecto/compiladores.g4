grammar compiladores;

fragment LETRA : [A-Za-z] ;
fragment DIGITO : [0-9] ;

// INST : (LETRA | DIGITO | [- ,;{}()+=>] )+ '\n' ;

//CARACTERES ESPECIALES
PA  : '(' ;
PC  : ')' ;
LLA : '{' ;
LLC : '}' ;
PYC : ';' ;
PUNTO : '.';
COMA : ',';
//OPERACIONES

// ARITMETICAS
SUMA  : '+' ;
RESTA : '-' ;
MULT  : '*' ;
DIV   : '/' ;
MOD   : '%' ;
ASIG  : '=' ;

INCRE : '++' ;
DECRE : '--' ;

SUMAIGUAL : '+=' ;
RESTAIGUAL : '-=' ;


//LOGICAS
AND : '&&';
OR : '||';


//COMPARADORES
MENOR : '<' ;
MAYOR : '>' ;
IGUAL : '==' ;
MENORIG : '<=';
MAYORIG : '>=';
DIF: '=!' ;

comparadores : MENOR | MAYOR | IGUAL | MENORIG | MAYORIG | DIF;

NUMERO : ENTERO
        | DECIMAL
        ;

//TIPO DE DATO
INT   : 'int' ;
DOUBLE : 'double';
CHAR : 'char';

//FUNCIONES
VOID : 'void';
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;
ELSE  : 'else';
RETURN : 'return';

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
ENTERO : DIGITO+;
DECIMAL : DIGITO+ PUNTO DIGITO+; 


WS : [ \t\n\r] -> skip;

tdato: INT | DOUBLE | CHAR;
tfuncion : INT | DOUBLE | CHAR | VOID;

programa : instrucciones EOF ;
//programa : (declaraciones PYC)* prototipo* funcion* EOF ;

prototipo: tfuncion ID PA parametros PC PYC;

funcion : tfuncion ID PA parametros PC bloque;

parametros : tdato ID parametrosp
            | 
            ;

parametrosp : COMA parametros parametrosp
            | 
            ;

usofuncion : ID PA (argumentos) PC;



argumentos : (opal) argumentosp
            |;
argumentosp : COMA argumentos argumentosp 
            |;

instrucciones : instruccion instrucciones
              |
              ;


instruccion : declaraciones PYC
            | funcion
            | prototipo     
            | bloque
            | asignacion PYC
            | usofuncion PYC
            | opal PYC
            | return  PYC
            | ifor
            | iwhile
            | iif
            | PYC
            ;

bloque : LLA instrucciones LLC ;

declaraciones : declaracion  declaracionp;

declaracion : tdato ID ((ASIG|RESTAIGUAL|SUMAIGUAL) opal)?;

declaracionp : COMA ID ((ASIG|RESTAIGUAL|SUMAIGUAL) opal)? declaracionp
              |
              ;

asignacion : ID ASIG opal;

return : RETURN opal;

// Operacion aritmetica o logica
opal : lor;

// Logico AND
lor : land lorp;

//Logico OR prima
lorp: OR land lorp
  | 
  ;

//Logico AND
land : comp landp;

//Logico AND prima
landp : AND comp landp 
  |
  ;

// Comparacion 
comp : exp comparadores exp
  | exp;

// Expresion aritmetica
exp : term e ;

e   : SUMA  term e
    | RESTA term e
    |
    ;

term : factor t ;
t    : MULT factor t
     | DIV  factor t
     | MOD  factor t
     |
     ;

factor : NUMERO
       | ID
       | usofuncion
       | PA exp PC
       | ID (DECRE|INCRE)
       ;

iwhile : WHILE PA cond PC instruccion ;

iif : IF PA cond PC instruccion 
      | IF PA cond PC instruccion ielse;

ielse: ELSE instruccion ;

ifor : FOR PA init PYC cond PYC iter PC instruccion ;

init : (asignacion|opal) (COMA (asignacion|opal))*
      |
      ;

cond : opal
      |;

iter : (asignacion|opal) (COMA (asignacion|opal))*
      |;
