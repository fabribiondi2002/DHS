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
WHILE : 'while' ;
FOR   : 'for' ;
IF    : 'if' ;

ID : (LETRA | '_')(LETRA | DIGITO | '_')* ;
ENTERO : DIGITO+;
DECIMAL : DIGITO+ PUNTO DIGITO+; 


WS : [ \t\n\r] -> skip;
// OTRO : . ;

// s : ID     {print("ID ->" + $ID.text + "<--") }         s
//   | NUMERO {print("NUMERO ->" + $NUMERO.text + "<--") } s
//   | WHILE  {print("WHILE ->" + $WHILE.text + "<--") }   s
  // | OTRO   {print("Otro ->" + $OTRO.text + "<--") }     s
  // | EOF
  // ;

// si : s EOF ;

// s : PA s PC s
//   |
//   ;

programa : instrucciones EOF ;

instrucciones : instruccion instrucciones
              |
              ;

// instruccion : INST {print($INST.text[:-1])};
instruccion : declaracion
            | iwhile
            | ifor
            | iif
            | bloque
            | asignacion 
            | PYC
            ;

declaracion : INT ID PYC ;

asignacion : ID ASIG opal ;

// TDATO: INT
//         | DOUBLE
//         | LONG
//         ;


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
       | PA exp PC
       ;

iwhile : WHILE PA cond PC (bloque | instruccion) ;

bloque : LLA instrucciones LLC ;

iif : IF PA cond PC (bloque | instruccion)  ;
ifor : FOR PA init PYC cond PYC iter PC (bloque | instruccion) ;
init : asignacion;
cond : opal;
iter : (ID|NUMERO) ASIG exp;
