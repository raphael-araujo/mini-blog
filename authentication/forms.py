from django.contrib.auth import forms


class LoginForm(forms.AuthenticationForm):
    """Formulário para ser utilizado na página de login"""
    ...


class RegisterForm(forms.UserCreationForm):
    """Formulário para ser utilizado na página de cadastro"""
    ...
