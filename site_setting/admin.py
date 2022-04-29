from django.contrib import admin
from . import models


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'phone_number', 'email', 'is_active']
    list_editable = ['phone_number', 'email', 'is_active']


admin.site.register(models.SiteSetting, SiteSettingAdmin)


class HeaderLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'is_active']
    list_editable = ['url', 'is_active']


admin.site.register(models.HeaderLink, HeaderLinkAdmin)


class IntroAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'description', 'is_active']
    list_editable = ['tag', 'description', 'is_active']


admin.site.register(models.Intro, IntroAdmin)
