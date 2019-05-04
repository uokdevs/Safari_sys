from django.http import HttpResponse
from django.shortcuts import render


# co-ordinate request and html response
def home(request):
    return render(request, 'index.html')


def FAQs(request):
    return render(request, 'FAQ.html')


def contact_us(request):
    return render(request, 'contact-us.html')