from django.urls import path
from . import views

from django.contrib.auth.views import auth_logout

urlpatterns = [
    path('register/', views.doctorregister, name='doctorRegister'),
    path('', views.showAppointment, name='showAppointment'),
    path('profile', views.doctorProfile, name='doctorProfile'),
]
