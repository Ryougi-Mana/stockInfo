import time
import uuid

from selenium import webdriver
from bs4 import BeautifulSoup
from entity.finance import main_indicators, balance_sheets, profit_statement, cash_flow_statement
from entity.finance.main_indicators import MainIndicators
from entity.finance.balance_sheets import BalanceSheets
from entity.finance.profit_statement import ProfitStatement
from entity.finance.cash_flow_statement import CashFlowStatement
from entity.stockList import Stocks


def launchChrome():
    chrome_driver = r'C:\Python38\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
    # 获取chrome浏览器的所有可选项
    options = webdriver.ChromeOptions()
    # 设置window.navigator.webdriver为false
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 谷歌文档提到需要加上这个属性来规避bug
    options.add_argument('--disable-gpu')
    # 禁止加载图片
    options.add_argument('blink-settings=imagesEnabled=false')
    # 浏览器不提供可视化页面
    options.add_argument('--headless')
    # 伪装为手机请求头
    options.add_argument(
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/74.0.3729.157 Mobile Safari/537.36')

    # google浏览器
    explorer = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return explorer


def processStock(broswer):
    # 开始请求的计时
    time_request = time.time()
    # 获取页面
    broswer.get(url)
    print(stockCode_Str, ':Url-Request Time Cost', time.time() - time_request, 's')
    # 开始计时
    time_start = time.time()
    # 切换iframe 以保证准确定位
    broswer.switch_to.frame('dataifm')
    # 获取财务报表所有的表的类型
    sideNav = broswer.find_elements_by_xpath('//*[@id="cwzbDemo"]/div[2]/ul/li')

    for report_type in range(0, len(sideNav)):
        if report_type >= 4:
            break
        # 当前报表名称
        report_statement_type = sideNav[report_type].text
        print('Current Finance Report Statement:', report_statement_type)
        # 导航栏中的当前链接
        sheet_href = sideNav[report_type].find_element_by_tag_name('a')

        html = BeautifulSoup(broswer.page_source, 'lxml')
        left_div = html.select(".left_thead")
        # 各项指标
        indicators = BeautifulSoup(str(left_div), 'lxml').select('th')
        # for indicator in indicators:
        # print(indicator.text)

        # 数据表格<table>
        # 包含 报告期
        # 包含报告期下的各个财务数据
        right_div = html.select('.data_tbody')
        data_and_periods = BeautifulSoup(str(right_div), 'lxml')
        periods_table = data_and_periods.select('.top_thead')
        periods = BeautifulSoup(str(periods_table[0]), 'lxml').find_all('div', class_='td_w')

        # 创建对象列表 根据报表类型的不同 分别创建不同的PO对象
        entityList = []
        for i in range(0, len(periods)):
            uuidStr = str(uuid.uuid4()).replace('-', '')
            report_period = periods[i].text
            print('[', report_period, ']', end='')
            entity = None
            # 主要指标
            if report_type == 0:
                entity = MainIndicators(Id=uuidStr, Code=stockCode, Code_Str=stockCode_Str, Report_Period=report_period)
            # 资产负债表
            elif report_type == 1:
                entity = BalanceSheets(Id=uuidStr, Code=stockCode, Code_Str=stockCode_Str, Report_Period=report_period)
            # 利润表
            elif report_type == 2:
                entity = ProfitStatement(Id=uuidStr, Code=stockCode, Code_Str=stockCode_Str,
                                         Report_Period=report_period)
            # 现金流量表
            elif report_type == 3:
                entity = CashFlowStatement(Id=uuidStr, Code=stockCode, Code_Str=stockCode_Str,
                                           Report_Period=report_period)

            entityList.append(entity)

        # 数据表格
        data_table = data_and_periods.select('.tbody')
        # 整个表格的数据
        dataGrid = BeautifulSoup(str(data_table), 'lxml').select('tr')

        # 处理每一行
        for y in range(0, len(dataGrid)):
            # 处理每一列
            # print('==>第', y + 1, '行')
            datas = dataGrid[y].contents
            for x in range(0, len(datas)):
                po = entityList[x]
                attrName = po.__dir__()[y + 7]
                attrValue = datas[x].text
                po.__setattr__(attrName, attrValue)
                # print('[', attrName, '=', attrValue, ']', end='')

        # 存入数据库
        if report_type == 0:
            main_indicators.insertPatch(entityList)
        elif report_type == 1:
            balance_sheets.insertPatch(entityList)
        elif report_type == 2:
            profit_statement.insertPatch(entityList)
        elif report_type == 3:
            cash_flow_statement.insertPatch(entityList)

        # relocate the tab
        # 如果不是最后一页，就切换表格！
        try:
            if report_type < len(sideNav) - 1:
                # 点击导航栏中的下一个链接
                sideNav[report_type + 1].find_element_by_tag_name('a').click()
                time.sleep(1)
                # broswer.switch_to.frame('dataifm')
        except Exception as ex:
            print(ex)
        finally:
            print(sheet_href.text, '输出完毕')

    print(stockCode_Str, ':Data-Handle Time Cost', time.time() - time_start, 's')


# 启动浏览器
print('\n', 'ready to launch the browser!')
broswer = launchChrome()
domain = 'http://stockpage.10jqka.com.cn/'
# 这次要处理的股票的所有代码 起步位置 股票数量 板块类型
stockList = Stocks.selectBunchOfCode(startNo=0, size=5, market_type=0)
for stock in stockList:
    stockCode_Str = stock
    subject: str = '/finance'
    try:
        stockCode = int(stockCode_Str)
    except Exception as ex:
        print(ex)
    finally:
        url = 'http://stockpage.10jqka.com.cn/' + stockCode_Str + subject
        broswer.get(url=url)
        # 处理数据
        processStock(broswer)
print('\n', 'ready to close the browser!')
broswer.close()
broswer.quit()
