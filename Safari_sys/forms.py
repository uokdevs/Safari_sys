from django import forms
from . import models
from django.contrib.auth.models import User


class BookingForm(forms.Form):
    fro = forms.CharField(max_length=100)
    to = forms.CharField(max_length=100)
    date = forms.DateField(widget=forms.DateInput())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    remember = forms.BooleanField(required=False)


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = models.AuthInfo
        fields = ['username', 'password', 'last_name', 'first_name', 'email']


class signupAuth(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput())
    email = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

