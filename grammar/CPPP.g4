grammar CPPP;

program: subtaskBlock+ EOF;

subtaskBlock: subtaskName '{' configBlock genBlock checkerBlock? '}';

subtaskName: ID+;
configBlock: 'config' '{' (INPUT CPP_FILE OUTPUT CPP_FILE | (OUTPUT CPP_FILE INPUT CPP_FILE)) '}';
genBlock: 'generate' '{' func+ '}';
checkerBlock: 'checker' '{' ID+ '}'; 
primitiveType:  INT | FLOAT | DOUBLE | LL | CHAR | STRTYPE;
dataType: primitiveType | ARRAY '<' dataType '>' | TREE '(' NUMBER ')' | GRAPH '(' NUMBER ',' NUMBER ')';
func: var | printStmt;
var: VAR dataType ID  ('[' expr ']')* option* ';';
expr: ID | NUMBER | STR;
printStmt: PRINT ID*;
option: ID+;

INT: 'int';
FLOAT: 'float';
DOUBLE: 'double';
LL: 'll';
CHAR: 'char';
STRTYPE: 'string';
ARRAY: 'array';
PRINT: 'print';
VAR: 'var';
TREE: 'tree';
GRAPH: 'graph';
INPUT: 'input';
OUTPUT: 'output';
CPP_FILE: '"' (~["\\\r\n] | '\\' .)* '.cpp"';
NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
STR: '"' (~["\\] | '\\' .)* '"';

WS : [ \t\r\n]+ -> skip;