# coding = 'utf-8'
from selenium import webdriver
import time


def swipe_down(self, second):
    for i in range(int(second / 0.1)):
        js = "var q=document.documentElement.scrollTop=" + str(300 + 200 * i)
        self.browser.execute_script(js)
        time.sleep(0.1)
    js = "var q=document.documentElement.scrollTop=100000"
    self.browser.execute_script(js)
    time.sleep(0.2)

def switch_Tab(self,index):
    lis = self.find_elements_by_xpath('//*[@id="cwzbDemo"]/div[2]/ul/li')

    a = lis[index].find_element_by_tag_name('a')
    if index != 0:
        try:
            # 切换表格！ 0主要指标 1资产负债表 2利润表 3现金流量表
            a.click()
            browser.switch_to.frame('dataifm')
        except Exception as ex:
            print(ex)
        finally:
            print(a.text, '输出了')
    else:
        print('无法定位到主要指标')


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
    code = '300725'
    url1 = genURL(code)

    chrome_driver = r'C:\Python38\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'
    # 获取chrome浏览器的所有可选项
    options = webdriver.ChromeOptions()
    # 设置window.navigator.webdriver为false
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 禁止加载图片
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # google浏览器
    browser = webdriver.Chrome(executable_path=chrome_driver, options=options)

    # 发起请求，主要指标
    browser.get(url1)
    # 休眠3秒钟
    time.sleep(3)

    # 切换iframe 以保证准确定位
    browser.switch_to.frame('dataifm')
    # 获取财务报表所有的表的类型
    lis = browser.find_elements_by_xpath('//*[@id="cwzbDemo"]/div[2]/ul/li')

    cwzbTable = browser.find_elements_by_xpath('//*[@id="cwzbTable"]')
    # 边侧栏目，有者各种指标，都是可见的!
    left_thead = browser.find_elements_by_xpath('//div[@class="left_thead"]/table[2]/tbody/tr')
    # 头部：报告期的时间点
    top_thead = browser.find_elements_by_xpath('//div[@class="data_wraper"]/div/table/tbody/tr/th')
    # 表格向右移动的按钮，是一个带有onclick事件的<div>标签，click()点击后会<div class="data_tbody">标签的style={left:146px}会变成left:20px
    scroll_to_right = browser.find_element_by_xpath('//div[@class="table_data"]/div[2]')

    # 输出当下 每种指标 item
    for item in left_thead:
        print(item.find_element_by_tag_name('th').text)

    # 输出该股票所有的报告期 report_date
    count = 0
    for item in top_thead:
        div = item.find_element_by_xpath('div[@class="td_w"]')
        try:
            if count < len(top_thead) - 6:
                scroll_to_right.click()
                print(div.text)
            else:
                print(div.text)
        except Exception as ex:
            print(ex)
        count = count + 1
        time.sleep(0.1)

    # 建立四张表
    # 主要指标 main_indicators
    # 利润表 income_statement
    # 资产负债表 balance_sheets
    # 现金流量表 cash_flow_statement
    # 每一张表除了他们自己的报告期(reporting period)以及各项项目(items)以外。还有这一项目具体的财务数字
    # reporting_period;items[0],item[1]------item[?],data,date_str(字符串形式)
    # for index in range(0, len(lis)):
    #     a = lis[index].find_element_by_tag_name('a')
    #     # 主要指标已经
    #     if index != 0:
    #         try:
    #             # 切换表格！ 资产负债表 利润表 现金流量表
    #             a.click()
    #             browser.switch_to.frame('dataifm')
    #         except Exception as ex:
    #             print(ex)
    #         finally:
    #             print(a.text, '输出了')

    print('ready to close the browser!')
    browser.close()
