from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Roles)
admin.site.register(models.Permission)
admin.site.register(models.Group)
