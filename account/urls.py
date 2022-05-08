from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot_password'),
    path('activate-account/<str:email_active_code>', views.ActiveAccountView.as_view(), name='activate_account'),
    path('reset-password/<str:reset_password_code>', views.ResetPasswordView.as_view(), name='reset_password')
]