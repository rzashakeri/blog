from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from newsletter.forms import NewsletterForm
from newsletter.models import NewsletterModel


class NewsletterView(View):
    def get(self, request: HttpRequest):
        newsletter_form = NewsletterForm()
        context = {
            'newsletter_form': newsletter_form
        }
        return render(request, 'newsletter/newsletter_component.html', context)

    def post(self, request: HttpRequest):
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            new_email = newsletter_form.cleaned_data.get('email')
            email_is_exists = NewsletterModel.objects.filter(email=new_email).exists()
            if email_is_exists:
                messages.warning(request, 'email has exists')
            else:
                newsletter = NewsletterModel(email=new_email)
                newsletter.save()
                messages.success(request, 'thanks for submit email')
                return redirect('home')
        return redirect('home')

