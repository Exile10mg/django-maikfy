from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.login, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path('password_reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'), name="password_reset_complete"),
]