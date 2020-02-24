from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import (UserSignUpForm, ExtendedDoctorsDetailForm, ExtendedPatientsDetailForm,
                    UpdateUserProfile, UpdatePatientProfile, UpdateDoctorProfile)


def LoginpageView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/accounts/profile')
        else:
            messages.error(request, 'Username or Password is invalid')
            return redirect('/accounts/login')
    return render(request, 'login.html')


def ProfileView(request):
    user = request.user
    if user is None:
        return render(request, 'login.html')
    args = {'user': user}
    if user.is_patient:
        return render(request, 'Pprofile.html', args)
    elif user.is_doctor:
        return render(request, 'Dprofile.html', args)
    else:
        return render(request, 'login.html')


def DoctorSignupView(request):
    if request.method == 'POST':

        user_form = UserSignUpForm(request.POST)
        doctor_form = ExtendedDoctorsDetailForm(request.POST)

        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save(commit=False)
            user.is_doctor = True
            raw_password = user_form.cleaned_data.get('password1')
            user.save()
            # doctor_form.save(commit=False)
            user.doctor_detail.specialization = doctor_form.cleaned_data.get('specialization')
            user.doctor_detail.open_time = doctor_form.cleaned_data.get('open_time')
            user.doctor_detail.close_time = doctor_form.cleaned_data.get('close_time')
            if doctor_form.cleaned_data.get('specialization') is not None:
                user.doctor_detail.is_verified = True
            user.doctor_detail.save()
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                return redirect('/accounts/login')
            else:
                return render(request, 'Dsignup.html')
        messages.error(request, "Form is invalid")
        return render(request, 'Dsignup.html')
    else:
        user_form = UserSignUpForm()
        doctor_form = ExtendedDoctorsDetailForm()
    return render(request, 'Dsignup.html', {'user_form': user_form, 'doctor_form': doctor_form})


def PatientSignupView(request):
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        patient_form = ExtendedPatientsDetailForm(request.POST)

        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.is_patient = True
            raw_password = user_form.cleaned_data.get('password1')
            user.save()
            user.patient_detail.age = patient_form.cleaned_data.get('age')
            user.patient_detail.save()
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                return redirect('/accounts/login')
            else:
                messages.error(request, "User in not authenticated")
                return render(request, 'Psignup.html')
        messages.error(request, "Form is invalid")
        return render(request, 'Psignup.html', {'user_form': user_form, 'patient_form': patient_form})
    else:
        user_form = UserSignUpForm()
        patient_form = ExtendedPatientsDetailForm()
        return render(request, 'Psignup.html', {'user_form': user_form, 'patient_form': patient_form})


def DoctorProfileUpdateView(request):
    if request.method == 'POST':
        update_user_form = UpdateUserProfile(request.POST, instance=request.user)
        update_doctor_form = UpdateDoctorProfile(request.POST, instance=request.user.doctor_detail)
        if update_user_form.is_valid() and update_doctor_form.is_valid():
            user = update_user_form.save(commit=False)
            user.is_doctor = True
            user.save()
            # doctor_form.save(commit=False)
            user.doctor_detail.specialization = update_doctor_form.cleaned_data.get('specialization')
            user.doctor_detail.open_time = update_doctor_form.cleaned_data.get('open_time')
            user.doctor_detail.close_time = update_doctor_form.cleaned_data.get('close_time')
            if update_doctor_form.cleaned_data.get('specialization') is not None:
                user.doctor_detail.is_verified = True
            user.doctor_detail.save()
            return redirect('/accounts/profile')
        messages.error(request, "Form is invalid")
        return render(request, 'Dupdate.html')
    else:
        update_user_form = UpdateUserProfile(instance=request.user)
        update_doctor_form = UpdateDoctorProfile(instance=request.user.doctor_detail)
    return render(request, 'Dupdate.html',
                  {'update_user_form': update_user_form, 'update_doctor_form': update_doctor_form})


def PatientProfileUpdateView(request):
    if request.method == 'POST':
        update_user_form = UpdateUserProfile(request.POST, instance=request.user)
        update_patient_form = UpdatePatientProfile(request.POST, instance=request.user.patient_detail)

        if update_user_form.is_valid() and update_patient_form.is_valid():
            user = update_user_form.save(commit=False)
            user.is_patient = True
            user.save()
            user.patient_detail.age = update_patient_form.cleaned_data.get('age')
            user.patient_detail.save()
            return redirect('/accounts/profile')
        messages.error(request, "Form is invalid")
        return render(request, 'Pupdate.html')
    else:
        update_user_form = UpdateUserProfile(instance=request.user)
        update_patient_form = UpdatePatientProfile(instance=request.user.patient_detail)
        return render(request, 'Pupdate.html',
                      {'update_user_form': update_user_form, 'update_patient_form': update_patient_form})


def ChangePasswordView(request):
    if request.method == 'POST':
        change_password_form = PasswordChangeForm(data=request.POST, user=request.user)

        if change_password_form.is_valid():
            change_password_form.save()
            update_session_auth_hash(request, change_password_form.user)
            return redirect('/accounts/profile')
        messages.error(request, "Form is invalid")
        return render(request, 'change_password.html', {'change_password_form': change_password_form})
    else:
        change_password_form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'change_password_form': change_password_form})
