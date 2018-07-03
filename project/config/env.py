#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

#Author:fured
#date:2018-6-30
#desc:Set the environment variables required for the interface test


class Ftest(object):
    #domain = "http://192.200.41.231:8000"
    #dataapi = "/data/api/cloudeye/v1/"
    #domainauth = "http://192.200.41.231:5000"
    #auth = "/authority/api/cloudeye/v1/"
    #test 目录文件及表明
    #testexcel = "DataApi.xlsx"
    #tablename = "test"
    #test case 文件名
    #case = "dataapi"


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

    def getEnvironmentVariable(self,key):
        if self.env_json.has_key(key):
            return self.env_json[key]
        else:
            return False

    def setEnvironmentVariable(self,env_file):
        pass

    @staticmethod
    def setGlobalVariable(key,vaule):
        setattr(Ftest,key,vaule)

    @staticmethod
    def getGlobalVariable(key):
        return Ftest.key

