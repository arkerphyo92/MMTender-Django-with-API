from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=False,max_length=255)
    website = forms.CharField(required=False,max_length=55)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2","address","website"]
        labels = {
            "username": "Username",
            "email": "Email",
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "password1": "Password",
            "password2": "Repeat Password",
            "address": "Address",
            "website" : "Website",
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Email'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Last Name'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Repeat Same Password'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Your Address'})
        self.fields['website'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Your Website'})

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username' : 'Username',
            'password' : 'Password',
            }
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter Password'})