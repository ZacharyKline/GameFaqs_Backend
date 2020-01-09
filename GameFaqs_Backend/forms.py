from django import forms
from GameFaqs_Backend.models import GFUser

# Login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)


# Register Form/Create User
class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = GFUser
        fields = ['username', 'password']


# Create FAQ

# Create message (for message board)
