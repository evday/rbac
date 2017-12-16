import json

from django.shortcuts import render,redirect,HttpResponse

from rbac import models
from rbac.service.init_permission import init_permission


from permission.page_permission_list.page_permission_list import Base_permission_list,OrderPermissionList


def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.is_ajax():

        state = {"state": None}
        username = request.POST.get("user")

        if username == "":
            state["state"] = "user_none"
            return HttpResponse(json.dumps(state))
        password = request.POST.get("pwd")

        if password == "":
            state["state"] = "pwd_none"
            return HttpResponse(json.dumps(state))

        user = models.User.objects.filter(username=username, password=password).first()
        if user:
            state["state"] = "login_success"
            init_permission(user,request)

        else:
            state["state"] = "failed"

        return HttpResponse(json.dumps(state))

def index(request):
    return HttpResponse("欢迎登录")

def userinfo(request):
    permission_list = Base_permission_list(request.permission_code_list)
    userinfo_list = models.User.objects.all()
    return render(request,'userinfo.html',locals())

def userinfo_add(request):
    return render(request,'userinfo_add.html')
def order(request):
    order_permission_list = OrderPermissionList(request.permission_code_list)
    return render(request,"order.html",locals())