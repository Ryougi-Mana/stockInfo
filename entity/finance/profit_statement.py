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
class ProfitStatement(Base):
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
    Total_operating_revenue = Column(String(32), default='', comment='一、营业总收入(元)', unique=False)
    Including_operating_income = Column(String(32), default='', comment='其中：营业收入(元)', unique=False)
    Total_operating_cost = Column(String(32), default='', comment='二、营业总成本(元)', unique=False)
    Operating_cost = Column(String(32), default='', comment='其中：营业成本(元)', unique=False)
    Business_tax_and_surcharges = Column(String(32), default='', comment='营业税金及附加(元)', unique=False)
    Sales_expenses = Column(String(32), default='', comment='销售费用(元)', unique=False)
    Management_expenses = Column(String(32), default='', comment='管理费用(元)', unique=False)
    Research_develop_expenses = Column(String(32), default='', comment='研发费用(元)', unique=False)
    Financial_expenses = Column(String(32), default='', comment='财务费用(元)', unique=False)
    Including_interest_expense = Column(String(32), default='', comment='其中：利息费用(元)', unique=False)
    Interest_income = Column(String(32), default='', comment='利息收入(元)', unique=False)
    Asset_impairment_loss = Column(String(32), default='', comment='资产减值损失(元)', unique=False)
    Credit_impairment_loss = Column(String(32), default='', comment='信用减值损失(元)', unique=False)
    Income_from_changes_in_FairValue = Column(String(32), default='', comment='加：公允价值变动收益(元)', unique=False)
    Invest_income = Column(String(32), default='', comment='投资收益(元)', unique=False)
    Invest_income_of_assoc_Enterp_and_JointVenture = Column(String(32), default='',
                                                            comment='其中：联营企业和合营企业的投资收益(元)',
                                                            unique=False)
    Operating_profit = Column(String(32), default='', comment='三、营业利润(元)', unique=False)
    Non_operating_income = Column(String(32), default='', comment='加：营业外收入(元)', unique=False)
    Gains_from_disposal_of_non_current_assets = Column(String(32), default='', comment='其中：非流动资产处置利得(元)',
                                                       unique=False)
    Non_operating_expenditure = Column(String(32), default='', comment='减：营业外支出(元)', unique=False)
    Loss_on_disposal_of_non_current_assets = Column(String(32), default='', comment='其中：非流动资产处置损失(元)',
                                                    unique=False)
    Total_profit = Column(String(32), default='', comment='四、利润总额(元)', unique=False)
    Income_tax_expense = Column(String(32), default='', comment='减：所得税费用(元)', unique=False)
    NP = Column(String(32), default='', comment='五、净利润(元)', unique=False)
    NP_from_continuing_operations = Column(String(32), default='', comment='（一）持续经营净利润(元)', unique=False)
    NP_attri_to_owner_of_ParentComp = Column(String(32), default='',
                                             comment='归属于母公司所有者的净利润(元)', unique=False)
    Minority_shareholders_profit_and_loss = Column(String(32), default='', comment='少数股东损益(元)', unique=False)
    NP_after_deduct_non_recurring_profit_and_loss = Column(String(32), default='',
                                                           comment='扣除非经常性损益后的净利润(元)', unique=False)
    Earnings_per_share = Column(String(32), default='', comment='六、每股收益(元)', unique=False)
    Basic_earnings_per_share = Column(String(32), default='', comment='（一）基本每股收益(元)', unique=False)
    Diluted_earnings_per_share = Column(String(32), default='', comment='（二）稀释每股收益(元)', unique=False)
    Other_ComprehIncome = Column(String(32), default='', comment='七、其他综合收益(元)', unique=False)
    Other_ComprehIncome_attri_to_ParentCompOwner = Column(String(32), default='',
                                                          comment='归属母公司所有者的其他综合收益(元)',
                                                          unique=False)
    Total_ComprehIncome = Column(String(32), default='', comment='八、综合收益总额(元)', unique=False)
    Total_ComprehIncome_attri_to_shareholders_of_ParentComp = Column(String(32), default='',
                                                                     comment='归属于母公司股东的综合收益总额(元)',
                                                                     unique=False)
    Total_ComprehIncome_attri_to_minor_ShareHolders = Column(String(32), default='',
                                                             comment='归属于少数股东的综合收益总额(元)', unique=False)

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