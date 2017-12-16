#!/usr/bin/env python
#-*- coding:utf-8 -*-
#date:"2017-12-16,13:40"

class Base_permission_list(object):
    def __init__(self,code_list):
        self.code_list = code_list

    def has_add(self):
        if "add" in self.code_list:
            return True
    def has_edit(self):
        if "edit" in self.code_list:
            return True
    def has_delete(self):
        if "delete" in self.code_list:
            return True


#类的继承
class OrderPermissionList(Base_permission_list):
    def has_report(self):
        if "report" in self.code_list:
            return True