#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

#Auther:fured
#date:2018.07.02
#desc:Packaging requests


#desc:记录每个请求的数据，为了生成报告
class Record(object):
    method = ""
    url = ""
    response_time = 0.0
    data_size = 0.0
    status_code = ""
    pass

#desc：进行每个请求的数据记录
def record():
    Record.method = Request.method
    Record.url = Request.url
    Record.response_time = Response.ResponseTime(Request.response)
    Record.data_size = Response.DataSize(Request.response)
    Record.status_code = Response.Code(Request.response)

#desc：一个测试用例结束后，清楚这些记录
def clear():
    Record.method = ""
    Record.url = ""
    Record.response_time = 0.0
    Record.data_size = 0.0
    Record.status_code = ""
    Request.method = None
    Request.url = None
    Request.params = None
    Request.headers = None
    Request.response = None
    Request.files = None

#desc：获取请求回复的一些信息
class Response(object):

    def __init__(self):
        pass

    #获取返回的状态码
    @staticmethod
    def Code(response):
        return response.status_code

    #获取返回的数据实体
    @staticmethod
    def Body(response):
        return response.text

    #获取返回头部中的content
    @staticmethod
    def Content(response):
        return response.content

    #获取发送的url
    @staticmethod
    def Url(response):
        return response.url

    #获取返回响应的时间，单位：毫秒（ms）
    @staticmethod
    def ResponseTime(response):
        return  response.elapsed.total_seconds() * 1000

    #获取返回数据的大小，单位：字节（Byte）
    @staticmethod
    def DataSize(response):
        if dict(response.headers).has_key("Content-Length"):
            return float(response.headers["Content-Length"])
        else:
            return 0

#desc：封装http请求
class Request(object):
    #目前只支持“get”和“post”方法
    support_method = ["get","post"]
    method = None
    params = None
    headers = None
    url = None
    response = None
    files = None
    def __init__(self):
        pass

    #desc：发送http请求
    @staticmethod
    def send():
        if Request.method == None or Request.url == None:
            raise Exception("Request is error!")
            return None
        if Request.method not in Request.support_method:
            raise Exception("Not support "+Request.method+" method!")
            return None
        if Request.method == "get":
            if Request.params != None:
                if Request.headers != None:
                    Request.response = requests.get(Request.url,params=Request.params,headers=Request.headers)
                    record()
                    return Request.response

                else:
                    Request.response = requests.get(Request.url, params=Request.params, headers=Request.headers)
                    record()
                    return Request.response

            else:
                if Request.headers != None:
                    Request.response = requests.get(Request.url,headers=Request.headers)
                    record()
                    return Request.response

                else:
                    Request.response = requests.get(Request.url, headers=Request.headers)
                    record()
                    return Request.response
        if Request.method == "post":
            if Request.params != None:
                if Request.headers != None:
                    if Request.files != None:
                        Request.response = requests.post(Request.url,data=Request.params,headers=Request.headers,files=Request.files)
                        record()
                        return Request.response
                    else:
                        Request.response = requests.post(Request.url, data=Request.params, headers=Request.headers)
                        record()
                        return Request.response

                else:
                    if Request.files != None:
                        Request.response = requests.post(Request.url, data=Request.params,files=Request.files)
                        record()
                        return Request.response
                    else:
                        Request.response = requests.post(Request.url, data=Request.params)
                        record()
                        return Request.response

            else:
                if Request.headers != None:
                    Request.response = requests.post(Request.url,headers=Request.headers)
                    record()
                    return Request.response

                else:
                    Request.response = requests.post(Request.url, headers=Request.headers)
                    record()
                    return Request.response
