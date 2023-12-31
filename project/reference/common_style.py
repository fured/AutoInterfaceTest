#!/usr/bin/env python
# encoding: utf-8
import ctypes

# desc：windows命令行界面，有颜色输出

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 黑色
FOREGROUND_BLACK = 0x0
# 蓝色
FOREGROUND_BLUE = 0x01  # text color contains blue.
# 绿色
FOREGROUND_GREEN = 0x02  # text color contains green.
# 浅绿色
FOREGROUND_RESEDA = 0x03
# 红色
FOREGROUND_RED = 0x04  # text color contains red.
# 紫色
FOREGROUND_PURPLE = 0x05
# 黄色
FOREGROUND_YELLOW = 0X06
# 白色
FOREGROUND_white = 0x07
# 增强
FOREGROUND_INTENSITY = 0x08  # text color is intensified.
# 淡蓝色
FOREGROUND_WATHETBLUE = 0x09
# 淡绿色
FOREGROUND_WATHEGREEN = 0x0A
# 淡浅绿色
FOREGROUND_WATHERESEDA = 0x0B
# 淡红色
FOREGROUND_WATHERED = 0x0B
# 淡紫色
FOREGROUND_WATHEPURPLE = 0x0C
# 淡黄色
FOREGROUND_WATHEYELLOW = 0x0D
# 亮白色
FOREGROUND_BringWhite = 0x0F

# 背景色即10，11，12 ... 1F
BACKGROUND_BLUE = 0x10  # background color contains blue.
BACKGROUND_GREEN = 0x20  # background color contains green.
BACKGROUND_RED = 0x40  # background color contains red.
BACKGROUND_INTENSITY = 0x80  # background color is intensified.


class Color(object):
    """
    See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp
    for information on Windows APIs.
    """
    # 获取标准输出句柄
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def set_cmd_color(self, color, handle=std_out_handle):
        """(color) -> bit
        Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        """
        bool_ = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool_

    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print print_text
        self.reset_color()

    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print print_text
        self.reset_color()

    def print_white(self, print_text):
        self.set_cmd_color(FOREGROUND_BringWhite)
        print print_text
        self.reset_color()

    def print_white_(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_BLUE)
        print print_text
        self.reset_color()

    def print_blue_text(self, print_text):
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        print print_text
        self.reset_color()

    def print_red_text_with_blue_bg(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY | BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print print_text
        self.reset_color()


if __name__ == "__main__":
    clr = Color()
    clr.print_white("test")
    clr.print_white_("test")
    clr.print_red_text('red')
    clr.print_green_text('green')
    clr.print_blue_text('blue')
    clr.print_red_text_with_blue_bg('background')
