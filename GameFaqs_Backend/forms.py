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
        widgets = {
            'password': forms.PasswordInput()
        }


class Add_FAQ(ModelForm):
    class Meta:
        model = models.Faq
        fields = ['name', 'body', 'game']
# Create message (for message board)


class Add_Message(ModelForm):
    class Meta:
        model = models.Message
        fields = ['title', 'body', 'game']


class EditUserForm(ModelForm):
    class Meta:
        model = models.GFUser
        fields = ['username', 'password', 'signature', 'website']


class QuestionForm(ModelForm):
    class Meta:
        model = models.Question 
        fields = ['game', 'question_title', 'question_body', 'spoiler']


class AnswerForm(ModelForm):
    class Meta:
        model = models.Answer
        fields = ['answer_body']