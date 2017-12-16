#!/usr/bin/env python
# -*- coding:utf-8 -*-
# date:"2017-12-14,0:16"

from django.conf import settings


def init_permission(user, request):
    '''
    获取权限信息列表，放入session中
    :param user:
    :param request:
    :return:
    '''
    permission_list = user.roles.values(
        "permissions__id",#权限ID
        "permissions__title",#权限名
        "permissions__url",  # url
        "permissions__group_id",#组ID
        "permissions__code",#权限代码
        "permissions__group__menu_id",#菜单ID
        "permissions__group__menu__title",#菜单名
        "permissions__menu_gp_id"#组内菜单id,为空表示是菜单


    ).distinct()  # 获取权限信息列表，并去重
    #菜单相关
    sub_permission = []
    for item in permission_list:
        temp = {
            "id":item["permissions__id"],
            "title":item["permissions__title"],
            "url":item["permissions__url"],
            "menu_gp_id": item["permissions__menu_gp_id"],
            "menu_id": item["permissions__group__menu_id"],
            "menu_title": item["permissions__group__menu__title"]
        }

        sub_permission.append(temp)

    request.session[settings.PERMISSION_MENU_KEY] = sub_permission


    #权限相关
    result = {}
    for item in permission_list:
        group_id = item["permissions__group_id"]
        url = item["permissions__url"]
        code = item["permissions__code"]
        if group_id in result:
            result[group_id]["codes"].append(code)
            result[group_id]["urls"].append(url)

        else:
            result[group_id] = {
                "codes": [code,],
                "urls": [url,]
            }

    request.session[settings.PERMISSION_URL_DICT_KEY] = result
