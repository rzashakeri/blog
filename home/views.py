from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'shared/_layout.html'


def header_component(request):
    return render(request, 'shared/header_component.html')
