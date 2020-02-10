# coding=utf-8
import time
import uuid
from bs4 import BeautifulSoup
import utils

# 东方财富网股吧地址
from entity import curd
from entity.Stocks import Stocks

URL_base = 'http://guba.eastmoney.com/'
URL_append = 'remenba.aspx?type=1&tab=1'
URL = URL_base + URL_append


# 针对股票列表作出选择
def getStockList(url: str):
    htmlContent = utils.getHtml(url)
    # 获取股票页面
    bs = BeautifulSoup(htmlContent, 'lxml')
    # 按照class选择ul
    ul = bs.select(".ngblistul2")
    # ul字符串化，bs对象化
    soup = BeautifulSoup(str(ul), 'lxml')
    # 选出soup里所有的<a>标签
    # 含有InnerText或者href属性 分别是股票的名字和代码
    stockList = soup.find_all("a")
    return stockList


# 以本地文件为源
# soup = BeautifulSoup(open(r"C:\Users\Administrator\Desktop\stockList.html", mode='rb'), 'lxml')

soup = BeautifulSoup(utils.getHtml(URL), 'lxml')
# 获取股票种类
ul0 = soup.find_all("ul", class_="market_tab")
soup0 = BeautifulSoup(str(ul0), 'lxml')
a0s = soup0.find_all("a")

# 股票板块的链接和名字
dictOfStock = {}
for a0 in a0s:
    name = a0.string
    href = a0.attrs['href']
    print(name)
    print(href),
    dictOfStock[name] = href

# 获取所有的板块下的所有股票的代码和名称，写入数据库
# 获取HTML，并且分析出BeautifulSoup对象
stocks = getStockList(url=URL)
marketType = 0
# market是股票板块名称，url是股票板块的网站链接
for market, url in dictOfStock.items():
    stocks = getStockList(url)
    dataList = []
    for stock in stocks:
        text = stock.string
        # 从字符串提取股票的代码
        stockCode = utils.extractStockCode(text)
        # 从字符串提取股票的名称
        stockName = utils.extractStockName(text)
        # 存入股票的uuid和本业务无关
        stockId = str(uuid.uuid4()).replace('-', '')
        # 代码为非数字型的数字型代码都默认为0存入数据库
        code = 0
        # 美股代码是英文，股票名字可能是中英文混合，纯英文，纯中文，带有符号的英文
        if marketType == 3 or marketType == 4:
            code = 0
        else:
            code = int(stockCode.lstrip('0'))
        # 创建股票的对象
        data = Stocks(id=stockId,
                      code=code,
                      codeStr=stockCode,
                      name=stockName,
                      market=market,
                      market_type=marketType)
        # 堆入列表中
        dataList.append(data)

    # 批量写入
    curd.insertPatch(dataList)
    # 板块的种类序号
    marketType = marketType + 1
    print("程序沉睡2秒")
    time.sleep(2)
    print("程序再次执行")
