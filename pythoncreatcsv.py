# pythontools
#!/bin/bash
# -*- encoding: utf8 -*-
my python tools

import datetime
import codecs
import csv
class Ccsv:
    def CreatCsv(self, datas, savepath='./'):
        csvfile = self.getcsvname(savepath)
        CsvHeader = ["姓名","年龄"]
        f = open(csvfile, 'wb')
        #设定语言格式
        f.write(codecs.BOM_UTF8)
        #设定csv的导出格式
        writer = csv.writer(f, dialect='excel')
        writer.writerow(CsvHeader)
        for row in datas:
            writer.writerow(row)

        return csvfile

    def getcsvname(self, savepath):
        lye, lmon = self.getlast_month()
        #name = u'%s年%s月'
        name = "hotelinfo%s%s"%(lye, lmon)
        csvfile = savepath+name+".csv"
        return csvfile

    def getlast_month(self):
        """
        获取上个月第一天的日期
        :return: 返回日期
        """
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        if 1 == month:
            month = 12
            year -= 1
        else:
            month -= 1
        return year, month
        
if __name__ == "__main__":
    creatcsv = Ccsv()
    datas = [["张三",19],["李四",20]]
    creatcsv.CreatCsv(datas)
