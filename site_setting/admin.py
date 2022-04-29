from django.contrib import admin
from . import models


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'phone_number', 'email']
    list_editable = ['phone_number', 'email']


admin.site.register(models.SiteSetting, SiteSettingAdmin)


class HeaderLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link']
    list_editable = ['link']


admin.site.register(models.HeaderLink, HeaderLinkAdmin)