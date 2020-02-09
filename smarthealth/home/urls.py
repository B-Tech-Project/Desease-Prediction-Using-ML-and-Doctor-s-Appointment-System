from django.urls import path, include
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [
    path('', views.loginPage, name='loginpage'),
    path("logout", views.logout_request, name='logout'),
]
