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

        "permissions__url",  # url
        "permissions__group_id",
        "permissions__code"

    ).distinct()  # 获取权限信息列表，并去重

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
    print(result,"-----------")
    request.session[settings.PERMISSION_URL_DICT_KEY] = result
