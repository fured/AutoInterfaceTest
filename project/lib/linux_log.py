#!/bin/python
# -*- coding: UTF-8 -*-

"""
Author:fured
date:2018-07-03
desc:Output setting for Linux operating
"""

# 亮白色
FOREGROUND_BringWhite = '\033[1;37m'
# 绿色
FOREGROUND_GREEN = '\033[0;32m'
# 红色
FOREGROUND_RED = '\033[0;31m'
# 青色
FOREGROUND_BLUE = '\033[0;36m'
# 结束符
END = '033[0m'
# usage:颜色代码+输出文字+结束符


class Flog(object):
    def __init__(self):
        pass

    @classmethod
    def output(cls, content):
        print '    %s%s%s' % (FOREGROUND_BLUE, content, END)
        return None

    @classmethod
    def error(cls, content):
        print '    %s%s%s' % (FOREGROUND_RED,content,END)
        return None

    @classmethod
    def errornotline(cls, content):
        print ('    %s%s%s' % (FOREGROUND_RED, content, END)),
        return None

    @classmethod
    def right(cls, content):
        print '    %s%s%s' % (FOREGROUND_GREEN, content, END)
        return None

    @classmethod
    def nameout(cls, content):
        print '%s%s%s' % (FOREGROUND_BringWhite, content, END)
        return None

