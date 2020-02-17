from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接参数
ENGINE = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/finance?charset=utf8mb4", )
# Base是declarative_base的实例化对象
Base = declarative_base()
DBSession = sessionmaker(bind=ENGINE)
session = DBSession()


def createTable(tablename):
    sql = "create table " + tablename
    sql += "( id varchar(32) primary key not null,"
    sql += "stock_name varchar(32) default '' not null comment '股票名称',"
    sql += "stock_code varchar(32) default '' not null comment '股票代码',"
    sql += "indicator_name varchar(32) default '' not null comment '指标名称',"
    sql += "indicator_data varchar(32) default '' null comment '指标数值',"
    sql += "finance_type int null comment '该行数据所属的财务报表的类型',"
    sql += "finance_name varchar(32) default '' null comment '该行数据所属的财报种类名');"
    session.execute(sql)
    session.commit()


# def getDynamicModel(claz_name, table_name):
#     cls = type(claz_name, (Finance,), {'__tablename__': table_name})
#     return cls
# modelClass = getDynamicModel('Yaoshikeji', 'yaoshikeji')
# re = modelClass(Id='sdfas',Code=300725,Code_Str='300725',Report_Period='2019-09-09',Indicator_Name='NetProfit')


if __name__ == '__main__':
    tablename = "stock_300725"
    createTable(tablename)
