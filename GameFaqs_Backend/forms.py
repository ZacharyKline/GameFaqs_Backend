from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import User
from GameFaqs_Backend import models


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    class Meta:
        model = models.GFUser
        fields = ['username', 'password']


class Add_FAQ(ModelForm):
    class Meta:
        model = models.Faq
        fields = ['name', 'body']


class Add_Message(ModelForm):
    class Meta:
        model = models.Message
        fields = ['title', 'body']
