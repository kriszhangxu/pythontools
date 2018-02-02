#!/bin/bash
# -*- encoding: utf8 -*-

import openpyxl
import datetime
import time
import codecs

def CreatExcel(database, filepath='./'):
    """
    创建excel,并添加数据，并且返回excel的地址,使用xlwt时,有最大行数的限制
    """
    titleArr = [u'姓名', u'年龄']
    wb = openpyxl.Workbook()
    lye, lmon = getlast_month()
    sheetName = '%s年%s月'%(lye, lmon)
    wb.create_sheet(index=0,title=codecs.decode(sheetName,"utf-8"))
    ws = wb.get_sheet_by_name(codecs.decode(sheetName,"utf-8"))
    wb.get_active_sheet()
    ws.append(titleArr)
    for row,val in enumerate( database ):
        ws.append(tuple(val))
    excelName = datetime.date(datetime.date.today().year,datetime.date.today().month,1).strftime('%Y%m%d')+str(int(time.time()))+".xlsx"
    savePath = filepath+reviewtype['savepath']+'/'+excelName
    wb.save(savePath)
    return savepath

def getlast_month():
    """
    获取上个月第一天的日期
    return: 返回日期
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
    datas = [["张三",19],["李四",20]]
    CreatExcel(datas)
    
