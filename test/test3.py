import time

# coding = 'utf-8'
from selenium import webdriver
from bs4 import BeautifulSoup


def swipe_down(self, second):
    for i in range(int(second / 0.1)):
        js = "var q=document.documentElement.scrollTop=" + str(300 + 200 * i)
        self.browser.execute_script(js)
        time.sleep(0.1)
    js = "var q=document.documentElement.scrollTop=100000"
    self.browser.execute_script(js)
    time.sleep(0.2)


if __name__ == "__main__":
    url = 'http://data.eastmoney.com/'
    subject = 'bbsj/xjll/'
    stockCode = '300725'
    suffix = '.html'
    url1 = url + subject + stockCode + suffix

    baidu = "http://www.baidu.com"

    chrome_driver = r'C:\Python38\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe'

    options = webdriver.ChromeOptions()
    # 设置window.navigator.webdriver为false
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 禁止加载图片
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    browser = webdriver.Chrome(executable_path=chrome_driver, options=options)
    browser.get(url1)

    time.sleep(2)
    print('wait for 2 sec')

    # tbody里的每一行 <tr>
    trs1 = browser.find_elements_by_xpath('//table[@id="dt_1"]/tbody/tr')
    # thead里的每一行 <tr>
    trs2 = browser.find_elements_by_xpath('//table[@id="dt_1"]/thead/tr')
    # 先处理tbody
    for tr in trs1:
        tds = tr.find_elements_by_tag_name('td')
        # 每一行中的某些标签比较特殊，含有NCR成分，需要特别处理
        for index in range(0, len(tds)):
            # 取出td内部的span
            if index != 0 and index != len(tds) - 1:
                try:
                    span = tds[index].find_element_by_tag_name('span').get_attribute("innerText")
                    text = str(span).replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape')
                    print(text)
                except Exception as ex:
                    print(ex)
            else:
                print(tds[index].get_attribute("innerText"))

# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
    browser.quit()

# aa = a.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape')
