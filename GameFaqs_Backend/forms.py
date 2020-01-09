from django import forms
from django.forms import ModelForm
from GameFaqs_Backend import models


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
        fields = ['name', 'body']
# Create message (for message board)


class Add_Message(ModelForm):
    class Meta:
        model = models.Message
        fields = ['title', 'body']
