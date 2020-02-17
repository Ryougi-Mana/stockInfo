from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entity.stockList.Stocks import Stocks

ENGINE = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/stock?charset=utf8mb4", )
DBSession = sessionmaker(bind=ENGINE)
session = DBSession()


# 所有数据一并提交
def insertPatch(dataList: list):
    for data in dataList:
        session.add(data)
    session.commit()


def closeSession():
    session.close()


if __name__ == '__main__':
    stock = Stocks('a',code=300725,codeStr='300725', name='药石科技', market="深市", market_type=1)
