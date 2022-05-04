from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import auth , messages
from .forms import LoginForm

# Create your views here.


def login(request):
    form = LoginForm
    # form.get_invalid_login_error

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        # print(form.errors)
        user = auth.authenticate(username=username, password=password)
        
        if not user:
            messages.error(request, message="Your username and password didn't match. Please try again.")
            # print('A')
            # form.error_messages
            # form.errors
            # form.get_invalid_login_error
            
            return redirect('/auth/login')
        
        else:
            auth.login(request, user)

            return redirect('/blog/all_blogs')

    else:
        if request.user.is_authenticated:
            return redirect('/blog/')

        return render(request, 'login.html', {'form': form})


def register(request):
    return HttpResponse('teste')
