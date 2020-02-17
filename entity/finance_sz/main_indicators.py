import os

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Index, UniqueConstraint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ENGINE = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/sz_finance?charset=utf8mb4", )

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
    Id = Column(Integer, index=True, primary_key=True, autoincrement=True)
    # 股票代码
    Code = Column(Integer, index=True, comment='股票代码-数字型', unique=False)
    # 股票代码
    Code_Str = Column(String(32), index=True, comment='股票代码-字符串型', unique=False)
    # 报告期 X
    Report_Period = Column(String(32), default='', comment='报告期', unique=False)
    # 财务项目指标名称 Y
    Indicator_Name = Column(String(32), default='', comment='财务项目指标名称', unique=False)
    # 财务项目指标数值
    Indicator_Data = Column(String(32), default='', comment='财务项目指标数值', unique=False)

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


def insertBatch(dataList: list):
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
    create_db()
    # showColumns();
