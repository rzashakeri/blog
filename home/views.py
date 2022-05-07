from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from article.models import Article
from site_setting.models import HeaderLink, SiteSetting, Intro


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self,**kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['articles_general'] = Article.objects.filter(category__name='general', is_active=True).all()[:3]
        context['articles_web'] = Article.objects.filter(category__name='web', is_active=True).all()[:3]
        context['articles_programming'] = Article.objects.filter(category__name='programming', is_active=True).all()[:3]
        return context


def header_component(request: HttpRequest):
    context = {
        'links': HeaderLink.objects.filter(is_active=True),
        'site': SiteSetting.objects.filter(is_active=True).first()
    }
    return render(request, 'shared/header_component.html', context)


def intro_component(request):
    context = {
        'intro': Intro.objects.filter(is_active=True).first()
    }
    return render(request, 'shared/intro_component.html', context)


def newsletter_component(request):
    return render(request, 'shared/newsletter_component.html')


def footer_component(request):
    return render(request, 'shared/footer_component.html')
