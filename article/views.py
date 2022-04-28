from django.shortcuts import render
from django.views.generic import DetailView

from article.models import Article


class SingleArticle(DetailView):
    template_name = 'article/single_article.html'
    model = Article
    context_object_name = 'single_article'