# coding='utf-8
from bs4 import BeautifulSoup
import utils
from selenium import webdriver

if __name__ == "__main__":
    url = 'http://data.eastmoney.com/'
    subject = 'bbsj/xjll/'
    stockCode = '300725'
    suffix = '.html'
    url = url + subject + stockCode + suffix
    htmlContent = utils.getHtml(url)

    bs = BeautifulSoup(htmlContent, 'lxml')
    # print(bs.prettify())

    script = bs.select("script")
    bs1 = BeautifulSoup(str(script), 'lxml')
    print(str(bs1))

    browser = webdriver.chrome


    # aa = a.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape')
