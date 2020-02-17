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
class CashFlowStatement(Base):
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
    CashFlow_from_OperaActv = Column(String(32), default='', comment='一、经营活动产生的现金流量(元)', unique=False)
    Cash_from_GoodsSelling_and_ServProviding = Column(String(32), default='',
                                                      comment='销售商品、提供劳务收到的现金(元)', unique=False)
    Taxes_and_refunds_recv = Column(String(32), default='', comment='收到的税费与返还(元)', unique=False)
    Cash_from_other_OperaActv = Column(String(32), default='', comment='收到其他与经营活动有关的现金(元)',
                                       unique=False)
    CashSubtotal_inflow_from_OperaActv = Column(String(32), default='', comment='经营活动现金流入小计(元)',
                                                unique=False)
    Cash_for_goods_and_services = Column(String(32), default='', comment='购买商品、接受劳务支付的现金(元)', unique=False)
    Cash_to_and_for_employees = Column(String(32), default='', comment='支付给职工以及为职工支付的现金(元)', unique=False)
    Taxes_paid = Column(String(32), default='', comment='支付的各项税费(元)', unique=False)
    Cash_related_to_other_OperaActv = Column(String(32), default='', comment='支付其他与经营活动有关的现金(元)',
                                             unique=False)
    Subtotal_of_cash_outflow_from_OperaActv = Column(String(32), default='', comment='经营活动现金流出小计(元)',
                                                     unique=False)
    NCFlow_from_OperaActv = Column(String(32), default='', comment='经营活动产生的现金流量净额(元)', unique=False)
    CashFlow_from_InvestActv = Column(String(32), default='', comment='二、投资活动产生的现金流量(元)', unique=False)
    Cash_from_invest_recovery = Column(String(32), default='', comment='收回投资收到的现金(元)', unique=False)
    Cash_from_invest_income = Column(String(32), default='', comment='取得投资收益收到的现金(元)', unique=False)
    NC_from_fixed_intang_and_LT_assets_Dispos = Column(
        String(32), default='', comment='处置固定资产、无形资产和其他长期资产收回的现金净额(元)', unique=False)
    NC_received_from_Disposal_of_SubsidiaryAndBuizUnit = Column(String(32), default='',
                                   comment='处置子公司及其他营业单位收到的现金净额(元)',
                                   unique=False)
    Cash_from_other_InvestActv = Column(String(32), default='', comment='收到其他与投资活动有关的现金(元)',
                                        unique=False)
    Subtotal_of_CashInflow_from_InvestActv = Column(String(32), default='', comment='投资活动现金流入小计(元)',
                                                    unique=False)
    Cash_for_acquis_and_construc_of_fixed_intang_and_LT_assets = Column(
        String(32), default='', comment='购建固定资产、无形资产和其他长期资产支付的现金(元)', unique=False)
    Cash_for_invest = Column(String(32), default='', comment='投资支付的现金(元)', unique=False)
    NC_by_subsidiaries_and_other_BuizUnits = Column(String(32), default='',
                                                    comment='取得子公司及其他营业单位支付的现金净额(元)', unique=False)
    Cash_related_to_other_InvestActv = Column(String(32), default='', comment='支付其他与投资活动有关的现金(元)',
                                              unique=False)
    Subtotal_of_CashOutflow_from_OperaActv = Column(String(32), default='', comment='投资活动现金流出小计(元)',
                                                    unique=False)
    NCFlow_from_InvestActv = Column(String(32), default='', comment='投资活动产生的现金流量净额(元)', unique=False)
    CashFlow_from_FinanceActv = Column(String(32), default='', comment='三、筹资活动产生的现金流量(元)', unique=False)
    Cash_from_absorbing_invest = Column(String(32), default='', comment='吸收投资收到的现金(元)', unique=False)
    Cash_from_borrowing = Column(String(32), default='', comment='取得借款收到的现金(元)', unique=False)
    Subtotal_of_cash_inflow_from_FinanceActv = Column(String(32), default='', comment='筹资活动现金流入小计(元)',
                                                      unique=False)
    Cash_for_debt_repay = Column(String(32), default='', comment='偿还债务支付的现金(元)', unique=False)
    Cash_for_distrib_of_dividends_profits_or_InterestRepay = Column(String(32), default='',
                                                                    comment='分配股利、利润或偿付利息支付的现金(元)',
                                                                    unique=False)
    Cash_for_other_FinanceActv = Column(String(32), default='', comment='支付其他与筹资活动有关的现金(元)', unique=False)
    Subtotal_of_CashOutFlow_from_FinanceActv = Column(String(32), default='', comment='筹资活动现金流出小计(元)',
                                                      unique=False)
    NCFlow_from_FinanceActv = Column(String(32), default='', comment='筹资活动产生的现金流量净额(元)', unique=False)
    Effect_of_ExchangeRate_changes_on_CashAndCashEquiv = Column(String(32), default='',
                                                                comment='四、汇率变动对现金及现金等价物的影响(元)',
                                                                unique=False)
    Net_incre_in_cash_and_CashEquiv = Column(String(32), default='', comment='五、现金及现金等价物净增加额(元)',
                                             unique=False)
    Balance_of_cash_and_CashEquiv_at_PeriodBegin = Column(String(32), default='',
                                                          comment='加：期初现金及现金等价物余额(元)',
                                                          unique=False)
    Balance_of_cash_and_CashEquiv_at_PeriodEnd = Column(String(32), default='',
                                                        comment='六、期末现金及现金等价物余额(元)', unique=False)
    Supplementary_information = Column(String(32), default='', comment='补充资料：(元)', unique=False)

    Adjust_NP_to_CashFlow_from_OperaActv = Column(String(32), default='',
                                                  comment='1、将净利润调节为经营活动现金流量：(元)', unique=False)
    Net_profit = Column(String(32), default='', comment='净利润(元)', unique=False)
    Aovision_for_asset_impairment = Column(String(32), default='', comment='加：资产减值准备(元)', unique=False)
    Depreciate_of_FixedDeplet_of_OilGas_and_ProdBioAssets = Column(
        String(32), default='', comment='固定资产折旧、油气资产折耗、生产性生物资产折旧(元)', unique=False)
    Amortization_of_intang_assets = Column(String(32), default='', comment='无形资产摊销(元)', unique=False)
    Amortization_of_long_term_unamortized_expenses = Column(String(32), default='', comment='长期待摊费用摊销(元)',
                                                            unique=False)
    Loss_on_dispos_of_fixed_intang_and_LT_assets = Column(String(32), default='',
                                                          comment='处置固定资产、无形资产和其他长期资产的损失(元)',
                                                          unique=False)
    Loss_on_retirement_of_fixed_assets = Column(String(32), default='', comment='固定资产报废损失(元)', unique=False)
    Loss_from_changes_in_fair_value = Column(String(32), default='', comment='公允价值变动损失(元)', unique=False)
    Financial_expenses = Column(String(32), default='', comment='财务费用(元)', unique=False)
    Invest_loss = Column(String(32), default='', comment='投资损失(元)', unique=False)
    Decrease_of_deferred_income_tax_assets = Column(String(32), default='', comment='递延所得税资产减少(元)', unique=False)
    Incre_in_deferred_income_TaxLiability = Column(String(32), default='', comment='递延所得税负债增加(元)', unique=False)
    Decrease_of_inventory = Column(String(32), default='', comment='存货的减少(元)', unique=False)
    Decrease_of_operate_receivables = Column(String(32), default='', comment='经营性应收项目的减少(元)', unique=False)
    Incre_in_operate_payables = Column(String(32), default='', comment='经营性应付项目的增加(元)', unique=False)
    OtherItem = Column(String(32), default='', comment='其他项目(元)', unique=False)
    Indirect_method_NCFlow_from_OperaActv = Column(String(32), default='',
                                                   comment='间接法-经营活动产生的现金流量净额(元)', unique=False)

    MajorInvest_and_FinanceActiv_not_invol_CashReceipts_and_pays = Column(String(32),
                                                                          default='',
                                                                          comment='2、不涉及现金收支的重大投资和筹资活动：(元)',
                                                                          unique=False)

    Net_changes_in_Cash_and_CashEquiv = Column(String(32), default='', comment='3、现金及现金等价物净变动情况：(元)',
                                               unique=False)
    Closing_balance_of_cash = Column(String(32), default='', comment='现金的期末余额(元)', unique=False)
    Opening_balance_of_cash = Column(String(32), default='', comment='减：现金的期初余额(元)', unique=False)
    Indirect_method_Net_Incre_in_Cash_and_CashEquiv = Column(String(32), default='',
                                                             comment='间接法-现金及现金等价物净增加额(元)', unique=False)

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