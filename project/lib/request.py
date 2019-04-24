#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

"""
Auther:fured
date:2018.07.02
desc:Packaging requests
"""


class Record(object):
    """
    记录每个请求的数据，用于生成报告

    """
    method = ""
    url = ""
    response_time = 0.0
    data_size = 0.0
    status_code = ""


def record():
    """
    记录每个请求进行过程中的数据
    :return:
    """
    Record.method = Request.method
    Record.url = Request.url
    Record.response_time = Response.ResponseTime(Request.response)
    Record.data_size = Response.DataSize(Request.response)
    Record.status_code = Response.Code(Request.response)


def clear():
    """
    执行完一个测试用例即一个请求后，清空记录的数据
    :return:
    """
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


class Response(object):
    """
    封装一层，返回响应中的数据
    """
    @staticmethod
    def Code(response):
        return response.status_code

    @staticmethod
    def Body(response):
        return response.text

    @staticmethod
    def Content(response):
        return response.content

    @staticmethod
    def Url(response):
        return response.url


    @staticmethod
    def ResponseTime(response):
        """
        获取返回响应的时间，单位：毫秒（ms）
        :param response:
        :return:
        """
        return response.elapsed.total_seconds() * 1000


    @staticmethod
    def DataSize(response):
    """
    获取返回数据的大小，单位：字节（Byte）
    """
        if dict(response.headers).has_key("Content-Length"):
            return float(response.headers["Content-Length"])
        else:
            return 0


class Request(object):
    """
    获取返回数据的大小，单位：字节（Byte）
    目前只支持：Get、POST
    """
    support_method = ["get","post"]
    method = None
    params = None
    headers = None
    url = None
    response = None
    files = None

    @staticmethod
    def send():
        """
        发送http请求
        :return:
        """
        # 关闭移除ssl证书认证后弹出的警告信息
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        if Request.method is None or Request.url is None:
            raise Exception("Request is error!")
            return None
        if Request.method not in Request.support_method:
            raise Exception("Not support " + Request.method+" method!")
            return None
        if Request.method == "get":
            if Request.params is not None:
                if Request.headers is not None:
                    Request.response = requests.get(Request.url, params=Request.params,
                                                    headers=Request.headers, verify=False)
                    record()
                    return Request.response

                else:
                    Request.response = requests.get(Request.url, params=Request.params,
                                                    headers=Request.headers, verify=False)
                    record()
                    return Request.response

            else:
                if Request.headers is not None:
                    Request.response = requests.get(Request.url, headers=Request.headers, verify=False)
                    record()
                    return Request.response

                else:
                    Request.response = requests.get(Request.url, headers=Request.headers, verify=False)
                    record()
                    return Request.response
        if Request.method == "post":
            if Request.params is not None:
                if Request.headers is not None:
                    if Request.files is not None:
                        Request.response = requests.post(Request.url, data=Request.params, headers=Request.headers,
                                                         files=Request.files, verify=False)
                        record()
                        return Request.response
                    else:
                        Request.response = requests.post(Request.url, data=Request.params, headers=Request.headers,
                                                         verify=False)
                        record()
                        return Request.response

                else:
                    if Request.files is not None:
                        Request.response = requests.post(Request.url, data=Request.params, files=Request.files,
                                                         verify=False)
                        record()
                        return Request.response
                    else:
                        Request.response = requests.post(Request.url, data=Request.params, verify=False)
                        record()
                        return Request.response

            else:
                if Request.headers is not None:
                    if Request.files is not None:
                        Request.response = requests.post(Request.url, headers=Request.headers, files=Request.files,
                                                         verify=False)
                        record()
                        return Request.response
                    else:
                        Request.response = requests.post(Request.url, headers=Request.headers,
                                                         verify=False)
                        record()
                        return Request.response
                else:
                    if Request.files is not None:
                        Request.response = requests.post(Request.url, files=Request.files, verify=False)
                        record()
                        return Request.response
                    else:
                        Request.response = requests.post(Request.url, verify=False)
                        record()
                        return Request.response
