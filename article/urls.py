from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>', views.SingleArticle.as_view(), name='single_article'),
    path('category/<slug:category>', views.CategoryArticle.as_view(), name='category_article')
]