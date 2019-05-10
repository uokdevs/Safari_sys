from django.http import HttpResponse
from django.shortcuts import render
import os
import json
from . import forms

json_file = open(os.path.join(os.getcwd(), 'Info.json'))
json_data = json.load(json_file)

dst = json_data['Destinations']
const = 'Matatu Booking| '

def handle_post(rqst,):
    form = forms.BookingForm(rqst)
# co-ordinate request and html responses
def home(request):
    '''
    handles empty request --> 'localhost/'
    :param request:
    :return:
    '''

    if request.method == 'POST':
        handle_post(request)

    return render(request, 'index.html', {
        'title': const+'Booking Home',
        'arr': dst,
    })


def FAQs(request):
    '''
    handles 'localhost/FAQ'
    :param request:
    :return:
    '''

    if request.method == 'POST':
        handle_post(request)

    return render(request, 'FAQ.html', {
        'title': const+'FAQ\'s',
        'arr': dst,
    })


def contact_us(request):
    '''
    handles 'localhost/contact_us'
    :param request:
    :return:
    '''

    if request.method == 'POST':
        handle_post(request)

    return render(request, 'contact-us.html', {
        'title': 'Contact-us',
        'arr': dst,
    })


def ret_fontawesome(request, doc_path=''):
    '''
    handles url --> localhost/wefonts/<path: docpath>/'
    for fontaweseome icons
    '''
    pathx = "webfonts/"+doc_path
    with open(pathx, 'rb') as f:
        data = f.read()

    return HttpResponse(data, content_type='application/font-woff2')
