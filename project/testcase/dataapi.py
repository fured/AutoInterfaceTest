#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import requests
import unittest
import platform

sys.path.append('..')
from config.env import DataApi as env
from config.glovarl import DataApi as glovarl

if platform.system() == "Linux":
    import output_style as output
else:
    import common_style as output

#Author:fured
#date:2018.06.30
#desc:interface test case

project_name = "Data Api"
glovarl.project_name = project_name

class UserLogin(unittest.TestCase):
    desc = "登录并获取token"

    def setUp(self):
        print "start test..."

    def test(self):
        headers = {"Content-Type": "application/json"}
        payload = json.dumps({"userName": "sangfor", "rand": 755601452147616764, "domain": "test@sangfor.com", "clientVersion": "1.0.0", "clientProduct": "usability", "auth": "775518362020b951f7d2764ddd2b0650ffe0d818dbdf731e96aeb89a", "clientId": "100"})
        r = requests.post(env.domainauth+env.auth+"login",data=payload,headers=headers)
        self.request = r

    def tearDown(self):
        print "ResponseData:"+self.request.text
        self.assertEqual(self.request.status_code,200)
        responsedata = json.loads(self.request.text)
        glovarl.data_token = responsedata["data"]["token"]
        self.assertEquals(responsedata["code"],0)
        print "test ending!"

class UserData(unittest.TestCase):
    desc = "获取用户数据"

    def setUp(self):
        print "start test..."

    def test(self):
        payload = {"token":glovarl.data_token}
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
        payload = {"token":glovarl.data_token}
        r = requests.get(env.domain+env.dataapi+"asset",params=payload)
        print "request:"+r.url

    def tearDown(self):
        print "test ending!"