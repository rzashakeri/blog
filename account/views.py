from django import forms
from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, TemplateView, FormView

from account.forms import RegisterForm, LoginForm
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
                                is_active=False,
                                username=email)
                new_user.set_password(password)
                new_user.save()
                return redirect('home')
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                check_password = user.check_password(user_password)
                if check_password:
                    login(request, user)
                    return redirect('home')
                else:
                    login_form.add_error('password', 'password is not correct !')
            else:
                login_form.add_error('email', 'email dose not exists !')
        context = {
            'login_form': login_form
        }
        return render(request, 'account/login.html', context)
