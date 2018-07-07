#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

#Auther:fured
#date:2018.07.02
#desc:Generate test report

#模板的路径，之前设置了环境变量
TEMPLATEPATH = os.environ.get("TEMPLATEPATH")

class Report(object):

    #desc：初始化Report类
    #parameter：case_data:用例信息
    #           report_name:报告文件名
    def __init__(self,case_data,report_name):
        self.case_data = case_data
        self.report_name = report_name

    #desc：生成一个或者指定的几个案例的运行报告
    #parameter：show_data：案例信息
    #          show_case:每个运行过程中的信息
    def generate_one_html(self,show_data,show_case):
        fp_report = open(self.report_name,"w")
        write_header(fp_report,show_data)
        i = 0
        while i < len(self.case_data):
            case_name = self.case_data[i][len(self.case_data) - 3] + self.case_data[i][len(self.case_data) - 2]
            j = 0
            sign = False
            while j < len(show_case):
                if case_name == show_case[j][0]:
                    write_case(fp_report, show_case[j])
                    sign = True
                    break
                j = j + 1
            if sign == False:
                write_case(fp_report, None)
            i = i + 1
        write_end(fp_report)
        fp_report.close()
        return None

    # desc：生成指定文件夹中案例的运行报告
    # parameter：show_data：案例信息
    #           show_case:每个运行过程中的信息
    def generate_dir_html(self,show_data,show_case):
        fp_report = open(self.report_name,"w")
        write_header(fp_report,show_data)
        row = 0
        pre_dir_name = ""
        while row < len(self.case_data):
            dir_name = ""
            dir_col = 0
            while dir_col < len(self.case_data[row]) - 3:
                dir_name = dir_name + "/" + self.case_data[row][dir_col]
                dir_col = dir_col + 1
            if row == 0:
                write_dir_header(fp_report,dir_name)
                case_name = self.case_data[row][len(self.case_data[row]) - 3] + self.case_data[row][len(self.case_data[row]) - 2]
                j = 0
                sign = False
                while j < len(show_case):
                    if case_name == show_case[j][0]:
                        write_case(fp_report, show_case[j])
                        sign = True
                        break
                    j = j + 1
                if sign == False:
                    write_case(fp_report, None)

                if row == len(self.case_data) - 1:
                    write_dir_end(fp_report)
                row = row + 1
                pre_dir_name = dir_name
                continue
            if dir_name == pre_dir_name:
                case_name = self.case_data[row][len(self.case_data[row]) - 3] + self.case_data[row][len(self.case_data[row]) - 2]
                j = 0
                sign = False
                while j < len(show_case):
                    if case_name == show_case[j][0]:
                        write_case(fp_report, show_case[j])
                        sign = True
                        break
                    j = j + 1
                if sign == False:
                    write_case(fp_report, None)
            else:
                write_dir_end(fp_report)
                write_dir_header(fp_report,dir_name)
                case_name = self.case_data[row][len(self.case_data[row]) - 3] + self.case_data[row][len(self.case_data[row]) - 2]
                j = 0
                sign = False
                while j < len(show_case):
                    if case_name == show_case[j][0]:
                        write_case(fp_report, show_case[j])
                        sign = True
                        break
                    j = j + 1
                if sign == False:
                    write_case(fp_report, None)
            if row == len(self.case_data) - 1:
                write_dir_end(fp_report)
            pre_dir_name = dir_name
            row = row + 1
        write_end(fp_report)
        fp_report.close()
        return None

#desc:写报告html文件的头信息
def write_header(fp,show_data):
    fp_header = open(TEMPLATEPATH+"/report/header.html", "r")
    line_list = fp_header.readlines()
    for line in line_list:
        line = re.sub("SUITE_NAME",show_data["suite_name"], line)
        line = re.sub("SUITE_DESC", show_data["suite_desc"], line)
        line = re.sub("START_TIME", show_data["start_time"], line)
        line = re.sub("CASE_COUNT_TOTAL", str(show_data["case_count"]["total"]), line)
        line = re.sub("CASE_COUNT_FAIL", str(show_data["case_count"]["fail"]), line)
        line = re.sub("ASSERT_COUNT_TOTAL", str(show_data["assert_count"]["total"]), line)
        line = re.sub("ASSERT_COUNT_FAIL", str(show_data["assert_count"]["fail"]), line)
        line = re.sub("RUN_TIME", str(show_data["run_time"]), line)
        line = re.sub("DATA_SIZE", str(show_data["data_size"]), line)
        line = re.sub("AVG_RESPONSE_TIME", str(show_data["avg_response_time"]), line)
        fp.write(line)
    fp_header.close()

#desc:写报告html文件中目录的头信息
def write_dir_header(fp,dir_name):
    fp_dir_header = open(TEMPLATEPATH+"/report/dir_header.html")
    line_list = fp_dir_header.readlines()
    for line in line_list:
        line = re.sub("DIREECTOR_NAME",dir_name,line)
        fp.write(line.encode("utf8"))
    fp_dir_header.close()

#desc:写报告html文件中目录的尾信息
def write_dir_end(fp):
    fp_dir_end = open(TEMPLATEPATH + "/report/dir_end.html")
    line_list = fp_dir_end.readlines()
    for line in line_list:
        fp.write(line)
    fp_dir_end.close()

#desc：写案例的信息
def write_case(fp,show_case):
    fp_case = open(TEMPLATEPATH+"/report/case.html","r")
    line_list = fp_case.readlines()
    if show_case == None:
        for line in line_list:
            fp.write(line)
        fp_case.close()
        return None
    for line in line_list:
        if show_case != None:
            line = re.sub("CASE_NAME", show_case[0],line)
            line = re.sub("REQUEST_METHOD", show_case[1], line)
            line = re.sub("REQUEST_URL", show_case[2], line)
            line = re.sub("RESPONSE_TIME", str(show_case[3]), line)
            line = re.sub("DATA_SIZE", str(show_case[4]), line)
            line = re.sub("STATUS_CODE", str(show_case[5]), line)
            assert_info = ""
            if len(show_case[6]) != 0:
                for (key,value) in show_case[6].items():
                    if value == 1:
                        assert_info = assert_info + "<tr><td>" + key + "</td><td>" + str(value) + "</td><td>0</td></tr>"
                    else:
                        assert_info = assert_info + "<tr><td>" + key + "</td><td>0</td><td>"+ str(value) +"</td></tr>"
            line = re.sub("ASSERT_INFO",assert_info,line)
        fp.write(line.encode("utf-8"))
    fp_case.close()

#desc:写报告html文件的尾信息
def write_end(fp):
    fp_end = open(TEMPLATEPATH+"/report/end.html","r")
    line_list = fp_end.readlines()
    for line in line_list:
        fp.write(line)
    fp_end.close()
