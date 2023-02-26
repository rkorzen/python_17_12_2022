from django import forms
from .models import UserProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
