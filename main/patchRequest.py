import time

from selenium import webdriver
from bs4 import BeautifulSoup
from entity.finance_sh import main_indicators, balance_sheets, profit_statement, cash_flow_statement,bank_specific_indicators
from entity.finance_sh.main_indicators import MainIndicators
from entity.finance_sh.balance_sheets import BalanceSheets
from entity.finance_sh.profit_statement import ProfitStatement
from entity.finance_sh.cash_flow_statement import CashFlowStatement
from entity.finance_sh.bank_specific_indicators import BankSpecificIndicators
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


def processData(dataGrid, periods, indicators, modelClaz, model):
    entityArray = []
    # 处理每一个列
    for x in range(0, len(periods)):
        # 处理每一行
        for y in range(1, len(indicators)):
            entity = modelClaz(Code=stockCode, Code_Str=stockCode_Str, Report_Period=periods[x].text)
            entity.Indicator_Name = indicators[y].text
            entity.Indicator_Data = dataGrid[y - 1].contents[x].text
            entityArray.append(entity)
        # 插入当前一列
    model.insertBatch(entityArray)


def processDataTable(report_statement_type, dataGrid, periods, indicators):
    # 该股当前报表的数据总量
    if report_statement_type == '主要指标':
        processData(dataGrid, periods, indicators, MainIndicators, main_indicators)
    elif report_statement_type == '资产负债表':
        processData(dataGrid, periods, indicators, BalanceSheets, balance_sheets)
    elif report_statement_type == '利润表':
        processData(dataGrid, periods, indicators, ProfitStatement, profit_statement)
    elif report_statement_type == '现金流量表':
        processData(dataGrid, periods, indicators, CashFlowStatement, cash_flow_statement)
    elif report_statement_type == '银行专项指标':
        processData(dataGrid, periods, indicators, BankSpecificIndicators, bank_specific_indicators)


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
        # 当前报表名称
        report_statement_type = sideNav[report_type].text
        print('Current Finance Report Statement:', report_statement_type)
        # 导航栏中的当前链接
        sheet_href = sideNav[report_type].find_element_by_tag_name('a')

        html = BeautifulSoup(broswer.page_source, 'lxml')
        left_div = html.select(".left_thead")
        # 各项指标
        indicators = BeautifulSoup(str(left_div), 'lxml').select('th')
        indicatorsNum = len(indicators)
        # for indicator in indicators:
        # print(indicator.text)

        # 数据表格<table>
        # 包含 报告期
        # 包含报告期下的各个财务数据
        right_div = html.select('.data_tbody')
        data_and_periods = BeautifulSoup(str(right_div), 'lxml')
        periods_table = data_and_periods.select('.top_thead')
        periods = BeautifulSoup(str(periods_table[0]), 'lxml').find_all('div', class_='td_w')

        # 数据表格
        data_table = data_and_periods.select('.tbody')
        # 整个表格的数据
        dataGrid = BeautifulSoup(str(data_table), 'lxml').select('tr')

        # 处理数据，存入数据库
        processDataTable(report_statement_type, dataGrid, periods, indicators)

        # relocate the tab
        # 如果不是最后一页，就切换表格！
        refreshFlag = False
        try:
            if report_type < len(sideNav) - 1:
                # 点击导航栏中的下一个链接
                sideNav[report_type + 1].find_element_by_tag_name('a').click()
                time.sleep(0.1)
                while not refreshFlag:
                    new_left_div = BeautifulSoup(broswer.page_source, 'lxml').select(".left_thead")
                    nextIndicatorSum = BeautifulSoup(str(new_left_div), 'lxml').select('th')
                    refreshFlag = indicatorsNum != len(nextIndicatorSum)
                # broswer.switch_to.frame('dataifm')
        except Exception as ex:
            print(ex)
        finally:
            print(sheet_href.text, '输出完毕')

    print(stockCode_Str, ':Data-Handle Time Cost', time.time() - time_start, 's')
    print("=====================================")


# 启动浏览器
print('\n', 'ready to launch the browser!')
broswer = launchChrome()
domain = 'http://stockpage.10jqka.com.cn/'
# 这次要处理的股票的所有代码 起步位置 股票数量 板块类型
# 500了
stockList = Stocks.selectBunchOfCode(startNo=0, size=1552, market_type=0)
# 批量处理
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
