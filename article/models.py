from django.db import models

from user_management.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, verbose_name='parent', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='category name')
    description = models.CharField(max_length=300, verbose_name='description')
    slug = models.SlugField(max_length=300, verbose_name='url slug', unique=True)
    is_active = models.BooleanField(verbose_name='is active ?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    short_description = models.CharField(max_length=400, verbose_name='short description')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(upload_to='article')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='author')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='create date')
    slug = models.SlugField(max_length=400, unique=True, verbose_name='url slug')
    is_active = models.BooleanField(verbose_name='is active ?')
    category = models.ManyToManyField(to=ArticleCategory,verbose_name='category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'


class ArticleComment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='user')
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE, verbose_name='article')
    comment = models.TextField(verbose_name='comment')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='comment create date')
    parent = models.ForeignKey(to='ArticleComment', on_delete=models.CASCADE, verbose_name='parent', null=True, blank=True)
    confirm = models.BooleanField(verbose_name='confirmed ?', default=False)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

