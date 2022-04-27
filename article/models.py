from django.db import models

from user_management.models import User


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    short_description = models.CharField(max_length=400, verbose_name='short description')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='article')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='author')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create date')
    slug = models.SlugField(max_length=400, unique=True, verbose_name='url slug')
    is_active = models.BooleanField(verbose_name='is active ?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
