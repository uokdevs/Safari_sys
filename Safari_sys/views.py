from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import os
import json
from . import forms, models
from django.contrib.auth.hashers import make_password, check_password
from django.db.utils import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


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


def ret_static(request, dir=''):
    try:
        pathx = 'static/css/'+dir
        with open(pathx, 'r+') as f:
            data = f.read()
        return HttpResponse(data, content_type='text/css')
    except FileNotFoundError:
        try:
            pathx = 'static/js/'+dir
            with open(pathx, "r+") as f:
                data = f.read()
            return HttpResponse(data, content_type='application/javascript')
        except FileNotFoundError:
            ftype = dir.split('.')[-1]
            if ftype in ('jpg', 'jpeg'):
                content = 'image,jpeg'
            elif ftype == 'png':
                content = 'image/png'
            elif ftype == 'ico':
                content = 'image,x-icon'
            try:
                pathx = 'static/img/'+dir
                with open(pathx, 'rb') as f:
                    data = f.read()

                return HttpResponse(data, content_type=content)
            except FileNotFoundError:
                return HttpResponseNotFound()


def sign_up(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        form1 = forms.signupAuth(request.POST)

        if form.is_valid() and form1.is_valid():
            user = form1.save(commit=False)
            user1 = form.save(commit=False)

            # hash the plain text password
            hashed = make_password(form.cleaned_data.get('password'))
            user.password = hashed
            user1.password = hashed

            user.save()
            user1.save()

            login(request, user)
            return redirect('home')

    return render(request, 'signup.html')


def log_in(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=raw_password)
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('home')
