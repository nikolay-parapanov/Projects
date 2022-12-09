from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from tri.authh.models import Profile

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    age = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    # gender = forms.ChoiceField()

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'age',)


    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )

        if commit:
            profile.save()

        return user


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
