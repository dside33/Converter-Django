from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from login.forms import LoginForm, RegisterForm

from .utils import create_jwt_token

from user_profile.models import UserProfile


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', '/')
                return HttpResponseRedirect(next_url)
            
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')

# <a href="{% url 'profile-detail' pk=user_profile.id %}">
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            UserProfile.objects.create(user=user)

            access_token = create_jwt_token(user)
            print(access_token)
            
            response = redirect('/')
            response.set_cookie(key='access_token', value=access_token, httponly=True)
            return response
            
    else:
        form = RegisterForm()

    return render(request, 'login/register.html', {'form': form})