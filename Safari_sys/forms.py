from django import forms


class BookingForm(forms.Form):
    geo_from = forms.CharField(label='from', max_length=100)
    geo_destination = forms.CharField(label='destination', max_length=100)


class LoginForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())