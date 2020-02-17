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
class MainIndicators(Base):
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
    Growth_capacity_indicators = Column(String(32), default='', comment='成长能力指标', unique=False)
    Net_profit = Column(String(32), default='', comment='净利润(元)', unique=False)
    Year_on_year_growth_rate_of_net_profit = Column(String(32), default='', comment='净利润同比增长率', unique=False)
    Deduct_non_net_profit = Column(String(32), default='', comment='扣非净利润(元)', unique=False)
    Year_on_year_growth_rate_of_non_net_profit = Column(String(32), default='', comment='扣非净利润同比增长率', unique=False)
    Total_operating_revenue = Column(String(32), default='', comment='营业总收入(元)', unique=False)
    Year_on_year_growth_rate_of_total_operating_revenue = Column(String(32), default='', comment='营业总收入同比增长率',
                                                                 unique=False)
    Per_share_indicator = Column(String(32), default='', comment='每股指标', unique=False)
    Basic_earnings_per_share = Column(String(32), default='', comment='基本每股收益(元)', unique=False)
    Net_assets_per_share = Column(String(32), default='', comment='每股净资产(元)', unique=False)
    Capital_reserve_per_share = Column(String(32), default='', comment='每股资本公积金(元)', unique=False)
    Undistributed_profit_per_share = Column(String(32), default='', comment='每股未分配利润(元)', unique=False)
    Operating_cash_flow_per_share = Column(String(32), default='', comment='每股经营现金流(元)', unique=False)
    Profitability_index = Column(String(32), default='', comment='盈利能力指标', unique=False)
    Net_sales_interest_rate = Column(String(32), default='', comment='销售净利率', unique=False)
    Gross_margin_on_sales = Column(String(32), default='', comment='销售毛利率', unique=False)
    Return_on_equity = Column(String(32), default='', comment='净资产收益率', unique=False)
    Return_on_equity_diluted = Column(String(32), default='', comment='净资产收益率-摊薄', unique=False)
    Operational_capability_index = Column(String(32), default='', comment='运营能力指标', unique=False)
    Business_cycle = Column(String(32), default='', comment='营业周期(天)', unique=False)
    Inventory_turnover_rate = Column(String(32), default='', comment='存货周转率(次)', unique=False)
    Inventory_turnover_days = Column(String(32), default='', comment='存货周转天数(天)', unique=False)
    Days_of_receivables_turnover = Column(String(32), default='', comment='应收账款周转天数(天)', unique=False)
    Solvency_Index = Column(String(32), default='', comment='偿债能力指标', unique=False)
    Liquidity_ratio = Column(String(32), default='', comment='流动比率', unique=False)
    Quick_ratio = Column(String(32), default='', comment='速动比率', unique=False)
    Conservative_quick_ratio = Column(String(32), default='', comment='保守速动比率', unique=False)
    Property_right_ratio = Column(String(32), default='', comment='产权比率', unique=False)
    Asset_liability_ratio = Column(String(32), default='', comment='资产负债比率', unique=False)

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


def insert(data):
    session.add(data)
    session.commit()


def showColumns():
    cols = Base.metadata.tables
    cols = str(cols)
    print(cols)


if __name__ == '__main__':
    # create_db()
    showColumns();
