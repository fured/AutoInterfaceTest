#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import sys
sys.path.append('..')
import testcase.dataapi as one
from lib.excel import Excel




#suite=unittest.TestSuite()
#suite.addTest(one.UserLogin("test"))
#suite.addTest(one.UserData('test'))
#suite.addTest(one.UserAsset("test"))

#unittest.TextTestRunner(verbosity=2).run(suite)

#suite=unittest.TestLoader().loadTestsFromTestCase()
#unittest.TextTestRunner(verbosity=2).run(suite)

#得到案例目录结构信息
def get_testcase_structure():
    excel = Excel("DataApi.xlsx","test")
    info = excel.get_all_info()
    print info

#展示所有的结构信息
def show_all_testcase():
    structure = get_testcase_structure()

def usage():
    print "[Usage]:python dataapi.py action option"
    print ""
    print "Example:python dataapi.py run -o xxxxxx"
    print "        python dataapi.py info --tree"
    print ""
    print 'action: run  "Choose the right way to run the test case"'
    print '        option:--only/-o  "Run only one test case"'
    print '        option:--dir/-d   "Run the cases in the specified folder"'
    print ""
    print 'action: info "Get information about the test case"'
    print '        option:--tree/-t  "Show test cases info of all test case"'
    print '        option:--dir/-d   "Show test cases info of specified folder"'


if __name__ == "__main__":
    option = ["run","info"]
    option_run = ["--only","-o","--dir","-d"]
    option_info = ["--tree","-t","--dir","-d"]
    argvs = sys.argv

    if len(argvs) < 2:
        usage()
        exit(0)

    if argvs[1] not in option:
        usage()
        exit(0)

    if argvs[1] == option[0]:
        exit(0)

    if argvs[1] == option[1]:
        if argvs[2] == "--tree" or argvs[2] == "-t":
            show_all_testcase()
            exit(0)
        if argvs[2] == "--dir" or argvs[2] == "-d":
            show_dir_testcase()
            exit(0)
