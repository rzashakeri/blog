from django.contrib import admin
from . import models


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']
    

admin.site.register(models.NewsletterModel, NewsletterAdmin)