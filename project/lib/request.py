#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

#Auther:fured
#date:2018.07.02
#desc:Packaging requests

class Record(object):
    method = ""
    url = ""
    response_time = 0.0
    data_size = 0.0
    # print Record.data_size
    status_code = ""
    pass


def record():
    Record.method = Request.method
    Record.url = Request.url
    Record.response_time = Response.ResponseTime(Request.response)
    Record.data_size = Response.DataSize(Request.response)
    #print Record.data_size
    Record.status_code = Response.Code(Request.response)
    #Request.method = None
    #Request.url = None
    #Request.params = None
    #Request.headers = None
    #Request.response = None

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


class Response(object):

    def __init__(self):
        pass

    @staticmethod
    def Code(response):
        return response.status_code

    @staticmethod
    def Body(response):
        return response.text

    @staticmethod
    def Url(response):
        return response.url

    @staticmethod
    def ResponseTime(response):
        return  response.elapsed.total_seconds() * 1000

    #单位：字节，Byte
    @staticmethod
    def DataSize(response):
        if dict(response.headers).has_key("Content-Length"):
            return float(response.headers["Content-Length"])
        else:
            return 0

class Request(object):

    support_method = ["get","post"]
    method = None
    params = None
    headers = None
    url = None
    response = None
    def __init__(self):
        pass

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
                    Request.response = requests.post(Request.url,data=Request.params,headers=Request.headers)
                    record()
                    return Request.response
                else:
                    Request.response = requests.post(Request.url, data=Request.params, headers=Request.headers)
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
