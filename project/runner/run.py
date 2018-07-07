#!/bin/python
#-*- coding: UTF-8 -*-

import platform
import traceback
import datetime
import time
from config.env import Ftest
from lib import Fassert
from lib.request import Record
from lib import request

ALL_ERROR = []
ALL_EXCEPT = []
#example：
#统计信息
#INFO_REPORT = {
#    "suite_name":"Ftest",
#    "suite_desc":"Ftest desc",
#    "start_time":"Wed Jun 20 2018 16:33:20 GMT+0800 (中国标准时间)",
#    "case_count":{
#        "total":12,
#        "fail":2
#    },
#    "assert_count":{
#        "total":24,
#        "fail":4
#    },
#    "run_time":5.3,#秒，s
#    "data_size":20.2,#KB
#    "avg_reponse_time":12#毫秒，ms
#}
#单个case的信息
#INFO_CASE = [
#    ["name","method","url","response_time","data_size","ststus_code",{"assert_name":1/0,"assert_name":1/0}],
#    ["name","method","url","response_time","data_size","ststus_code",{"assert_name":1/0,"assert_name":1/0}]
#]
INFO_REPORT = {}
INFO_CASE = []
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
        INFO_REPORT["suite_name"] = imp_module.project_name
        INFO_REPORT["suite_desc"] = imp_module.desc
        INFO_REPORT["start_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        INFO_REPORT["case_count"] = {"total":len(case_list)}
        INFO_REPORT["case_count"]["fail"] = 0
        INFO_REPORT["assert_count"] = {"total":0,"fail":0}
        INFO_REPORT["run_time"] = int(time.time())
        INFO_REPORT["data_size"] = 0.0
        INFO_REPORT["avg_response_time"] = 0.0
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
        INFO_REPORT["suite_name"] = imp_module.project_name
        INFO_REPORT["suite_desc"] = imp_module.desc
        INFO_REPORT["start_time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        INFO_REPORT["case_count"] = {"total": len(case_list)}
        INFO_REPORT["case_count"]["fail"] = 0
        INFO_REPORT["assert_count"] = {"total": 0, "fail": 0}
        INFO_REPORT["run_time"] = int(time.time())
        INFO_REPORT["data_size"] = 0.0
        INFO_REPORT["avg_response_time"] = 0.0
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
    case_data = []
    INFO_CASE.append(case_data)

    case_data.append(desc)
    case_data.append(Record.method)
    case_data.append(Record.url)
    case_data.append(Record.response_time)
    case_data.append(Record.data_size)
    case_data.append(Record.status_code)
    j = 0
    assert_info = {}
    while j < len(Fassert.Fassert_right_list):
        assert_info[Fassert.Fassert_right_list[j]] = 1
        j = j + 1
    j = 0
    while j < len(Fassert.Fassert_error_list):
        assert_info[Fassert_error_list[j]] = 0
        j = j + 1
    case_data.append(assert_info)

    request.clear()
    assert_count = 0
    while assert_count < len(Fassert.Fassert_right_list):
        Flog.right(Fassert.RIGHT_SIGN + Fassert.Fassert_right_list[assert_count])
        assert_count = assert_count + 1
    assert_count = 0
    if len(Fassert.Fassert_error_list) != 0:
        error = []
        ALL_ERROR.append(error)
        error.append(desc)
        while assert_count < len(Fassert.Fassert_error_list):
            error.append(Fassert.Fassert_error_list[assert_count])
            Flog.error(Fassert.ERROR_SIGN +  Fassert.Fassert_error_list[assert_count])
            assert_count = assert_count + 1
    print ""
    INFO_REPORT["assert_count"]["total"] = INFO_REPORT["assert_count"]["total"] + len(Fassert.Fassert_right_list) + len(Fassert.Fassert_error_list)
    INFO_REPORT["assert_count"]["fail"]  = INFO_REPORT["assert_count"]["fail"] + len(Fassert.Fassert_error_list)
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
    INFO_REPORT["case_count"]["fail"] = len(ALL_ERROR)
    i = 0
    error_name = []
    while i < len(ALL_ERROR):
        error_name.append(ALL_ERROR[i][0])
        i = i + 1
    i = 0
    while i < len(ALL_EXCEPT):
        if ALL_EXCEPT[i][0] not in error_name:
            INFO_REPORT["case_count"]["fail"] = INFO_REPORT["case_count"]["fail"] + 1
        i = i + 1

    INFO_REPORT["run_time"] = int(time.time()) - INFO_REPORT["run_time"]
    i = 0
    response_time = 0.0
    while i < len(INFO_CASE):
        INFO_REPORT["data_size"] = INFO_REPORT["data_size"] + INFO_CASE[i][4]
        response_time  = response_time + INFO_CASE[i][3]
        i = i + 1
    INFO_REPORT["avg_response_time"] = round(response_time / INFO_REPORT["case_count"]["total"],3)

#    print INFO_REPORT
    #print INFO_CASE
    return None

