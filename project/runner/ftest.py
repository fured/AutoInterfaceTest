#!/usr/bin/python
# -*- coding: UTF-8 -*-

import run
import sys

from config.env import Ftest
from lib.excel import Excel
from run import Run
from tools.report import Report
from tools.template import Template

"""
Auther:fured
date:2018.07.01
desc:Entrance for Ftest test system
"""


def get_case_file(filename, env_file):
    """
    生成一份测试用例文件

    :param filename: 生成模板即文件的名字，文件名字必须为：XXX.py（必选）
    :param env_file: 测试所需要的环境变量即设置，使用json文件的形式给出（必选）
                    其中，必须有的环境变量："testexcel"：测试用例表文件
                                         "tablename":测试用例表文件中，具体的哪张表
    :return:
    """
    # 初始化环境变量
    Ftest.init(env_file)
    template = Template(Ftest.testexcel,Ftest.tablename)
    template.generate_file(filename)


def run_one_testcase(case_no, env_file, report_name=None):
    """
    运行一个或者指定的某几个测试用例

    :param case_no: 需要运行的测试用例的编号，多个时使用逗号分隔，如：“1，2，5”（必选）
    :param env_file: 测试所需要的环境变量，使用json文件的形式给出（必选）
    :param report_name: 生成报告的文件名，必须是html文件（可选）
    :return:
    """
    # 初始化环境变量
    Ftest.init(env_file)
    case_list = case_no.split(",")
    class_name_list = []
    i = 0
    while i < len(case_list):
        class_name = Excel(Ftest.testexcel, Ftest.tablename).get_case(case_list[i])
        class_name_list.append(class_name)
        i = i + 1
    # 运行测试
    Run().run_one_case(class_name_list)
    if report_name is not None:
        # 生成测试报告
        report = Report(class_name_list, report_name)
        report.generate_one_html(run.INFO_REPORT, run.INFO_CASE)
        pass
    return None


def run_dir_testcase(dir_name, env_file, report_name=None):
    """
    运行指定文件夹下的所有用例

    :param dir_name: 文件夹的名字
    :param env_file: 测试所需要的环境变量，使用json文件的形式给出（必选）
    :param report_name: 生成报告的文件名，必须是html文件（可选）
    :return:
    """
    # 初始化环境
    Ftest.init(env_file)
    dir_name = dir_name.decode("GB2312")
    dir_name = dir_name.encode("utf-8")
    class_list = Excel(Ftest.testexcel, Ftest.tablename).get_cases(dir_name.decode('utf-8'))
    # 运行测试
    Run().run_dir_case(class_list)
    if report_name is not None:
        # 生成测试报告
        report = Report(class_list, report_name)
        report.generate_dir_html(run.INFO_REPORT, run.INFO_CASE)

        pass
    return None


def show_all_testcase(env_file):
    """
    展示测试用例整体的目录结构

    :param env_file: 测试所需的环境变量（必选）
    :return:
    """
    # 初始化环境变量
    Ftest.init(env_file)
    # 获取目录信息数据
    data = Excel(Ftest.testexcel, Ftest.tablename).get_all_tree()
    # 展示目录树
    show(data)
    return None


def show_dir_testcase(dirname, env_file):
    """
    展示指定目录的结构信息

    :param dirname:文件夹名
    :param env_file: 测试所需的环境变量（必选）
    :return:
    """
    # 初始化环境变量
    Ftest.init(env_file)
    dirname = dirname.decode("GB2312")
    dirname = dirname.encode("utf-8")
    # 获取目录信息数据
    data = Excel(Ftest.testexcel, Ftest.tablename).get_dir_tree(dirname.decode('utf-8'))
    if data is False:
        print "The table:" + dirname.decode('utf-8') + " not exist!"
        return None
    # 展示目录树
    show(data)
    return None


def show(data):
    """
    目录树展示函数

    :param data: 目录结构信息数据
    :return:
    """
    row = 0
    while row < len(data):
        space_length = 0
        line_length = 0
        col = 0
        while col < len(data[row]) - 2:
            if row == 0 :
                if col == 0:
                    pass
                else:
                    line_length = len(data[row][col-1])
                if col == len(data[row]) -3:
                    print "  " * (space_length / 2) + "|" + "-" * line_length + data[row][col] + ":" + data[row][col+1]
                else:
                    print "  " * (space_length/2) + "|" + "-" * line_length + data[row][col]
                if col == 0:
                    space_length = space_length + len(data[row][col])
                else:
                    space_length = space_length + len(data[row][col-1]) + len(data[row][col])
            else:
                if data[row][col] == data[row - 1][col]:
                    if col == 0:
                        space_length = space_length + len(data[row-1][col])
                    else:
                        space_length = space_length + len(data[row-1][col - 1]) + len(data[row-1][col])
                else:
                    if col == 0:
                        pass
                    else:
                        line_length = len(data[row][col - 1])
                    if col == len(data[row]) - 3:
                        print "  " * (space_length / 2) + "|" + "-" * line_length + data[row][col]+":" + data[row][col+1]
                    else:
                        print "  " * (space_length/2) + "|" + "-" * line_length + data[row][col]
                    if col == 0:
                        space_length = space_length + len(data[row][col])
                    else:
                        space_length = space_length + len(data[row][col - 1]) + len(data[row][col])
            col = col + 1
        row = row + 1


def usage():
    """
    Ftest 使用说明

    :return:
    """
    print "[Usage]:Ftest action option"
    print ""
    print 'Example:Ftest run -o "1,2,5" -e xxx.json --report xxxx.html'
    print "        Ftest info --tree -e xxx.json"
    print "        Ftest tool -g xxx.py -e xxx.json "
    print ""
    print 'action: run  "Choose the right way to run the test case"'
    print '        option:--only/-o  "Run only one test case,use case no!"'
    print '        option:--dir/-d   "Run the cases in the specified folder"'
    print '        option:--env/-e   "The environment variables,use json file"'
    print '        option:--report   "Select whether to generate a report"'
    print ""
    print 'action: info "Get information about the test case"'
    print '        option:--tree/-t  "Show test cases info of all test case"'
    print '        option:--dir/-d   "Show test cases info of specified folder"'
    print '        option:--env/-e   "The environment variables,use json file"'
    print ""
    print 'action: tool "Provide some handy tools such as generation cases file"'
    print '        option:--generate/-g "The file name of the cases file"'
    print '        option:--env/-e   "The environment variables,use json file"'


if __name__ == "__main__":
    """
    Entrance入口
    """
    # 提供的服务
    option = ["run", "info", "tool"]
    option_run = ["--only", "-o", "--dir", "-d", "--env", "-e", "--report"]
    option_info = ["--tree", "-t", "--dir", "-d", "--env", "-e"]
    option_tool = ["--generate", "-g", "--env", "-e"]
    argvs = sys.argv
    if len(argvs) < 2:
        print "Please use the right way."
        print ""
        usage()
        exit(0)

    if argvs[1] not in option:
        print "No the action:" + argvs[1]
        usage()
        exit(0)
    # "run"运行测试用例
    if argvs[1] == option[0]:
        if len(argvs) < 3:
            usage()
            exit(0)
        if argvs[2] not in option_run:
            usage()
            exit(0)
        if argvs[2] == "--only" or argvs[2] == "-o":
            if len(argvs) < 6:
                usage()
                exit(0)
            if argvs[4] == "--env" or argvs[4] == "-e":
                if len(argvs[5].split(".")) != 2:
                    print "Environment file is invalid!"
                    exit(0)
                if argvs[5].split(".")[1] != "json":
                    print "Environment file is invalid!"
                    exit(0)
                if len(argvs) == 8 and argvs[6] == "--report":
                    if len(argvs[7].split(".")) !=2:
                        print "Report file name is invalid!"
                        exit(0)
                    if argvs[7].split(".")[1] != "html":
                        print "Report file name is invalid!"
                        exit(0)
                    run_one_testcase(argvs[3], argvs[5], argvs[7])
                    exit(0)
                run_one_testcase(argvs[3], argvs[5])
                exit(0)
            else:
                usage()
                exit(0)
        if argvs[2] == "--dir" or argvs[2] == "-d":
            if len(argvs) < 6:
                usage()
                exit(0)
            if argvs[4] == "--env" or argvs[4] == "-e":
                if len(argvs[5].split(".")) != 2:
                    print "Environment file is invalid!"
                    exit(0)
                if argvs[5].split(".")[1] != "json":
                    print "Environment file is invalid!"
                    exit(0)
                if len(argvs) == 8 and argvs[6] == "--report":
                    if len(argvs[7].split(".")) != 2:
                        print "Report file name is invalid!"
                        exit(0)
                    if argvs[7].split(".")[1] != "html":
                        print "Report file name is invalid!"
                        exit(0)
                    run_dir_testcase(argvs[3], argvs[5], argvs[7])
                    exit(0)
                run_dir_testcase(argvs[3], argvs[5])
                exit(0)
            else:
                usage()
                exit(0)
    # "info"展示测试用例信息
    if argvs[1] == option[1]:
        if len(argvs) < 3:
            usage()
            exit(0)
        if argvs[2] not in option_info:
            usage()
            exit(0)
        if argvs[2] == "--tree" or argvs[2] == "-t":
            if len(argvs) != 5:
                usage()
                exit(0)
            if argvs[3] == "--env" or argvs[3] == "-e":
                if len(argvs[4].split(".")) != 2:
                    print "Environment file is invalid!"
                    exit(0)
                if argvs[4].split(".")[1] != "json":
                    print "Environment file is invalid!"
                    exit(0)
                show_all_testcase(argvs[4])
                exit(0)
            else:
                usage()
                exit(0)
        if argvs[2] == "--dir" or argvs[2] == "-d":
            if len(argvs) != 6:
                usage()
                exit()
            if argvs[4] == "-env" or argvs[4] == "-e":
                if len(argvs[5].split(".")) != 2:
                    print "Environment file is invalid!"
                    exit(0)
                if argvs[5].split(".")[1] != "json":
                    print "Environment file is invalid!"
                    exit(0)
                show_dir_testcase(argvs[3], argvs[5])
                exit(0)
            else:
                usage()
                exit(0)
    # "tool"提供的工具
    if argvs[1] == option[2]:
        if len(argvs) != 6:
            usage()
            exit(0)
        if argvs[2] == "--generate" or argvs[2] == "-g":
            if len(argvs[3].split(".")) != 2:
                print "Case file is invalid!"
                exit(0)
            if argvs[3].split(".")[1] != "py":
                print "Case file is invalid!"
                exit(0)
        else:
            usage()
            exit(0)
        if argvs[4] == "--env" or argvs[4] == "-e":
            if len(argvs[5].split(".")) != 2:
                print "Environment file is invalid!"
                exit(0)
            if argvs[5].split(".")[1] != "json":
                print "Environment file is invalid!"
                exit(0)
            get_case_file(argvs[3], argvs[5])
            exit(0)
        else:
            usage()
            exit(0)
