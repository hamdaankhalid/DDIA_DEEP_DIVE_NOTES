# Generated from ./SQL_SUBSET.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SQL_SUBSETParser import SQL_SUBSETParser
else:
    from SQL_SUBSETParser import SQL_SUBSETParser

# This class defines a complete listener for a parse tree produced by SQL_SUBSETParser.
class SQL_SUBSETListener(ParseTreeListener):

    # Enter a parse tree produced by SQL_SUBSETParser#sql_stmt.
    def enterSql_stmt(self, ctx:SQL_SUBSETParser.Sql_stmtContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#sql_stmt.
    def exitSql_stmt(self, ctx:SQL_SUBSETParser.Sql_stmtContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#select_stmt.
    def enterSelect_stmt(self, ctx:SQL_SUBSETParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#select_stmt.
    def exitSelect_stmt(self, ctx:SQL_SUBSETParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#column_list.
    def enterColumn_list(self, ctx:SQL_SUBSETParser.Column_listContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#column_list.
    def exitColumn_list(self, ctx:SQL_SUBSETParser.Column_listContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#table_name.
    def enterTable_name(self, ctx:SQL_SUBSETParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#table_name.
    def exitTable_name(self, ctx:SQL_SUBSETParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#condition.
    def enterCondition(self, ctx:SQL_SUBSETParser.ConditionContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#condition.
    def exitCondition(self, ctx:SQL_SUBSETParser.ConditionContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#column_name.
    def enterColumn_name(self, ctx:SQL_SUBSETParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#column_name.
    def exitColumn_name(self, ctx:SQL_SUBSETParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#comparison_op.
    def enterComparison_op(self, ctx:SQL_SUBSETParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#comparison_op.
    def exitComparison_op(self, ctx:SQL_SUBSETParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by SQL_SUBSETParser#value.
    def enterValue(self, ctx:SQL_SUBSETParser.ValueContext):
        pass

    # Exit a parse tree produced by SQL_SUBSETParser#value.
    def exitValue(self, ctx:SQL_SUBSETParser.ValueContext):
        pass



del SQL_SUBSETParser