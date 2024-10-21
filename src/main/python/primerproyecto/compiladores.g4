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
LONG : 'long';
CHAR : 'char';
STRING : 'string';

//FUNCIONES
VOID : 'void';
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;
ELSE : 'else';
RETURN : 'return';
DO : 'do';

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
ENTERO : DIGITO+;
DECIMAL : DIGITO+ PUNTO DIGITO+; 


WS : [ \t\n\r] -> skip;

tdato : INT | DOUBLE | LONG | CHAR | STRING ;


programa : declaracion* funcion* EOF ;

funcion : funcionvoid | funcionreturn ;

funcionvoid : VOID ID PA parametros PC (bloque | PYC);

funcionreturn : tdato ID PA parametros PC (bloquereturn | PYC);

bloquereturn : LLA (instrucciones RETURN |  RETURN) opal PYC LLC ;

parametros : tdato ID parametrosp
            | 
            ;

parametrosp : COMA parametros parametrosp
            | 
            ;

usofuncion : ID PA (argumentos) PC;

argumentos : opal argumentosp
            |;
argumentosp : COMA argumentos argumentosp 
            |;

instrucciones : instruccion instrucciones
              |
              ;


instruccion : declaracion
            | iwhile
            | ifor
            | iif
            | bloque
            | asignacion 
            | usofuncion
            | PYC
            ;

declaracion : tdato ID PYC 
            | tdato asignacion;

asignacion : ID ASIG (usofuncion|opal) PYC;

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
       ;

iwhile : WHILE PA cond PC (bloque | instruccion) ;

bloque : LLA instrucciones LLC ;

iif : IF PA cond PC (bloque | instruccion)  ;

ifor : FOR PA init PYC cond PYC iter PC (bloque | instruccion) ;

init : ID ASIG (usofuncion|opal)
      | ID
      | tdato ID
      | tdato ID ASIG (usofuncion|opal)
      ;

cond : opal;

iter : (ID|NUMERO) ASIG exp;

ido: DO (bloque|instruccion) WHILE PA opal PC PYC ;
