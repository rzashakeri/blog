from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .forms import CommentForm
from django.views.generic import DetailView, ListView, TemplateView

from article.models import Article, ArticleCategory


class SingleArticle(DetailView):
    template_name = 'article/single_article.html'
    model = Article
    context_object_name = 'single_article'

    def get_context_data(self, **kwargs):
        context = super(SingleArticle, self).get_context_data()
        slug = self.kwargs.get('slug')
        article = Article.objects.filter(slug__iexact=slug).first()
        categories = article.category.prefetch_related('article_set').all()
        context['categories'] = categories
        return context


class CategoryArticle(ListView):
    template_name = 'article/category.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 2

    def get_queryset(self):
        query = super(CategoryArticle, self).get_queryset()
        category_name = self.kwargs.get('category')
        query = query.filter(is_active=True, category__name=category_name)
        return query

    def get_context_data(self, **kwargs):
        context = super(CategoryArticle, self).get_context_data()
        context['category_name'] = self.kwargs.get('category')
        return context


class CommentArticle(TemplateView):
    template_name = 'article/components/comment_component.html'

    def get_context_data(self, **kwargs):
        context = super(CommentArticle, self).get_context_data()
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context


class RecommendationArticle(TemplateView):
    template_name = 'article/components/recommendation_component.html'


class AuthorArticle(TemplateView):
    template_name = 'article/components/author_component.html'
