grammar CPPP;

program: subtaskBlock+ EOF;

subtaskBlock: subtaskName '{' configBlock genBlock '}';

subtaskName: ID+;
configBlock: 'config' '{' configItem+ '}';
configItem: INPUT STR | OUTPUT STR | TESTS NUMBER | SOL STR | TEST_SOL STR | compare;
genBlock: 'generate' '{' func+ '}';

primitiveType:  INT | FLOAT | DOUBLE | LL | CHAR | STRTYPE;
dataType: primitiveType | ARRAY '<' dataType '>' | TREE '(' expr ')' | GRAPH '(' expr ',' expr ')';

func: var | printStmt | loopStmt;
var: VAR dataType ID  ('[' expr ']')* option* ';';

printStmt: PRINT expr+ ';';
loopStmt: 'repeat' '(' expr ')' '{' func* '}';

compare: COMPARE expr?;

option: ID | RANGE '(' expr ',' expr ')';

expr: '-' expr | '(' expr ')' | expr ('*' | '/' | '%') expr | expr ('+' | '-') expr 
                   | expr ('>' | '<' | '>=' | '<=' | '==' | '!=') expr 
                   | expr ('&&' | '||') expr
                   | ID | NUMBER | STR;

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
TESTS: 'tests';
TEST_SOL: 'test_sol';
SOL: 'sol';
COMPARE: 'compare';
RANGE: 'range';
NUMBER: [0-9]+;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
STR: '"' (~["\\] | '\\' .)* '"';

WS : [ \t\r\n]+ -> skip;
