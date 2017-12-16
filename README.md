## rbac权限管理大致流程

day1

​	a: rbac/model.py 创建表(三个类，五张表)

​	b: 基于django admin后台录入数据

​	c: 用户登录程序：

​	 	init_permission.py 获取用户权限，写入session

​	d : 中间件

​		设置白名单

​		获取当前url与session中用户权限比较

day2

​	问题：页面是否显示添加，删除，修改等按钮

​	a: 修改表结构，permission表中增加一列code,创建 group 表

​	b: 生成数据结构 组id：{code:["list","add","edit","delete"],urls:[/userinfo/,/userinfo/add/,/userinfo/edit/(\d+),/userinfo/delete/(\d+)]}

​		将code 写入 request中 以此来解决是否显示添加，删除，修改等按钮