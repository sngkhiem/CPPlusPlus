grammar CPPP;

program: subtaskBlock+ EOF;

subtaskBlock: subtaskName '{' configBlock genBlock checkerBlock? '}';

subtaskName: ID+;
configBlock: 'config' '{' ID+ '}';
genBlock: 'generate' '{' ID+ '}';
checkerBlock: 'checker' '{' ID+ '}'; 
primitiveType:  INT | FLOAT | DOUBLE | LL | CHAR | STRTYPE;
dataType: primitiveType | ARRAY '<' dataType '>';
var: 'var' dataType ID  ('[' expr ']')* ';';
expr: ID | NUMBER | STR;

INT: 'int';
FLOAT: 'float';
DOUBLE: 'double';
LL: 'll';
CHAR: 'char';
STRTYPE: 'string';
ARRAY: 'array';
NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
STR: '"' (~["\\] | '\\' .)* '"';

WS : [ \t\r\n]+ -> skip;