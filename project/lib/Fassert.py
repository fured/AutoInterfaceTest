#!/bin/python
#-*- coding: UTF-8 -*-

import platform
if platform.system() == "Linux":
    from lib.linux_log import Flog
else:
    from lib.win_log import Flog

#Author:fured
#date:2018-07-03
#desc:Output setting for windows operating

ERROR_SIGN = "Error "
RIGHT_SIGN = "OK "
Fassert_error_list = []
Fassert_right_list = []

#a == b
def equal(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(ERROR_SIGN+message)
        #Flog.error(ERROR_SIGN+message)
        return None
    if compare_a != compare_b:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    else:
        Fassert_right_list.append(RIGHT_SIGN+message)
        #Flog.right(RIGHT_SIGN+message)
    return None

#a != b
def unequal(message,compare_a,compare_b):
    if compare_a != compare_b:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

#a > b
def greater(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
        return None
    if compare_a > compare_b:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

#a < b
def less(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
        return None
    if compare_a < compare_b:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

#a <= b
def lessequal(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
        return None
    if compare_a <= compare_b:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

#a >= b
def greaterequal(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
        return None
    if compare_a >= compare_b:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

#a is True
def true(message,compare_a):
    if compare_a is True:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

#a is False
def false(message,compare_a):
    if compare_a is False:
        Fassert_right_list.append(RIGHT_SIGN + message)
        #Flog.right(RIGHT_SIGN+message)
    else:
        Fassert_error_list.append(ERROR_SIGN + message)
        #Flog.error(ERROR_SIGN+message)
    return None

