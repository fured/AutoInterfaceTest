#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

"""
Author:fured
date:2018-6-30
desc:Set the environment variables required for the interface test
"""


class Ftest(object):
    """
    处理环境变量和全局变量
    环境变量中必须有的字段：testexcel = "DataApi.xlsx"
                            tablename = "test"
                            case = "dataapi"
    """
    def __init__(self, env_file):
        """
        初始化环境变量

        :param env_file: 环境变量文件路径，json文件
        """
        with open(env_file, "r") as fp:
            env_json = json.load(fp)
        for key, value in env_json.items():
            setattr(Ftest, key, value)
        self.env = env_json

    @staticmethod
    def init(env_file):
        with open(env_file, "r") as fp:
            env_json = json.load(fp)
        for key,value in env_json.items():
            setattr(Ftest, key, value)

    def getEnvironmentVariable(self, key):
        """
        获取环境变量

        :param key: 需要获取的环境变量的键值
        :return:
        """
        if self.env_json.has_key(key):
            return self.env_json[key]
        else:
            return False

    def setEnvironmentVariable(self, env_file):
        pass

    @staticmethod
    def setGlobalVariable(key, value):
        """
        设置全局变量

        :param key: 需要设置的全局变量的键值
        :param value: 需要设置的全局变量的值
        :return:
        """
        setattr(Ftest, key, value)

    @staticmethod
    def getGlobalVariable(key):
        """
        获取全局变量

        :param key: 需要获取的全局变量的键值
        :return:
        """
        return Ftest.key

