#!/bin/python
#-*- coding: UTF-8 -*-


#Author:fured
#date:2018-07-03
#desc:Assert setting

#断言失败的标记
ERROR_SIGN = "Error "
#断言成功的标记
RIGHT_SIGN = "OK "
#所有失败的断言列表
Fassert_error_list = []
#所有成功的断言列表
Fassert_right_list = []


#desc:判断两个数是否相等，a == b
def equal(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a != compare_b:
        Fassert_error_list.append(message)
    else:
        Fassert_right_list.append(message)
    return None

#desc:判断两个数是否不相等，a != b
def unequal(message,compare_a,compare_b):
    if compare_a != compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None

#desc:判断a是否大于b，a > b
def greater(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a > compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None

#desc:判断a是否小于b，a < b
def less(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a < compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None

#desc:判断a是否小于或等于b，a <= b
def lessequal(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a <= compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None

#desc:判断a是否大于或等于b，a >= b
def greaterequal(message,compare_a,compare_b):
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a >= compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None

#desc:判断a is True
def true(message,compare_a):
    if compare_a is True:
        Fassert_right_list.append( message)
    else:
        Fassert_error_list.append( message)
    return None

#desc:判断a is False
def false(message,compare_a):
    if compare_a is False:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None

