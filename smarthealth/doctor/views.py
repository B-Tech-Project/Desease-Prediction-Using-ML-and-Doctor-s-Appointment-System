from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
from .forms import RegisterDoctorForm
from .decorators import unauthenticated_user, allowed_user


@unauthenticated_user
def doctorregister(request):
    form = RegisterDoctorForm
    if request.method == "POST":
        form = RegisterDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Your account is Successfully Registered, Login to continue !! "+user)
            return redirect('loginpage')
    # group = Group.objects.get(name='doctor')
    # user.groups.add(group)
    context = {'form': form}
    return render(request, 'doctor/doctorRegister.html', context)


@login_required(login_url='loginpage')
@allowed_user(allowed_role=['doctor'])
def showAppointment(request):
    return render(request, 'doctor/showAppointment.html')


@login_required(login_url='loginpage')
@allowed_user(allowed_role=['doctor'])
def doctorProfile(request):
    return render(request, 'doctor/doctorProfile.html')
