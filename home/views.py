from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from article.models import Article
from site_setting.models import HeaderLink, SiteSetting


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self):
        context = super(Home, self).get_context_data()
        context['articles_general'] = Article.objects.filter(category__name='general', is_active=True).all()
        context['articles_web'] = Article.objects.filter(category__name='web', is_active=True).all()
        context['articles_programming'] = Article.objects.filter(category__name='programming', is_active=True).all()
        return context


def header_component(request):
    context = {
        'links': HeaderLink.objects.filter(is_active=True),
        'site': SiteSetting.objects.filter(is_active=True).first()
    }
    return render(request, 'shared/header_component.html', context)


def intro_component(request):
    return render(request, 'shared/intro_component.html')


def newsletter_component(request):
    return render(request, 'shared/newsletter_component.html')


def footer_component(request):
    return render(request, 'shared/footer_component.html')
