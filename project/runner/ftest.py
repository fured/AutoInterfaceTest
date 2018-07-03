#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import sys,json
import chardet
sys.path.append('..')
#import testcase.dataapi
from config.env import Ftest
from lib.excel import Excel
from tools.template import Template

#Auther:fured
#date:2018.07.01
#desc:enter

def get_case_file(filename):
    if len(filename.split(".")) != 2 or filename.split(".")[1] != "py":
        print "Filename is invalid!"
        print "Please refer to the follow..."
        usage()
        exit(0)
    template = Template(Ftest.testexcel,Ftest.tablename)
    template.generate_file(filename)


def run_one_testcase(case_no,env_file):
    # 初始化环境
    Ftest.init(env_file)
    case_list = case_no.split(",")
    class_name_list = []
    i = 0
    while i < len(case_list):
        class_name = Excel(Ftest.testexcel,Ftest.tablename).get_case(case_list[i])
        class_name_list.append(class_name)
        i = i + 1
    #print class_name
    #print sys.path
    #动态添加testcase类
    sys.path.append("../testcase")
    imp_module = __import__(Ftest.case)
    suite_list = []
    for class_name in class_name_list:
        case_class = getattr(imp_module, class_name)
        suite = unittest.TestLoader().loadTestsFromTestCase(case_class)
        suite_list.append(suite)
    suite = unittest.TestSuite(suite_list)
    unittest.TextTestRunner(verbosity=2).run(suite)


def run_dir_testcase(dir_name,env_file):
    #初始化环境
    Ftest.init(env_file)
    dir_name = dir_name.decode("GB2312")
    dir_name = dir_name.encode("utf-8")
    class_list = Excel(Ftest.testexcel,Ftest.tablename).get_cases(dir_name.decode('utf-8'))
    #动态添加testcase类
    sys.path.append("../testcase")
    imp_module = __import__(Ftest.case)
    suite_list = []
    for case_name in class_list:
        case_class = getattr(imp_module,case_name)
        suite = unittest.TestLoader().loadTestsFromTestCase(case_class)
        suite_list.append(suite)
    suite = unittest.TestSuite(suite_list)
    unittest.TextTestRunner(verbosity=2).run(suite)


#suite=unittest.TestSuite()
#suite.addTest(one.UserLogin("test"))
#suite.addTest(one.UserData('test'))
#suite.addTest(one.UserAsset("test"))

#unittest.TextTestRunner(verbosity=2).run(suite)

#suite=unittest.TestLoader().loadTestsFromTestCase()
#unittest.TextTestRunner(verbosity=2).run(suite)



#展示所有的结构信息
def show_all_testcase(env_file):
    Ftest.init(env_file)
    data = Excel(Ftest.testexcel,Ftest.tablename).get_all_tree()
    #for i in data:
    #    print i
    show(data)

#展示指定目录的结构信息
def show_dir_testcase(dirname,env_file):
    Ftest.init(env_file)
    dirname = dirname.decode("GB2312")
    dirname = dirname.encode("utf-8")
    #print chardet.detect(dirname)
    #dirname = "用户数据"
    #print chardet.detect(dirname)
    #data = Excel("DataApi.xlsx","test").get_dir_tree(u"用户数据")
    data = Excel(Ftest.testexcel, Ftest.tablename).get_dir_tree(dirname.decode('utf-8'))
    if data == False:
        print "The table:"+dirname.decode('utf-8')+" not exist!"
        return None
    #for i in data:
    #    print i
    show(data)

#展示
def show(data):
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
    print "[Usage]:python dataapi.py action option"
    print ""
    print "Example:python dataapi.py run -o xxxxxx"
    print "        python dataapi.py info --tree"
    print ""
    print 'action: run  "Choose the right way to run the test case"'
    print '        option:--only/-o  "Run only one test case,use case no!"'
    print '        option:--dir/-d   "Run the cases in the specified folder"'
    print '        option:--env/-e   "The environment variables,use json file"'
    print ""
    print 'action: info "Get information about the test case"'
    print '        option:--tree/-t  "Show test cases info of all test case"'
    print '        option:--dir/-d   "Show test cases info of specified folder"'


if __name__ == "__main__":
    option = ["run","info","tool"]
    option_run = ["--only","-o","--dir","-d","--env","-e"]
    option_info = ["--tree","-t","--dir","-d","--env","-e"]
    option_tool = ["--generate","-g"]
    argvs = sys.argv

    if len(argvs) < 2:
        usage()
        exit(0)

    if argvs[1] not in option:
        usage()
        exit(0)

    if argvs[1] == option[0]:
        if len(argvs) < 3:
            usage()
            exit(0)
        if argvs[2] not in option_run:
            usage()
            exit(0)
        if argvs[2] == "--only" or argvs[2] == "-o":
            if len(argvs) != 6:
                usage()
                exit(0)
            if argvs[4] == "--env" or argvs[4] == "-e":
                if argvs[5].split(".")[1] != "json":
                    print "Enviorment file is invliad!"
                    exit(0)
                run_one_testcase(argvs[3],argvs[5])
                exit(0)
            else:
                usage()
                exit(0)
        if argvs[2] == "--dir" or argvs[2] == "-d":
            if len(argvs) != 6:
                usage()
                exit(0)
            if argvs[4] == "--env" or argvs[4] == "-e":
                if len(argvs[5].split(".")) != 2:
                    print "Enviorment file is invliad!"
                    exit(0)
                if argvs[5].split(".")[1] != "json":
                    print "Enviorment file is invliad!"
                    exit(0)
                run_dir_testcase(argvs[3],argvs[5])
                exit(0)
            else:
                usage()
                exit(0)
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
                    print "Enviorment file is invliad!"
                    exit(0)
                if argvs[4].split(".")[1] != "json":
                    print "Enviorment file is invliad!"
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
                    print "Enviorment file is invliad!"
                    exit(0)
                if argvs[5].split(".")[1] != "json":
                    print "Enviorment file is invliad!"
                    exit(0)
                show_dir_testcase(argvs[3],argvs[5])
                exit(0)
            else:
                usage()
                exit(0)
    if argvs[1] == option[2]:
        if len(argvs) < 3:
            usage()
            exit(0)
        if argvs[2] not in option_tool:
            usage()
            exit(0)
        if argvs[2] not in option_tool:
            usage()
            exit(0)
        if argvs[2] == "--generate" or argvs[2] == "-g":
            if len(argvs) != 4:
                usage()
                exit(0)
            get_case_file(argvs[3])
            exit(0)