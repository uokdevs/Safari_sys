from django import forms


class Payment(forms.Form):
    code = forms.CharField(max_length=100, required=True)
