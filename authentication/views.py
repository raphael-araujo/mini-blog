from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm

# Create your views here.


def login(request):
    form = LoginForm

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.error(
                request, message="Your username and password didn't match. Please try again.")

            return redirect('/auth/login')

        else:
            auth.login(request, user)

            return redirect('/blog/all_blogs')

    else:
        if request.user.is_authenticated:
            return redirect('/blog/')

        return render(request, 'login.html', {'form': form})


def register(request):
    form = RegisterForm

    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.filter(username=username)

        if user.exists() and password1 != password2:
            messages.error(request, message='This username already exists')
            messages.error(
                request, message=form.error_messages['password_mismatch'])

            return redirect('/auth/register')

        if password1 != password2:
            messages.error(
                request, message=form.error_messages['password_mismatch'])

            return redirect('/auth/register')

        if user.exists():
            messages.error(request, message='This username already exists')

        try:
            user = User.objects.create_user(
                username=username, password=password2)
            user.save()
            messages.success(request, message='user created successfully.')

            return redirect('/auth/login')

        except:
            return redirect('/auth/register')

    else:
        if request.user.is_authenticated:
            return redirect('/blog/')

        return render(request, 'register.html', {'form': form})
