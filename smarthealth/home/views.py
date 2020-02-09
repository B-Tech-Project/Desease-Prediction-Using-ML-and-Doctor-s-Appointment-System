from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .decorators import unauthenticated_user


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('searchDisease')
        else:
            messages.error(request, 'Username or Password is incorrect! Please type valid credentials')
    context = {}
    return render(request, 'home.html', context)


@login_required(login_url='loginpage')
def logout_request(request):
    logout(request)
    return redirect('loginpage')
