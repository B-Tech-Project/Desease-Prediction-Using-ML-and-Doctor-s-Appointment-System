from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import (LoginpageView, ProfileView, DoctorSignupView, PatientSignupView,
                    PatientProfileUpdateView, DoctorProfileUpdateView, ChangePasswordView)

app_name = 'users'

urlpatterns = [
    path('login', LoginpageView, name='login'),

    path('logout', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),

    path('profile', login_required(ProfileView), name='profile'),
    # path('Dprofile', login_required(ProfileView), name='Dprofile'),

    path('Dsignup', DoctorSignupView, name='dsignup'),
    path('Psignup', PatientSignupView, name='psignup'),

    path('Patient/edit', login_required(PatientProfileUpdateView), name='Pupdateprofile'),
    path('Doctor/edit', login_required(DoctorProfileUpdateView), name='Dupdateprofile'),

    path('change_password', login_required(ChangePasswordView), name='ChangePassword'),
]