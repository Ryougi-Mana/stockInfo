# coding = 'utf-8'
import uuid

from selenium import webdriver
import time
from entity.finance import main_indicators, balance_sheets, profit_statement, cash_flow_statement
from entity.finance.main_indicators import MainIndicators
from entity.finance.balance_sheets import BalanceSheets
from entity.finance.profit_statement import ProfitStatement
from entity.finance.cash_flow_statement import CashFlowStatement


def swipe_down(self, second):
    for i in range(int(second / 0.1)):
        js = "var q=document.documentElement.scrollTop=" + str(300 + 200 * i)
        self.browser.execute_script(js)
        time.sleep(0.1)
    js = "var q=document.documentElement.scrollTop=100000"
    self.browser.execute_script(js)
    time.sleep(0.2)


def processData(reporting_periods, indicators, report_statement_type, scroll_to_left, scroll_to_right):
    print('====>当前处理的财务报表是:[', report_statement_type, ']')
    l: int = len(reporting_periods)
    # 批量插入的列表

    entityList: list = []
    # 由于不移动table，table中的部分数据会不可见，所有要移动整个table。
    steps = 6
    if report_statement_type == '主要指标':
        steps = 6
    else:
        steps = 5
    lastSteps = l % steps
    offsets = l - l % steps
    # 循环该报表中的每一列 X++;
    for report_period_index in range(0, l):
        # 切换到每一个表格的时候，可见的报告期表头最少是5个
        try:
            entity = processColumns(indicators, reporting_periods, report_period_index, report_statement_type)
            entityList.append(entity)
        except Exception as ex:
            print(ex)

        # 如果偏移量是步长的整数倍并且偏移量已经大于0了，那么就要进行一次step步长的网格右移
        if (report_period_index + 1) % steps == 0 and report_period_index > 0 and l - (
                report_period_index + 1) > lastSteps:
            for count in range(steps):
                # 多次向右移动
                scroll_to_right.click()
                time.sleep(0.1)
            time.sleep(1)
        # 临近末尾不需要多次右移，只需要单次偏移
        # 最后一次不能再向右位移，否则会有异常出现
        if offsets < report_period_index + 1 < offsets + steps:
            if report_period_index + 1 < offsets + lastSteps:
                try:
                    scroll_to_right.click()
                except Exception as ex:
                    print('[Error：现在是第]', report_period_index + 1, '列', '；总共有：', l, '列')
                    print(ex)
                finally:
                    time.sleep(0.3)

            # 批量插入
    if report_statement_type == '主要指标':
        cash_flow_statement.insertPatch(entityList)
    elif report_statement_type == '资产负债表':
        cash_flow_statement.insertPatch(entityList)
    elif report_statement_type == '利润表':
        cash_flow_statement.insertPatch(entityList)
    elif report_statement_type == '现金流量表':
        cash_flow_statement.insertPatch(entityList)


def matchCorresponCols(entity, dataList):
    for index in range(0, len(dataList)):
        attrName = entity.__dir__()[index + 3]
        attrValue = dataList[index]
        entity.__setattr__(attrName, attrValue)
    return entity


def processColumns(indicators, reporting_periods, report_period_index, report_statement_type):
    report_period = reporting_periods[report_period_index].text
    print("==>目前处理的报告期是:[", report_period, ']')
    # 用作填充数据库的对象
    dataList: list = []
    uuidStr = str(uuid.uuid4()).replace('-', '')
    # UUID 序号
    dataList.append(uuidStr)
    # 股票代码 整型
    dataList.append(stockCode)
    # 股票代码 字符串
    dataList.append(stockCode_Str)
    # 报告期
    dataList.append(report_period)
    # 返回的实例对象
    entity = None
    for indicator_index in range(0, len(indicators)):
        try:
            # 指标名字
            # indicator_name = indicators[indicator_index].find_element_by_tag_name('th').text
            # 指标数据
            indicator_data = data_rows[indicator_index].find_elements_by_tag_name('td')[report_period_index].text
            # print(indicator_name, '=', indicator_data, ';', end='')
            dataList.append(indicator_data)
        except Exception as ex:
            print(ex.args)
        # finally:
    if report_statement_type == '主要指标':
        entity = matchCorresponCols(MainIndicators(), dataList)
        # main_indicators.insert(entity)
    elif report_statement_type == '资产负债表':
        entity = matchCorresponCols(BalanceSheets(), dataList)
        # balance_sheets.insert(entity)
    elif report_statement_type == '利润表':
        entity = matchCorresponCols(ProfitStatement(), dataList)
        # profit_statement.insert(entity)
    elif report_statement_type == '现金流量表':
        entity = matchCorresponCols(CashFlowStatement(), dataList)
        # cash_flow_statement.insert(entity)
    print('======第[', report_period_index, ']列已被处理======', '\n')
    return entity


# 调整 <div class="data_tbody">的style:left值
# def scroll_to_right(browser):
#     js = '''let data_tbody = document.getElementsByClassName("data_tbody")[0];
#             let org_indent = parseInt(data_tbody.style.left.replace('px',''));
#             console.log("宽度：", org_indent-126)
#             new_indent = (org_indent-126).toString() + "px"
#             data_tbody.setAttribute("style":new_indent)'''
#     browser.browser.execute_script(js)


def genURL(stockCode):
    # 同花顺 单股页面 网站域名
    url = 'http://stockpage.10jqka.com.cn/'
    # 财务报表 项目
    subject = '/finance'
    return url + stockCode + subject


if __name__ == "__main__":

    # 测试代码
    stockCode = '600008'
    stockCode_Str = 600008
    url1 = genURL(stockCode)

    chrome_driver = r'C:\Python38\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
    # 获取chrome浏览器的所有可选项
    options = webdriver.ChromeOptions()
    # 设置window.navigator.webdriver为false
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 禁止加载图片
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # google浏览器
    broswer = webdriver.Chrome(executable_path=chrome_driver, options=options)
    # 全屏显示
    broswer.maximize_window()
    # 开始计时
    time_start = time.time()
    # 发起请求，主要指标
    broswer.get(url1)
    # 休眠
    time.sleep(0.2)

    # 切换iframe 以保证准确定位
    broswer.switch_to.frame('dataifm')

    # 获取财务报表所有的表的类型
    sideNav = broswer.find_elements_by_xpath('//*[@id="cwzbDemo"]/div[2]/ul/li')

    # 表格向右移动的按钮，是一个带有onclick事件的<div>标签，click()点击后会<div class="data_tbody">标签的style={left:146px}会变成left:20px
    scroll_to_right = broswer.find_element_by_xpath('//div[@class="table_data"]/div[2]')
    # 表格向右移动的按钮
    scroll_to_left = broswer.find_element_by_xpath('//div[@class="table_data"]/div[1]')

    # 循环每一个报表
    for report_type in range(0, len(sideNav)):

        # 头部：报告期的时间点
        # X轴长短
        reporting_periods = broswer.find_elements_by_xpath('//div[@class="data_wraper"]/div/table[1]/tbody/tr/th')

        # 边侧栏目，有者各种指标，都是可见的! 表中的每一个字段的名字都在这里
        # Y轴长短
        indicators = broswer.find_elements_by_xpath('//div[@class="left_thead"]/table[2]/tbody/tr')

        # 数据表格(每一行) 是一个list 用列表下标(Y轴)确认是哪一行 data_rows[?]
        data_rows = broswer.find_elements_by_xpath('//div[@class="data_wraper"]/div/table[2]/tbody/tr')

        # 导航栏中的当前链接
        sheet_href = sideNav[report_type].find_element_by_tag_name('a')

        # 当前报表名称
        report_statement_type = broswer.find_elements_by_xpath('//div[@id="cwzbDemo"]/div[2]/ul/li')[report_type].text

        # for indicator_index in range(0, len(indicators)):
        #     print(indicators[indicator_index].find_element_by_tag_name('th').text)
        print("=============================================================")
        # 主要指标已经
        if report_type == 0:
            # 含有子表的每一个<li>
            main_indicator = sideNav[report_type].find_elements_by_xpath('//div[@class="menubox"]/ul[1]/li')
            # 处理数据
            processData(reporting_periods, indicators, report_statement_type, scroll_to_left, scroll_to_right)

            # main_indicator = sideNav[index].find_elements_by_xpath('//div[@class="sub-a"]')
            # 存储主要指标表
            for indicator in main_indicator:
                # 主要指标下的每一个子表
                sub_sheet = indicator.find_element_by_tag_name('a')
                # browser.switch_to.frame('dataifm')
                # try:
                #     sub_sheet.click()
                # except Exception as ex:
                #     print(ex)
                # finally:
                print(sub_sheet.get_attribute('innerText'), '输出了', end='')
            print(report_statement_type, '输出了')

        # 切换表格！ 资产负债表 利润表 现金流量表
        elif report_type == 1:
            # 处理数据
            processData(reporting_periods, indicators, report_statement_type, scroll_to_left, scroll_to_right)
            # print('')
        elif report_type == 2:
            # 处理数据
            processData(reporting_periods, indicators, report_statement_type, scroll_to_left, scroll_to_right)
            # print('')
        elif report_type == 3:
            # 处理数据
            processData(reporting_periods, indicators, report_statement_type, scroll_to_left, scroll_to_right)
            # print('')
        # X轴 Y轴 重新定位        # relocate the tab
        # 如果不是最后一页
        if report_type < len(sideNav):
            try:
                # 切换表格！ 资产负债表
                # 导航栏中的下一个链接
                next_sheet_href = sideNav[report_type + 1].find_element_by_tag_name('a')
                next_sheet_href.click()
                time.sleep(1)
                broswer.switch_to.frame('dataifm')
            except Exception as ex:
                print(ex)
            finally:
                print(sheet_href.text, '输出完毕')

    print('ready to close the browser!')
    time_end = time.time()
    print('time cost', time_end - time_start, 's')
    broswer.close()
