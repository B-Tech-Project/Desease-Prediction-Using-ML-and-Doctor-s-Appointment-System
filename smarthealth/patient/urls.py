from django.urls import path
from . import views

urlpatterns = [
    path('', views.searchDisease, name='searchDisease'),
    path('register/', views.patientregister, name='patientRegister'),
    path('bookAppointment', views.bookAppointment, name='bookAppointment'),
    path('profile', views.patientProfile, name='patientProfile'),
]
