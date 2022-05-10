from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view(), name='user_profile'),
    path('edit/', views.EditProfileView.as_view(), name='edit_profile')
]
