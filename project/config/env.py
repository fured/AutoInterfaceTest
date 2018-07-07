#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

#Author:fured
#date:2018-6-30
#desc:Set the environment variables required for the interface test


#处理环境变量和全局变量
class Ftest(object):
#环境变量中必须有的字段：testexcel = "DataApi.xlsx"
#                   tablename = "test"
#                   case = "dataapi"

    #desc:初始化环境变量
    #parameter：env_file:环境变量文件，json文件（必选）
    def __init__(self,env_file):
        with open(env_file, "r") as fp:
            env_json = json.load(fp)
        for key,value in env_json.items():
            setattr(Ftest,key,value)
        self.env = env_json

    @staticmethod
    def init(env_file):
        with open(env_file, "r") as fp:
            env_json = json.load(fp)
        for key,value in env_json.items():
            setattr(Ftest,key,value)

    #desc:获取环境变量
    #parameter:key:需要获取的环境变量的键值
    def getEnvironmentVariable(self,key):
        if self.env_json.has_key(key):
            return self.env_json[key]
        else:
            return False

    def setEnvironmentVariable(self,env_file):
        pass

    #desc:设置全局变量
    #parameter：key：需要设置的全局变量的键值
    #           vaule：需要设置的全局变量的值
    @staticmethod
    def setGlobalVariable(key,vaule):
        setattr(Ftest,key,vaule)

    #desc：获取全局变量
    #parameter：key:需要获取的全局变量的键值
    @staticmethod
    def getGlobalVariable(key):
        return Ftest.key

