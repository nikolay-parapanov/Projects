from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2','first_name','last_name', 'email','age', 'gender', 'profile_pic')
        field_classes = {'username': auth_forms.UsernameField}
