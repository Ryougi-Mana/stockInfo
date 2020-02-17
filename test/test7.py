from entity.finance import main_indicators, balance_sheets, profit_statement, cash_flow_statement
from entity.finance.main_indicators import MainIndicators
from entity.finance.balance_sheets import BalanceSheets
from entity.finance.profit_statement import ProfitStatement
from entity.finance.cash_flow_statement import CashFlowStatement

from entity.finance import finance

if __name__ == '__main__':
    finance.createTable('stock_300726')

    # data1 = MainIndicators(Id='sdifjaiosjd', Code=200123, Net_profit='300玩', Code_Str='200124')
    # data2 = BalanceSheets(Id='123', Code=200123, Code_Str='600008', Report_Period='2019-09-30')
