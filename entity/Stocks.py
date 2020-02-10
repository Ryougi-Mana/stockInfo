# 1. 创建单表
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Index, UniqueConstraint

import datetime

ENGINE = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/stock?charset=utf8mb4", )

# Base是declarative_base的实例化对象
Base = declarative_base()


# 每个类都要继承Base
class Stocks(Base):
    # __tablename__是必须要的，它是设置实际存在数据库中的表名
    __tablename__ = "stocks"

    # Column是列的意思，固定写法 Column(字段类型, 参数)
    # primary_key主键、index索引、nullable是否可以为空
    id = Column(String(32), index=True, primary_key=True)
    code = Column(Integer, index=True)
    codeStr = Column(String(32), index=True)
    name = Column(String(32), nullable=True)
    market = Column(String(32), unique=False, nullable=True)
    # market_type = Column(Integer, default=datetime.datetime.now)
    market_type = Column(Integer, default=0, nullable=False)

    # 相当于Django的ORM的class Meta，是一些元信息
    __table_args__ = (
        UniqueConstraint("id", "code", name="uni_id_code"), Index("id", "code")
    )


def create_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(ENGINE)


def drop_db():
    # metadata.drop_all删除所有表
    Base.metadata.drop_all(ENGINE)


if __name__ == '__main__':
    create_db()
