#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import requests
import unittest
import platform

sys.path.append('..')
from config.env import Ftest
from lib.request import Response
from lib.request import Request
from lib import Fassert
if platform.system() == "Linux":
    from lib.linux_log import Flog
else:
    from lib.win_log import Flog

#Author:fured
#date:2018.06.30
#desc:interface test case

project_name = "Data Api Test"
desc = "The api provide data query function for users."

class UserLogin(object):
    desc = "登录并获取token"

    def setUp(self):
        Flog.output("start test...")

    def test(self):
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({"userName": "sangfor", "rand": 755601452147616764, "domain": "test@sangfor.com", "clientVersion": "1.0.0", "clientProduct": "usability", "auth": "775518362020b951f7d2764ddd2b0650ffe0d818dbdf731e96aeb89a", "clientId": "100"})
        Request.method = "post"
        Request.headers = headers
        Request.params = payload
        Request.url = Ftest.domainauth+Ftest.auth+"login"
        Request.send()
        Flog.output("POST " + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200",Response.Code(Request.response),200)
        responsedata = json.loads(Response.Body(Request.response))
        Ftest.setGlobalVariable("data_token",responsedata["data"]["token"])
        Fassert.equal("[INFO]back code is right!",responsedata["code"],0)
        Flog.output("test ending!")

class UserData(object):
    desc = "获取用户数据"

    def setUp(self):
        Flog.output("start test...")

    def test(self):
        payload = {"token":Ftest.data_token}
        Request.method = "get"
        Request.params = payload
        Request.url = Ftest.domain+Ftest.dataapi+"user"
        Request.send()
        Flog.output("GET " + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200", Response.Code(Request.response), 200)
        Flog.output("test ending!")

class UserDataTokenWrong(object):
    desc = "token错误获取用户数据"

    def setUp(self):
        Flog.output("start test...")

    def test(self):
        payload = {"token":"gqwedgcasiudgcu1237hwdesucui"}
        Request.method = "get"
        Request.params = payload
        Request.url = Ftest.domain+Ftest.dataapi+"user"
        Request.send()
        Flog.output("GET" + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200", Response.Code(Request.response), 200)
        data = json.loads(Response.Body(Request.response))
        Fassert.equal("[INFO]back code is right", data["code"],1101)
        Flog.output("test ending!")

class UserDataNoPam(object):
    desc = "无参数获取用户数据"

    def setUp(self):
        Flog.output("start test...")

    def test(self):
        Request.method = "get"
        Request.url = Ftest.domain+Ftest.dataapi+"user"
        Request.send()
        Flog.output("GET" + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200", Response.Code(Request.response), 200)
        data = json.loads(Response.Body(Request.response))
        Fassert.equal("[INFO]back code is right", data["code"],1100)
        Flog.output("test ending!")

class UserAsset(object):
    desc = "获取用户资产"

    def setUp(self):
        Flog.output("start test")

    def test(self):
        payload = {"token":Ftest.data_token}
        Request.method = "get"
        Request.url = Ftest.domain+Ftest.dataapi+"asset"
        Request.params = payload
        Request.send()
        Flog.output("GET" + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200", Response.Code(Request.response), 200)
        Flog.output("test ending!")

class UserAssetTokenWrong(object):
    desc = "token错误获取用户资产"

    def setUp(self):
        Flog.output("start test...")

    def test(self):
        payload = {"token":"gqwedgcasiudgcu1237hwdesucui"}
        Request.method = "get"
        Request.params = payload
        Request.url = Ftest.domain+Ftest.dataapi+"asset"
        Request.send()
        Flog.output("GET" + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200", Response.Code(Request.response), 200)
        data = json.loads(Response.Body(Request.response))
        Fassert.equal("[INFO]back code is right", data["code"],1101)
        Flog.output("test ending!")

class UserAssetNoPam(object):
    desc = "无参数获取用户资产"

    def setUp(self):
        Flog.output("start test...")

    def test(self):
        Request.method = "get"
        Request.url = Ftest.domain+Ftest.dataapi+"asset"
        Request.send()
        Flog.output("GET" + Response.Url(Request.response))

    def tearDown(self):
        Fassert.equal("[INFO]status code is 200", Response.Code(Request.response), 200)
        data = json.loads(Response.Body(Request.response))
        Fassert.equal("[INFO]back code is right", data["code"],1100)
        Flog.output("test ending!")