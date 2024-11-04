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
CHAR : 'char';

//FUNCIONES
VOID : 'void';
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;
RETURN : 'return';

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
ENTERO : DIGITO+;
DECIMAL : DIGITO+ PUNTO DIGITO+; 


WS : [ \t\n\r] -> skip;

tdato: INT | DOUBLE | CHAR;
tfuncion : INT | DOUBLE | CHAR | VOID;


programa : declaracion* funcion* EOF ;

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


instruccion : declaracion
            | icontrol
            | bloque
            | asignacion 
            | usofuncion
            | opal
            | return
            | PYC
            ;

bloque : LLA instrucciones LLC ;

icontrol: iwhile
        | ifor
        | iif;

declaracion : tdato ID PYC 
            | tdato ID ASIG opal PYC;

asignacion : ID ASIG opal PYC;

return : RETURN opal PYC;

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

iwhile : WHILE PA cond PC (LLA instrucciones LLC | instruccion) ;


iif : IF PA cond PC (LLA instrucciones LLC | instruccion)  ;

ifor : FOR PA init PYC cond PYC iter PC (LLA instrucciones LLC | instruccion) ;

init : ID ASIG opal
      | tdato ID
      | tdato ID ASIG opal
      | opal
      |
      ;

cond : opal;

iter : ID ASIG opal
      | opal
      |;
