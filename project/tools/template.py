#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re
from config.env import Ftest
from lib.excel import Excel

#获取模板的路径，之前设置了环境变量
TEMPLATEPATH = os.environ.get("TEMPLATEPATH")

#Auther:fured
#date:2018.07.01
#desc:生成测试案例模板

class Template(object):
    def __init__(self,filename,tablename):
        self.filename = filename
        self.tablename = tablename

    def write_header(self,fp_case_file):
        fp_header = open(TEMPLATEPATH+"/testcase/header.py", "r")
        line_list = fp_header.readlines()
        for line in line_list:
            fp_case_file.write(line)
        fp_header.close()

    def write_case(self,fp_case_file):
        case_list = Excel(self.filename,self.tablename).get_all_case()
        if len(case_list) == 0:
            print "The table:" + Ftest.tablename + "not test case!"
        fp_case = open(TEMPLATEPATH+"/testcase/case.py","r")
        line_list = fp_case.readlines()
        fp_case.close()
        row = 0
        while row < len(case_list):
            line_list[1] = re.sub("CLASS_NAME", case_list[row][1], line_list[1])
            for line in line_list:
                fp_case_file.write(line)
            line_list[1] = 'class CLASS_NAME(object):\n'
            row = row + 1

    def generate_file(self,filename):
        fp_case_file = open(filename, "wb")
        self.write_header(fp_case_file)
        self.write_case(fp_case_file)
        fp_case_file.close()