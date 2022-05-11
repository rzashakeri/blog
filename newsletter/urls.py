from django.urls import path
from . import views

urlpatterns = [
    path('add-email/', views.NewsletterView.as_view(), name='newsletter')
]