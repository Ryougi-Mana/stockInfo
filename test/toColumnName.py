if __name__ == '__main__':

    english_filePath = './eng/profit_statement'

    chinese_filePath = './chin/profit_statement'
    # test/eng/main_indicators
    codeList: list = []

    with open(english_filePath, mode='r', encoding='utf-8') as english_f:
        with open(chinese_filePath, mode='r', encoding='utf-8') as chinese_f:

            contents = english_f.readlines()
            comments = chinese_f.readlines()

            for content in contents:
                columns_name = content.replace('\n', '')
                if columns_name != '':
                    columns_name = str(columns_name).replace(' ', '_')
                    columns_name = columns_name.replace('_(days)', '')
                    columns_name = columns_name.replace('_(Times)', '')
                    columns_name = columns_name.replace('_(yuan)', '')
                    columns_name = columns_name.replace('_($)', '')
                    columns_name = columns_name.replace('\'', '')
                    columns_name = columns_name.replace('Including:_', 'Including_')
                    code = columns_name
                    codeList.append(code)
            for index in range(0, len(comments)):
                comment = str(comments[index]).replace('\n', '')
                if comment != '':
                    codeFrag = " = Column(String(32), default='', comment='" + comment + "', unique=False)"
                    codeList[index] += codeFrag

            for code in codeList:
                print(code)
