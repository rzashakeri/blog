from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import CommentForm
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from article.models import Article, ArticleCategory, ArticleComment


class SingleArticle(View):
    def get(self, request, slug):
        single_article = Article.objects.filter(slug__iexact=slug).first()
        categories = single_article.category.all()
        context = {
            'single_article': single_article,
            'categories': categories
        }
        return render(request, 'article/single_article.html', context)

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            article_id = request.POST.get('article_id')
            comment = comment_form.cleaned_data.get('comment_text')
            parent_id = request.POST.get('parent_id')
            new_comment = ArticleComment(article_id=article_id,
                                         user_id=request.user.id,
                                         comment=comment,
                                         parent_id=parent_id)
            new_comment.save()
            slug = kwargs.get('slug')
            return redirect(reverse('single_article', kwargs={'slug': slug}))


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


class CommentArticle(View):
    def get(self, request, *args, **kwargs):
        comment_form = CommentForm()
        single_article = kwargs.get('single_article')
        context = {
            'comment_form': comment_form,
            'single_article': single_article
        }
        return render(request, 'article/components/comment_component.html', context)


class RecommendationArticle(TemplateView):
    template_name = 'article/components/recommendation_component.html'


class AuthorArticle(TemplateView):
    template_name = 'article/components/author_component.html'
