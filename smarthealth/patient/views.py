from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import RegisterPatientForm
from .decorators import unauthenticated_user, allowed_user


@unauthenticated_user
def patientregister(request):
    form = RegisterPatientForm
    if request.method == "POST":
        form = RegisterPatientForm(request.POST)
        if form.is_valid():
            form.save()
    # group = Group.objects.get(name='patient')
    # user.groups.add(group)
    context = {'form': form}
    return render(request, 'patient/patientRegister.html', context)


@login_required(login_url='loginpage')
@allowed_user(allowed_role=['patient'])
def searchDisease(request):
    return render(request, 'patient/diseaseSearch.html')


@login_required(login_url='loginpage')
@allowed_user(allowed_role=['patient'])
def bookAppointment(request):
    return render(request, 'patient/bookAppointment.html')


@login_required(login_url='loginpage')
@allowed_user(allowed_role=['patient'])
def patientProfile(request):
    return render(request, 'patient/patientProfile.html')
