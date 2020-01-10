from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from GameFaqs_Backend import models, views


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    class Meta:
        model = models.GFUser
        fields = ['username', 'password']
# Register Form/Create Us
# Create FAQ


class Add_FAQ(ModelForm):
    class Meta:
        model = models.Faq
        fields = ['name', 'body', 'game']
# Create message (for message board)


class Add_Message(ModelForm):
    class Meta:
        model = models.Message
        fields = ['title', 'body']
        
