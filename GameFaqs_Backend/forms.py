from django import forms
from django.forms import ModelForm
<<<<<<< HEAD
from django.contrib.auth.models import User
from GameFaqs_Backend import models, views
 
=======
from GameFaqs_Backend import models
>>>>>>> 763e8d0669a705e00793ba6705565087d4a0499d


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
<<<<<<< HEAD
        fields = ['title', 'body']
=======
        fields = ['title', 'body']
>>>>>>> 763e8d0669a705e00793ba6705565087d4a0499d
