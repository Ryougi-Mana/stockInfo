import os

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Index, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ENGINE = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/stock?charset=utf8mb4", )

# Base是declarative_base的实例化对象
Base = declarative_base()

DBSession = sessionmaker(bind=ENGINE)
session = DBSession()


# 每个类都要继承Base
class BalanceSheets(Base):
    # __tablename__是必须要的，它是设置实际存在数据库中的表名
    __tablename__ = os.path.split(__file__)[-1].split(".")[0]

    # 股票通用 字段

    # primary_key主键、index索引、nullable是否可以为空
    Id = Column(String(32), index=True, primary_key=True)
    # 股票代码
    Code = Column(Integer, index=True, comment='股票代码-数字型', unique=False)
    # 股票代码
    Code_Str = Column(String(32), index=True, comment='股票代码-字符串型', unique=False)
    # 报告期
    Report_Period = Column(String(32), default='', comment='报告期', unique=False)

    # 主要指标下的各种财务项目
    Current_assets = Column(String(32), default='', comment='流动资产(元)', unique=False)
    Monetary_capital = Column(String(32), default='', comment='货币资金(元)', unique=False)
    Financial_assets_measured_at_fair_value_through_profit_or_loss = Column(String(32), default='',
                                                                            comment='以公允价值计量且其变动计入当期损益的金融资产(元)',
                                                                            unique=False)
    Notes_receivable_and_accounts_receivable = Column(String(32), default='', comment='应收票据及应收账款(元)', unique=False)
    Including_notes_receivable = Column(String(32), default='', comment='其中：应收票据(元)', unique=False)
    Accounts_receivable = Column(String(32), default='', comment='应收账款(元)', unique=False)
    Prepayment = Column(String(32), default='', comment='预付款项(元)', unique=False)
    Total_other_receivables = Column(String(32), default='', comment='其他应收款合计(元)', unique=False)
    Other_receivables = Column(String(32), default='', comment='其他应收款(元)', unique=False)
    Inventory = Column(String(32), default='', comment='存货(元)', unique=False)
    Non_current_assets_due_within_one_year = Column(String(32), default='', comment='一年内到期的非流动资产(元)', unique=False)
    Other_current_assets = Column(String(32), default='', comment='其他流动资产(元)', unique=False)
    Total_current_assets = Column(String(32), default='', comment='流动资产合计(元)', unique=False)
    Non_current_assets = Column(String(32), default='', comment='非流动资产(元)', unique=False)
    Available_for_sale_financial_assets = Column(String(32), default='', comment='可供出售金融资产(元)', unique=False)
    Long_term_equity_investment = Column(String(32), default='', comment='长期股权投资(元)', unique=False)
    Total_fixed_assets = Column(String(32), default='', comment='固定资产合计(元)', unique=False)
    Including_fixed_assets = Column(String(32), default='', comment='其中：固定资产(元)', unique=False)
    Total_construction_in_progress = Column(String(32), default='', comment='在建工程合计(元)', unique=False)
    Including_Construction_in_progress = Column(String(32), default='', comment='其中：在建工程(元)', unique=False)
    Intangible_assets = Column(String(32), default='', comment='无形资产(元)', unique=False)
    Goodwill = Column(String(32), default='', comment='商誉(元)', unique=False)
    Long_term_unamortized_expenses = Column(String(32), default='', comment='长期待摊费用(元)', unique=False)
    Deferred_income_tax_assets = Column(String(32), default='', comment='递延所得税资产(元)', unique=False)
    Other_non_current_assets = Column(String(32), default='', comment='其他非流动资产(元)', unique=False)
    Total_non_current_assets = Column(String(32), default='', comment='非流动资产合计(元)', unique=False)
    Total_assets = Column(String(32), default='', comment='资产合计(元)', unique=False)
    Current_liabilities = Column(String(32), default='', comment='流动负债(元)', unique=False)
    Short_term_loan = Column(String(32), default='', comment='短期借款(元)', unique=False)
    Notes_payable_and_accounts_payable = Column(String(32), default='', comment='应付票据及应付账款(元)', unique=False)
    Including_notes_payable = Column(String(32), default='', comment='其中：应付票据(元)', unique=False)
    Accounts_payable = Column(String(32), default='', comment='应付账款(元)', unique=False)
    Advance_payment = Column(String(32), default='', comment='预收款项(元)', unique=False)
    Payroll_payable = Column(String(32), default='', comment='应付职工薪酬(元)', unique=False)
    Tax_payable = Column(String(32), default='', comment='应交税费(元)', unique=False)
    Total_other_payables = Column(String(32), default='', comment='其他应付款合计(元)', unique=False)
    Dividend_payable = Column(String(32), default='', comment='应付股利(元)', unique=False)
    Other_payables = Column(String(32), default='', comment='其他应付款(元)', unique=False)
    Total_current_liabilities = Column(String(32), default='', comment='流动负债合计(元)', unique=False)
    Non_current_liabilities = Column(String(32), default='', comment='非流动负债(元)', unique=False)
    Deferred_income_tax_liabilities = Column(String(32), default='', comment='递延所得税负债(元)', unique=False)
    Deferred_income_non_current_liabilities = Column(String(32), default='', comment='递延收益-非流动负债(元)', unique=False)
    Total_non_current_liabilities = Column(String(32), default='', comment='非流动负债合计(元)', unique=False)
    Total_liabilities = Column(String(32), default='', comment='负债合计(元)', unique=False)
    Owners_equity_or_shareholders_equity = Column(String(32), default='', comment='所有者权益（或股东权益）(元)', unique=False)
    Paid_in_capital_or_share_capital = Column(String(32), default='', comment='实收资本（或股本）(元)', unique=False)
    Capital_reserve = Column(String(32), default='', comment='资本公积(元)', unique=False)
    Other_comprehensive_income = Column(String(32), default='', comment='其他综合收益(元)', unique=False)
    Surplus_reserve = Column(String(32), default='', comment='盈余公积(元)', unique=False)
    Undistributed_profit = Column(String(32), default='', comment='未分配利润(元)', unique=False)
    Total_owners_equity_attributable_to_the_parent_company = Column(String(32), default='', comment='归属于母公司所有者权益合计(元)',
                                                                    unique=False)
    Minority_shareholders_equity = Column(String(32), default='', comment='少数股东权益(元)', unique=False)
    Total_owners_equity_or_shareholders_equity = Column(String(32), default='', comment='所有者权益（或股东权益）合计(元)',
                                                        unique=False)
    Total_liabilities_and_owners_equity_or_shareholders_equity = Column(String(32), default='',
                                                                        comment='负债和所有者权益（或股东权益）合计(元)', unique=False)

    # 相当于Django的ORM的class Meta，是一些元信息
    __table_args__ = (
        UniqueConstraint("Id", "Code", name="uni_Id_Code"), Index("Id", "Code")
    )


def create_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(ENGINE)


def drop_db():
    # metadata.drop_all删除所有表
    Base.metadata.drop_all(ENGINE)


def insertPatch(dataList: list):
    for data in dataList:
        session.add(data)
    session.commit()


if __name__ == '__main__':
    create_db()


def insert(data):
    session.add(data)
    session.commit()