#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2017-12-14,0:16"

from django.conf import settings



def init_permission(user,request):
    '''
    获取权限信息列表，放入session中
    :param user:
    :param request:
    :return:
    '''
    permission_list = user.roles.values(
        "permissions__id",
        "permissions__title",#权限名
        "permissions__url",#url

    ).distinct() #获取权限信息列表，并去重


    url_list = []
    for item in permission_list:
        url_list.append(item["permissions__url"])
    print(url_list)
    request.session["permission_url_list"] = url_list
