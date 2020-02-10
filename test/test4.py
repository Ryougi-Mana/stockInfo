import time
import html


def dec(a):
    # &#x  开头  解码  :  以 &# 或 &#x 开头的字符串叫做 NCR 字符
    # 通过 py2.x下的HTMLParser 或 py3.x下的html 的 unescape() 方法来转换成能看懂的中文字符
    aa = a.replace(';', '').replace('&#x', '\\u').encode('utf-8').decode('unicode_escape')
    print(aa)
    return aa


def dec_r(b):
    # r'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'   开头  解码
    # python3 以上 字符串不能 直接 decode， 先编码成utf-8 ， 在进行解码
    bb = b.encode('utf-8').decode('unicode_escape')
    print(bb)
    return bb


if __name__ == '__main__':
    '''
        编码  解码
        '''
    a = '&#x3010;&#x8BD5;&#x547C;&#x3011;'  # 【试呼】
    a = '&#x0068;&#x0074;&#x0074;&#x0070;&#x003a;&#x002f;&#x002f;&#x0077;&#x0077;&#x0077;&#x002e;&#x0036;&#x0036;&#x0038;&#x0038;&#x002e;&#x0061;&#x0070;&#x0070;&#x0073;&#x0076;&#x0069;&#x0070;&#x0061;&#x0070;&#x0069;&#x002e;&#x006b;&#x0075;&#x0075;&#x0068;&#x0075;&#x0069;&#x002e;&#x0063;&#x006f;&#x006d;&#x003a;&#x0036;&#x0035;&#x0035;&#x0033;&#x0033;&#x002f;&#x0070;&#x006c;&#x006a;&#x0065;&#x002f;&#x0069;&#x0064;&#x002e;&#x0070;&#x0068;&#x0070;  '
    # http://www.6688.appsvipapi.kuuhui.com:65533/plje/id.php
    c = '&#xE273;.&#xE7A3;&#xE268;&#xE268;&#xE7A3;&#xEBC0;&#xE7A3;&#xE7A3;&#xE793;&#xF4CD;&#xE793;&#xEA5D;&#xEBC0;&#xF4CD;&#xE7A3;'

    dec(a)  # &#x  开头  解码
    dec(c)

    b = u'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'  # 直接打印出来 ————》 人生苦短，py是岸
    b = r'\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8'

    dec_r(b)

    d = r'\u58817'
    e = u'\uea5d'
    dec_r(e)
