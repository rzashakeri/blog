from time import sleep

from django.contrib import messages
from django.contrib.auth import logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.views import View
from user_management.models import User
from user_profile.forms import EditProfileModelForm
from utility.email_service import send_email


class UserProfileView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            user_id = request.user.id
            user: User = User.objects.filter(id=user_id).first()
            context = {
                'user': user
            }
            return render(request, 'user_profile/user_profile.html', context)
        else:
            raise Http404


class EditProfileView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            # get current user id
            user_id = request.user.id
            # get user by id
            user: User = User.objects.filter(id=user_id).first()
            edit_profile_form = EditProfileModelForm(instance=user)
            context = {
                'edit_profile_form': edit_profile_form
            }
            return render(request, 'user_profile/edit_profile.html', context)
        else:
            raise Http404

    def post(self, request: HttpRequest):
        user: User = User.objects.filter(id=request.user.id).first()
        current_user_email = user.email
        edit_profile_form = EditProfileModelForm(request.POST, instance=user)
        if edit_profile_form.is_valid():
            user_email = edit_profile_form.cleaned_data.get('email')
            if user_email != current_user_email:
                email_is_exists = User.objects.filter(email__iexact=user_email).exists()
                if email_is_exists:
                    edit_profile_form.add_error('email', 'The email is a duplicate ')
                    context = {
                        'edit_profile_form': edit_profile_form
                    }
                    return render(request, 'user_profile/edit_profile.html', context)
                else:
                    messages.warning(request, 'Confirmation email sent, You can log in again after confirming the email')
                    user.is_active = False
                    user.save()
                    send_email('confirm email', user_email, {'user': user}, 'emails/activate_account.html')
                    logout(request)
                    return redirect('login')
            edit_profile_form.save(commit=True)
            return redirect('edit_profile')
        context = {
            'edit_profile_form': edit_profile_form
        }
        return render(request, 'user_profile/edit_profile.html', context)


def user_profile_options(request, *args, **kwargs):
    context = {
        'edit_profile_form': kwargs.get('edit_profile_form')
    }
    return render(request, 'user_profile/component/user_profile_options.html', context)
