from django import forms
from . import models
from django.contrib.auth.models import User

# class BookingForm(forms.Form):
#     geo_from = forms.CharField(label='from', max_length=100)
#     geo_destination = forms.CharField(label='destination', max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    remember = forms.BooleanField()


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

