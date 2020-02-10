# coding='utf-8
v = None
import re,uuid


def fun():
    for i in range(10):
        if i == 0:
            global v
            v = 1
        else:
            v = v + 1
    print('v=', v)

def cleanHeadZeroNum(string):
    return string.lstrip('0')


if __name__ == '__main__':

    codeStr = "(umdd)UltraPro MidCap400"
    codeSplict = codeStr.split(")")
    codeSplict2 = codeSplict[0].split("(")
    print(codeSplict[1])
    print(codeSplict2[1])


    uuidStr = str(uuid.uuid4()).replace('-','')

    print(uuid.uuid4())
    print(uuidStr)
    print(uuidStr.__len__())

    string = "(003251)我的"
    print(re.findall(r"\d+\.?\d*", string))
    print(re.sub("\D", "", string))


    print(cleanHeadZeroNum("007025"))
    # ['1.45', '5', '6.45', '8.82']

    sql = str('insert into stocks(code,name,market,market_type) value(')
    code = 600000
    name = '浦发银行'
    market = '沪市'
    market_type = 0
    sql = sql + str(code) + ","
    sql = sql + "'" + name + "',"
    sql = sql + "'" +market + "',"
    sql = sql + str(market_type)
    sql = sql + ")"

    print(sql)
    fun()
