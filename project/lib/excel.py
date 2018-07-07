#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd

from collections import defaultdict

#Author:fured
#date:2018.07.01
#desc:Operation case excel table

class Excel(object):
    #desc:初始化用例表
    #parameter:filename:用例表文件名
    #          talename:用例表名
    def __init__(self,filename,talename):
        self.filename = filename
        self.tablename = talename

    #desc:获取整张表的信息，除了两行标题
    def get_all_info(self):
        #打开文件
        wb = xlrd.open_workbook(self.filename)
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
                cols = cols + 1
            rows = rows + 1
        #将空格填满，由于表格进行了合并单元格，所以有很多空格
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
        #删除空格，这时的空格是由于目录各个用例的目录层级不同导致的，应该删除
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

    #desc：返回所有的案例信息
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

    #desc:返回指定的一个或多个用例信息
    #parameter：case_no：用例编号
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

    #desc:返回指定文件夹中所有的用例信息
    #parameter:dirname：文件夹的名字
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

    #desc：返回整个目录的信息
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
        return data

    #desc：返回指定目录的目录树信息
    def get_dir_tree(self,dirname):
        data = self.get_all_info()
        #找到对应文件夹起始位置
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
        return dir_data
