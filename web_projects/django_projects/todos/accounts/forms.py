from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()


class UserProfileForm(forms.ModelForm):

    helper = FormHelper()
    helper.add_input(Submit("submit", "Submit", css_class="btn-primary"))

    class Meta:
        model = UserProfile

        fields = [
            "user",
            "description",
            "picture",
        ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
