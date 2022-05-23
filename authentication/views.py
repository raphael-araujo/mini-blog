from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import LoginForm, RegisterForm

# Create your views here.


def login(request):
    """View function para a página de login"""

    form = LoginForm

    if request.method == 'POST':
        # coleta as informações preenchidas pelo usuário e guarda em variáveis:
        username = request.POST['username']
        password = request.POST['password']

        # verifica se as credenciais são válidas:
        user = auth.authenticate(username=username, password=password)

        if not user:
            # se as credenciais forem inválidas, uma mensagem de erro será mostrada:
            messages.error(
                request, message="Your username and password didn't match. Please try again.")

            # e o usuário será redirecionado novamente para a página de login:
            return redirect('/auth/login')

        else:
            # se as credenciais são válidas, o usuário será logado:
            auth.login(request, user)

            # e será redirecionado para a lista de blogs:
            return redirect('/blog/all_blogs')

    else:
        if request.user.is_authenticated:
            # se o usuário já estiver logado, ele será redirecionado para a página inicial:
            return redirect('/blog/')

        return render(request, 'login.html', {'form': form})


def register(request):
    """View function para a página de registro"""

    form = RegisterForm

    if request.method == 'POST':
        # coleta as informações preenchidas pelo usuário e guarda em variáveis:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # verifica se nome de usuário já está registrado, buscando-o no banco de dados:
        user = User.objects.filter(username=username)

        # se o usuário já existir e/ou as senhas não coincidirem, mensagens de erro serão mostradas:
        if user.exists() and password1 != password2:
            messages.error(request, message='This username already exists')
            messages.error(
                request, message=form.error_messages['password_mismatch'])

            # e o usuário será redirecionado à página de registro:
            return redirect('/auth/register')

        if password1 != password2:
            messages.error(
                request, message=form.error_messages['password_mismatch'])

            return redirect('/auth/register')

        if user.exists():
            messages.error(request, message='This username already exists')

        try:
            # caso o usuário não exista, será criado um novo:
            user = User.objects.create_user(
                username=username, password=password2)
            user.save()
            messages.success(request, message='user created successfully.')

            # em seguida, o usuário será redirecionado para a página de login:
            return redirect('/auth/login')

        except:
            # se houver alguma exceção, o usuário será redirecionado novamente para a página de registro:
            return redirect('/auth/register')

    else:
        if request.user.is_authenticated:
            # se o usuário já estiver logado, ele será redirecionado para a página inicial:
            return redirect('/blog/')

        return render(request, 'register.html', {'form': form})
