from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from GameFaqs_Backend import models, views 


# Login form

# Register Form/Create Us
# Create FAQ
class Add_FAQ(ModelForm):
    class Meta:
        model = Faq
        fields = ['name', 'body']
# Create message (for message board)
class Add_Message(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'body']