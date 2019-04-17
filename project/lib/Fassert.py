#!/bin/python
# -*- coding: UTF-8 -*-

"""
Author:fured
Date:2018-07-03
Desc:Assert setting
"""

# 断言失败的标记
ERROR_SIGN = "Error "
# 断言成功的标记
RIGHT_SIGN = "OK "
# 所有失败的断言列表
Fassert_error_list = []
# 所有成功的断言列表
Fassert_right_list = []


def equal(message, compare_a, compare_b):
    """
    判断两个数是否相等

    :param message:
    :param compare_a:
    :param compare_b:
    :return:
    """
    if compare_a != compare_b:
        Fassert_error_list.append(message)
    else:
        Fassert_right_list.append(message)
    return None


def unequal(message, compare_a, compare_b):
    """
    判断两个数是否不相等，a != b

    :param message:
    :param compare_a:
    :param compare_b:
    :return:
    """
    if compare_a != compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None


def greater(message, compare_a, compare_b):
    """
    判断a是否大于b，a > b

    :param message:
    :param compare_a:
    :param compare_b:
    :return:
    """
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a > compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None


def less(message, compare_a, compare_b):
    """
    判断a是否小于b

    :param message:
    :param compare_a:
    :param compare_b:
    :return:
    """
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a < compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None


def lessequal(message, compare_a, compare_b):
    """
    判断a是否小于或等于b，a <= b

    :param message:
    :param compare_a:
    :param compare_b:
    :return:
    """
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a <= compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None


def greaterequal(message, compare_a, compare_b):
    """
    判断a是否大于或等于b，a >= b

    :param message:
    :param compare_a:
    :param compare_b:
    :return:
    """
    if type(compare_a) != type(compare_b):
        Fassert_error_list.append(message)
        return None
    if compare_a >= compare_b:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None


def true(message, compare_a):
    """
    判断 a 为True
    :param message:
    :param compare_a:
    :return:
    """
    if compare_a is True:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None


def false(message, compare_a):
    """
    判断 a 为False
    :param message:
    :param compare_a:
    :return:
    """
    if compare_a is False:
        Fassert_right_list.append(message)
    else:
        Fassert_error_list.append(message)
    return None
