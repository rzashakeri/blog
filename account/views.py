from django import forms
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, TemplateView, FormView

from account.forms import RegisterForm
from user_management.models import User


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # check email exists
            email = register_form.cleaned_data.get('email')
            user_email: bool = User.objects.filter(email__iexact=email).exists()
            if user_email:
                register_form.add_error('email', 'email exists !')
            else:
                # user data
                first_name = register_form.cleaned_data.get('first_name')
                last_name = register_form.cleaned_data.get('last_name')
                password = register_form.cleaned_data.get('password')
                new_user = User(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                is_active=False)
                new_user.set_password(password)
                new_user.save()
                return redirect('home')
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register.html', context)
