from django.db import models

# Create your models here.
class User(models.Model):
    '''
    用户表
    '''
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=32)
    email = models.EmailField(verbose_name="邮箱",max_length=32)

    roles = models.ManyToManyField(to="Roles",verbose_name="用户角色",blank=True)

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.username

class Roles(models.Model):
    '''
    角色表
    '''
    title = models.CharField(verbose_name="角色",max_length=32)
    permissions = models.ManyToManyField(to="Permission",verbose_name="角色权限")

    class Meta:
        verbose_name_plural = "角色表"
    def __str__(self):
        return self.title

class Permission(models.Model):
    '''
    权限表
    '''
    title = models.CharField(verbose_name="权限",max_length=32)
    url = models.CharField(verbose_name="含正则的url",max_length=64)
    is_menu = models.BooleanField(verbose_name="是否是菜单")
    code = models.CharField(verbose_name="代码",max_length=32)
    group = models.ForeignKey(verbose_name="所属组", to="Group")




    class Meta:
        verbose_name_plural = "权限表"

    def __str__(self):
        return self.title

class Group(models.Model):
    title = models.CharField(verbose_name="组名称",max_length=32)

    def __str__(self):
        return self.title