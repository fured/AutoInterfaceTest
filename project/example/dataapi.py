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
if platform.system() == "Linux":
    from lib.linux_log import Flog
else:
    from lib.win_log import Flog

#Author:fured
#date:2018.06.30
#desc:interface test case

project_name = "Data Api"
Ftest.project_name = project_name

def print():


class UserLogin(unittest.TestCase):
    desc = "登录并获取token"

    def setUp(self):
        print "start test..."

    def test(self):
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({"userName": "sangfor", "rand": 755601452147616764, "domain": "test@sangfor.com", "clientVersion": "1.0.0", "clientProduct": "usability", "auth": "775518362020b951f7d2764ddd2b0650ffe0d818dbdf731e96aeb89a", "clientId": "100"})
        response = requests.post(Ftest.domainauth+Ftest.auth+"login",data=payload,headers=headers)
        print "POST " + Response.Url(response)
        self.response = response


    def tearDown(self):
        print "ResponseData:"+self.response.text
        self.assertEqual(self.response.status_code,200)
        responsedata = json.loads(self.response.text)
        Ftest.setGlobalVariable("data_token",responsedata["data"]["token"])
        print Ftest.data_token
        self.assertEquals(responsedata["code"],0)
        print "test ending!"

class UserData(unittest.TestCase):
    desc = "获取用户数据"

    def setUp(self):
        print "start test..."

    def test(self):
        payload = {"token":Ftest.data_token}
        r = requests.get(env.domain+env.dataapi+"user",params=payload)
        self.request = r

    def tearDown(self):
        print self.request.url
        print self.request.status_code
        print "test ending!"

class UserAsset(unittest.TestCase):
    desc = "获取用户资产"

    def setUp(self):
        print "start test"

    def test(self):
        payload = {"token":Ftest.data_token}
        r = requests.get(Ftest.domain+Ftest.dataapi+"asset",params=payload)
        print Response.Url(r)

    def tearDown(self):
        print "test ending!"