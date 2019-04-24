#!/bin/python
# -*- coding: UTF-8 -*-

import ctypes
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
Author:fured
date:2018-07-03
desc:Output setting for windows operating
"""

STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 亮白色
FOREGROUND_BringWhite = 0x0F
# 绿色
FOREGROUND_GREEN = 0x02
# 红色
FOREGROUND_RED = 0x04
# 蓝色
FOREGROUND_BLUE = 0x01
# 增强
FOREGROUND_INTENSITY = 0x08


class Flog(object):
    # 获取标准输出句柄
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    # 获取标准错误输出句柄
    std_error_heandle = ctypes.windll.kernel32.GetStdHandle(STD_ERROR_HANDLE)

    def __init__(self):
        pass

    @classmethod
    def output(cls, content):
        Flog.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_BLUE)
        print "    ".decode() + str(content)
        Flog.reset_color()

    @classmethod
    def dir(cls, content):
        Flog.set_cmd_color(FOREGROUND_BLUE)
        print content
        Flog.reset_color()

    @classmethod
    def error(cls, content):
        Flog.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print "    " + content
        Flog.reset_color()

    @classmethod
    def errornotline(cls, content):
        Flog.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print ("    " + content),
        Flog.reset_color()

    @classmethod
    def right(cls, content):
        Flog.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print "    " + content
        Flog.reset_color()

    @classmethod
    def nameout(cls, content):
        Flog.set_cmd_color(FOREGROUND_BringWhite)
        print content
        Flog.reset_color()

    @classmethod
    def set_cmd_color(cls,color, handle=std_out_handle):
        """
        设置颜色
        :param color:
        :param handle:
        :return:
        """
        bool_ = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool_

    @classmethod
    def reset_color(cls):
        """
        恢复默认设置
        :return:
        """
        Flog.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


if __name__ == "__main__":
    Flog.nameout("AAA")
    Flog.right("AAA")
    Flog.output("AAA")
