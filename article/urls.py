from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.SingleArticle.as_view(), name='single_article')
]