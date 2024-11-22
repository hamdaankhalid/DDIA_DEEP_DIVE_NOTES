grammar SQL_SUBSET;

// Entry point
sql_stmt
    : select_stmt EOF
    ;

// Select statement
select_stmt
    : SELECT column_list FROM table_name (WHERE condition)?
    ;

// Columns
column_list
    : '*' | column_name (',' column_name)*
    ;

// Table
table_name
    : IDENTIFIER
    ;

// Condition
condition
    : column_name comparison_op value
    ;

// Column
column_name
    : IDENTIFIER
    ;

// Operators
comparison_op
    : '=' | '>' | '<' | '>=' | '<=' | '<>'
    ;

// Value
value
    : STRING | NUMBER
    ;

// Tokens
SELECT      : 'SELECT';
FROM        : 'FROM';
WHERE       : 'WHERE';
IDENTIFIER  : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER      : [0-9]+;
STRING      : '\'' .*? '\'';
WS          : [ \t\r\n]+ -> skip;
