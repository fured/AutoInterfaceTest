#!/usr/bin/python
# -*- coding: UTF-8 -*-

#Auther:fured
#date:2018.07.02
#desc:Packaging requests


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

