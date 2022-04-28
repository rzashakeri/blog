from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'author', 'create_date']
    list_editable = ['short_description']


admin.site.register(models.Article, ArticleAdmin)


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active', 'parent']


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
