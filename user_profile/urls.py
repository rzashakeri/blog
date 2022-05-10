from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name='user_profile')
]
