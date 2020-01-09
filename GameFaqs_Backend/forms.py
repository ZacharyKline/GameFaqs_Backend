from django import forms
from GameFaqs_Backend.models import GFUser
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    class Meta:
        model = GFUser
        fields = ['username', 'password']
