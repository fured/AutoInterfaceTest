#!/bin/python
#-*- coding: UTF-8 -*-

import platform
import traceback
from config.env import Ftest
from lib import Fassert

ALL_ERROR = []
ALL_EXCEPT = []

window_dir_sign = ">"

if platform.system() == "Linux":
    from lib.linux_log import Flog
else:
    from lib.win_log import Flog

class Run(object):
    def __init__(self):
        pass

    def run_one_case(self,case_list):
        imp_module = __import__(Ftest.case)
        name = 'Project: ' + imp_module.project_name
        Flog.nameout(name)
        print ""
        row = 0
        while row < len(case_list):
            try:
                desc = "-> " + case_list[row][0]+case_list[row][1]
                Flog.nameout(desc)
                class_name = getattr(imp_module, case_list[row][2])
                run(class_name,case_list[row][0]+case_list[row][1])
            except Exception, error:
                exce = []
                ALL_EXCEPT.append(exce)
                exce.append(case_list[row][0]+case_list[row][1])
                #Flog.error(str(error))
                exce.append(str(error))
                Flog.error(traceback.format_exc())
                row = row + 1
                continue
            row = row + 1
        end()
        return None

    def run_dir_case(self,case_list):
        imp_module = __import__(Ftest.case)
        name = "Project: " + imp_module.project_name
        Flog.nameout(name)
        row = 0
        while row < len(case_list):
            space_len = 0
            space_length = 0
            col = 0
            while col < len(case_list[row]) - 2:
                if row == 0:
                    if col == 0:
                        pass
                    if col == len(case_list[row]) - 3:
                        Flog.nameout(" " * space_len + "-> " + case_list[row][col] + ":" + case_list[row][col + 1])
                        try:
                            class_name = getattr(imp_module,case_list[row][len(case_list[row]) - 1])
                            run(class_name,case_list[row][len(case_list[row]) - 3] + case_list[row][len(case_list[row]) - 2])
                        except Exception,error:
                            exce = []
                            ALL_EXCEPT.append(exce)
                            exce.append(case_list[row][len(case_list[row]) - 3] + case_list[row][len(case_list[row]) - 2])
                            exce.append(str(error))
                            Flog.error(traceback.format_exc())
                    else:
                        print ""
                        Flog.nameout(" " * space_len +window_dir_sign  + case_list[row][col])
                    if col == 0:
                        space_length = space_length + len(case_list[row][col])
                    else:
                        space_length = space_length + len(case_list[row][col - 1]) + len(case_list[row][col])
                else:
                    if case_list[row][col] == case_list[row - 1][col]:
                        if col == 0:
                            space_length = space_length + len(case_list[row - 1][col])
                        else:
                            space_length = space_length + len(case_list[row - 1][col - 1]) + len(case_list[row - 1][col])
                    else:
                        if col == 0:
                            pass
                        if col == len(case_list[row]) - 3:
                            Flog.nameout(" " * space_len  + "-> " + case_list[row][col] + ":" + case_list[row][col + 1])
                            try:
                                class_name = getattr(imp_module, case_list[row][len(case_list[row]) - 1])
                                run(class_name,
                                    case_list[row][len(case_list[row]) - 3] + case_list[row][len(case_list[row]) - 2])
                            except Exception, error:
                                exce = []
                                ALL_EXCEPT.append(exce)
                                exce.append(case_list[row][len(case_list[row]) - 3] + case_list[row][len(case_list[row]) - 2])
                                exce.append(str(error))
                                Flog.error(traceback.format_exc())
                        else:
                            print ""
                            Flog.nameout(" " * space_len + window_dir_sign + case_list[row][col])
                        if col == 0:
                            space_length = space_length + len(case_list[row][col])
                        else:
                            space_length = space_length + len(case_list[row][col - 1]) + len(case_list[row][col])
                col = col + 1
                space_len = space_len + 1
            row = row + 1
        end()
        return None

def run(class_name,desc):
    case = class_name()
    #desc = "-> " + case_list[0]+case_list[1]
    #Flog.nameout(desc)
    print ""
    case.setUp()
    print ""
    case.test()
    print ""
    case.tearDown()
    print ""
    assert_count = 0
    while assert_count < len(Fassert.Fassert_right_list):
        Flog.right(Fassert.Fassert_right_list[assert_count])
        assert_count = assert_count + 1
    assert_count = 0
    if len(Fassert.Fassert_error_list) != 0:
        error = []
        ALL_ERROR.append(error)
        error.append(desc)
        while assert_count < len(Fassert.Fassert_error_list):
            error.append(Fassert.Fassert_error_list[assert_count])
            Flog.error(Fassert.Fassert_error_list[assert_count])
            assert_count = assert_count + 1
    print ""
    Fassert.Fassert_right_list = []
    Fassert.Fassert_error_list = []

def end():
    print "END" + "-"* 100
    print ""
    Flog.error("#Failure" + " "*45 + "#detial")
    print ""
    i = 0
    while i < len(ALL_ERROR):
        j = 1
        Flog.errornotline(ALL_ERROR[i][0])
        while j < len(ALL_ERROR[i]):
            Flog.error(" "*48 + ALL_ERROR[i][j])
            j = j + 1
        i = i + 1
    i = 0
    while i < len(ALL_EXCEPT):
        j = 1
        Flog.errornotline(ALL_EXCEPT[i][0])
        while j < len(ALL_EXCEPT[i]):
            Flog.error(" "*(48-len(ALL_EXCEPT[i][0])*2) + ALL_EXCEPT[i][j])
            j = j + 1
        print ""
        i = i + 1
    return None

