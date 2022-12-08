from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    age = forms.IntegerField
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {"username": UsernameField}


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class SignUpView(CreateView):
    template_name = 'authh/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('sign up')


class SignInView(LoginView):
    template_name = 'authh/sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(LogoutView):
    template_name = 'authh/sign-out.html'
