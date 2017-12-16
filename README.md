## rbac权限管理大致流程

day1

​	a: rbac/model.py 创建表(三个类，五张表)

​	b: 基于django admin后台录入数据

​	c: 用户登录程序：

​	 	init_permission.py 获取用户权限，写入session

​	d : 中间件

​		设置白名单

​		获取当前url与session中用户权限比较