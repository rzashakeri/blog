from django.shortcuts import render
from django.views.generic import DetailView, ListView

from article.models import Article, ArticleCategory


class SingleArticle(DetailView):
    template_name = 'article/single_article.html'
    model = Article
    context_object_name = 'single_article'


class CategoryArticle(ListView):
    template_name = 'article/category.html'
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        query = super(CategoryArticle, self).get_queryset()
        category_name = self.kwargs.get('category')
        query = query.filter(is_active=True, category__name=category_name)
        return query

    def get_context_data(self, **kwargs):
        context = super(CategoryArticle, self).get_context_data()
        context['category_name'] = self.kwargs.get('category')
        return context
