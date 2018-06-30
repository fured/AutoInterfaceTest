#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd


class Excel(object):
    def __init__(self,filename,talename):
        self.filename = filename
        self.tablename = talename

    def get_all_info(self):
        #打开文件
        wb = xlrd.open_workbook(self.filename)
        #print wb.nsheets
        #判断表是否存在
        sheetname = []
        for sheet in wb.sheets():
            sheetname.append(sheet.name)
        if self.tablename not in sheetname:
            return "table " + self.tablename + " not exist!"

        ws = wb.sheet_by_name(self.tablename)
        rows = 0
        data = []
        while rows < ws.nrows:
            list = []
            data.append(list)
            cols = 0
            while cols <ws.ncols:
                list.append(ws.cell_value(rows,cols))
                #print ws.cell_value(rows,cols)
                cols = cols + 1
            rows = rows + 1

        for i in data:
            print i
        #print  ws.row_values(0)

