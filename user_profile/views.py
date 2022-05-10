from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from user_management.models import User


class UserProfile(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_id = request.user.id
            user: User = User.objects.filter(id=user_id).first()
            context = {
                'user': user
            }
            return render(request, 'user_profile.html', context)
        else:
            raise Http404


def user_profile_options(request):
    return render(request, 'user_profile/component/user_profile_options.html')
