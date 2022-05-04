from django.shortcuts import render
from django.views.generic import CreateView, TemplateView


class RegisterView(TemplateView):
    template_name = 'account/register.html'
