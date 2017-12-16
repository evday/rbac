#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2017-12-16,11:24"

import re

from django.conf import settings
from django.shortcuts import redirect,HttpResponse

class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class RbacMiddleWare(MiddlewareMixin):
    '''
    1,获取当前请求的url
    2,获取session中当前用户的权限url
    '''

    def process_request(self,request):

        current_url = request.path_info #当前请求的url

        #与settings中设置的无需验证(白名单)的url做比较
        for url in settings.VALID_URL:
            regex = "^{0}$".format(url)
            if re.match(regex,current_url):# 将白名单的url和当前用户请求的url匹配
                return None

        #获取session中的权限列表
        permission_list = request.session.get("permission_url_list")

        #如果没有权限列表,返回登录页面
        if not permission_list:
            return redirect("/login/")

        flag = False
        for db_url in permission_list:
            regex = "^{0}$".format(db_url)
            if re.match(regex,current_url):
                flag = True
            break
        if not flag:
            return HttpResponse("对不起，该页面您无权访问")