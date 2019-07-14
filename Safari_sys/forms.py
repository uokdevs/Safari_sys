from django import forms


# class BookingForm(forms.Form):
#     geo_from = forms.CharField(label='from', max_length=100)
#     geo_destination = forms.CharField(label='destination', max_length=100)


class LoginForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    u_name = forms.CharField(max_length=100)
    p_code = forms.CharField(widget=forms.PasswordInput())
    mail = forms.EmailField(max_length=100)
    f_name = forms.CharField( max_length=100)
    l_name = forms.CharField( max_length=100)

