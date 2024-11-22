from antlr4 import *
from SQL_SUBSETLexer import SQL_SUBSETLexer
from SQL_SUBSETParser import SQL_SUBSETParser

input_sql = "SELECT name, age FROM users WHERE age > 30"
input_stream = InputStream(input_sql)
lexer = SQL_SUBSETLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = SQL_SUBSETParser(token_stream)

# Parse the SQL query
tree = parser.sql_stmt()

print(tree.toStringTree(recog=parser))

"""
(sql_stmt (
    select_stmt
            SELECT (
                column_list (column_name name), (column_name age)
            )
            FROM (
                table_name users
            )
            WHERE (
                condition (column_name age) (comparison_op >) (value 30)
        )
    ) 
)
"""