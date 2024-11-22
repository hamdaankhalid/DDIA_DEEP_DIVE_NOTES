# Generated from ./SQL_SUBSET.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,51,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,26,8,1,1,2,1,2,
        1,2,1,2,5,2,32,8,2,10,2,12,2,35,9,2,3,2,37,8,2,1,3,1,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,2,1,
        0,3,8,1,0,13,14,45,0,16,1,0,0,0,2,19,1,0,0,0,4,36,1,0,0,0,6,38,1,
        0,0,0,8,40,1,0,0,0,10,44,1,0,0,0,12,46,1,0,0,0,14,48,1,0,0,0,16,
        17,3,2,1,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,9,0,0,20,21,3,4,2,
        0,21,22,5,10,0,0,22,25,3,6,3,0,23,24,5,11,0,0,24,26,3,8,4,0,25,23,
        1,0,0,0,25,26,1,0,0,0,26,3,1,0,0,0,27,37,5,1,0,0,28,33,3,10,5,0,
        29,30,5,2,0,0,30,32,3,10,5,0,31,29,1,0,0,0,32,35,1,0,0,0,33,31,1,
        0,0,0,33,34,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,36,27,1,0,0,0,36,
        28,1,0,0,0,37,5,1,0,0,0,38,39,5,12,0,0,39,7,1,0,0,0,40,41,3,10,5,
        0,41,42,3,12,6,0,42,43,3,14,7,0,43,9,1,0,0,0,44,45,5,12,0,0,45,11,
        1,0,0,0,46,47,7,0,0,0,47,13,1,0,0,0,48,49,7,1,0,0,49,15,1,0,0,0,
        3,25,33,36
    ]

class SQL_SUBSETParser ( Parser ):

    grammarFileName = "SQL_SUBSET.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "','", "'='", "'>'", "'<'", "'>='", 
                     "'<='", "'<>'", "'SELECT'", "'FROM'", "'WHERE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SELECT", "FROM", "WHERE", "IDENTIFIER", 
                      "NUMBER", "STRING", "WS" ]

    RULE_sql_stmt = 0
    RULE_select_stmt = 1
    RULE_column_list = 2
    RULE_table_name = 3
    RULE_condition = 4
    RULE_column_name = 5
    RULE_comparison_op = 6
    RULE_value = 7

    ruleNames =  [ "sql_stmt", "select_stmt", "column_list", "table_name", 
                   "condition", "column_name", "comparison_op", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    SELECT=9
    FROM=10
    WHERE=11
    IDENTIFIER=12
    NUMBER=13
    STRING=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Sql_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_stmt(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.Select_stmtContext,0)


        def EOF(self):
            return self.getToken(SQL_SUBSETParser.EOF, 0)

        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_sql_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSql_stmt" ):
                listener.enterSql_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSql_stmt" ):
                listener.exitSql_stmt(self)




    def sql_stmt(self):

        localctx = SQL_SUBSETParser.Sql_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sql_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.select_stmt()
            self.state = 17
            self.match(SQL_SUBSETParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQL_SUBSETParser.SELECT, 0)

        def column_list(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.Column_listContext,0)


        def FROM(self):
            return self.getToken(SQL_SUBSETParser.FROM, 0)

        def table_name(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.Table_nameContext,0)


        def WHERE(self):
            return self.getToken(SQL_SUBSETParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.ConditionContext,0)


        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)




    def select_stmt(self):

        localctx = SQL_SUBSETParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(SQL_SUBSETParser.SELECT)
            self.state = 20
            self.column_list()
            self.state = 21
            self.match(SQL_SUBSETParser.FROM)
            self.state = 22
            self.table_name()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 23
                self.match(SQL_SUBSETParser.WHERE)
                self.state = 24
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQL_SUBSETParser.Column_nameContext)
            else:
                return self.getTypedRuleContext(SQL_SUBSETParser.Column_nameContext,i)


        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_column_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_list" ):
                listener.enterColumn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_list" ):
                listener.exitColumn_list(self)




    def column_list(self):

        localctx = SQL_SUBSETParser.Column_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_column_list)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(SQL_SUBSETParser.T__0)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.column_name()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==2:
                    self.state = 29
                    self.match(SQL_SUBSETParser.T__1)
                    self.state = 30
                    self.column_name()
                    self.state = 35
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SQL_SUBSETParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)




    def table_name(self):

        localctx = SQL_SUBSETParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(SQL_SUBSETParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_name(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.Column_nameContext,0)


        def comparison_op(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.Comparison_opContext,0)


        def value(self):
            return self.getTypedRuleContext(SQL_SUBSETParser.ValueContext,0)


        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = SQL_SUBSETParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.column_name()
            self.state = 41
            self.comparison_op()
            self.state = 42
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SQL_SUBSETParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_column_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_name" ):
                listener.enterColumn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_name" ):
                listener.exitColumn_name(self)




    def column_name(self):

        localctx = SQL_SUBSETParser.Column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_column_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SQL_SUBSETParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_comparison_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_op" ):
                listener.enterComparison_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_op" ):
                listener.exitComparison_op(self)




    def comparison_op(self):

        localctx = SQL_SUBSETParser.Comparison_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 504) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SQL_SUBSETParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(SQL_SUBSETParser.NUMBER, 0)

        def getRuleIndex(self):
            return SQL_SUBSETParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SQL_SUBSETParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





