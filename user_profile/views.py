from django.http import Http404, HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from user_management.models import User


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
            context = {
                'user': user
            }
            return render(request, 'user_profile/edit_profile.html', context)
        else:
            raise Http404


def user_profile_options(request):
    return render(request, 'user_profile/component/user_profile_options.html')
