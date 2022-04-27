from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


admin.site.register(models.User, UserAdmin)
