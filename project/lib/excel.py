#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import json
from collections import defaultdict

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
        #获取tablename表的内容，从第三行开始
        ws = wb.sheet_by_name(self.tablename)
        rows = 2
        data = []
        while rows < ws.nrows:
            list = []
            data.append(list)
            cols = 0
            while cols <ws.ncols:
                if type(ws.cell_value(rows,cols)) == float or type(ws.cell_value(rows,cols)) == int:

                    list.append(str(int(ws.cell_value(rows,cols))))
                else:
                    list.append(ws.cell_value(rows,cols))
                #print ws.cell_value(rows,cols)
                cols = cols + 1
            rows = rows + 1
        #将空格填满
        col = 3
        while col < len(data[0]):
            row = 0
            while row < len(data):
                if data[row][col] == "":
                    if row > 0:
                        if data[row - 1][col] != "":
                            data[row][col] = data[row - 1][col]
                row = row + 1
            col = col + 1
        #删除空格
        cols = len(data[0]) - 1
        row = 0
        while row < len(data):
            col = cols
            while col > 2:
                if data[row][col] == "":
                    data[row].pop(col)
                    col = col - 1
                else:
                    break
            row = row + 1
        return data

    def get_all_case(self):
        data = self.get_all_info()
        case_data = []
        cols = [1,2]
        row = 0
        while row < len(data):
            list = []
            case_data.append(list)
            for col in cols:
                list.append(data[row][col])
            row = row + 1
        return case_data

    def get_case(self,case_no):
        data = self.get_all_info()
        data_list = []
        case_row = None
        row = 0
        while row < len(data):
            if data[row][0] == case_no:
                case_row = row
                break
            row = row + 1
        if case_row == None:
            print "The Case Not Exist!"
            exit(0)
            return None
        i = 0
        while i < 3:
            data_list.append(data[row][i])
            i = i + 1
        return data_list

    def get_cases(self,dirname):
        dir_data = self.get_dir_tree(dirname)
        if dir_data == False:
            print "The dictory is not Exist"
            exit(0)
        return dir_data
        row = 0
        data_list = []
        while row < len(dir_data):
            class_list = []
            data_list.append(class_list)
            class_list.append(dir_data[row][len(dir_data[row]) - 3])
            class_list.append(dir_data[row][len(dir_data[row]) - 2])
            class_list.append(dir_data[row][len(dir_data[row]) - 1])
            row = row + 1
        return data_list


    def get_all_tree(self):
        data = self.get_all_info()
        i = 0
        while i < len(data):
            j = 0
            while j < 3:
                data[i].append(data[i][0])
                del data[i][0]
                j = j + 1
            i = i + 1
        #for a in data:
        #    print a
        return data

    def get_dir_tree(self,dirname):
        data = self.get_all_info()
        #for i in data:
        #    print i
        #找到对应文件夹起始位置
        #print dirname
        find = False
        dir_col = None
        dir_row = None
        row = 0
        while row < len(data):
            col = 3
            while col < len(data[row]):
                if data[row][col] == dirname:
                    find = True
                    dir_row = row
                    dir_col = col
                    break
                col = col + 1

            if find:
                break
            row = row + 1
        if dir_col == None or dir_row == None:
            return False
        #print dir_row
        #print dir_col
        #找到对应文件夹结束的行
        dir_last_row = None
        find_row = dir_row + 1
        while find_row  < len(data):
            if data[find_row][col] != dirname:
                dir_last_row = find_row
                break
            find_row = find_row + 1
        if dir_last_row == None:
            dir_last_row = len(data)

        #print dir_last_row
        #转换顺序
        dir_data = []
        row = dir_row
        while row < dir_last_row:
            list = []
            dir_data.append(list)
            col = dir_col
            while col < len(data[row]):
                list.append(data[row][col])
                col = col + 1
            col = 0
            while col < 3:
                list.append(data[row][col])
                col = col + 1
            row = row + 1
        #for i in dir_data:
        #    print i
        return dir_data

        #dir_tree = tree()
        #dir_tree["a"]["b"]["c"]
        #print json.dumps(dir_tree)

#迭代，以防止出现keyerror，当建不存在时
def tree():
    return defaultdict(tree)
