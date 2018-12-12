# -*- coding:utf-8 -*-

__author__ = 'cutieyy'

import random
import os
import xlsxwriter
import writeRandom

#os.mkdir('/Users/momo/PycharmProjects/week_1/random_test')

if __name__ == '__main__':
    str1="random"
    for i in range(1,101):
        filename=str1+str(i)+'.xlsx'
        file_path = os.path.join('/Users/momo/PycharmProjects/week_1/random_test', filename)
        xls = writeRandom.XlsAPI(file_path)
        # 创建Excel对象
        xls.xlsOpenWorkbook()
        # 添加工作对象
        sheet_names = ['sheet1', 'sheet2', 'sheet3']
        for sheet_name in sheet_names:
            sheet = xls.xlsAddWorksheet(sheet_name)
            # Excel的标题
            xls.addWorksheetTitle(sheet, ['数字编号', '生成的随机数（0-1000）'])
            # Excel的数据
            for i in range(1, 101):
                xls.appendWorkshetData(sheet, [i, random.randint(1, 1000)])

            xls.setWorksheetWidth(sheet)

        xls.xlsCloseWorkbook()

