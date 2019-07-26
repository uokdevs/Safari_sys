from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
import os
import json
from . import forms
from booking import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout
import datetime as dt


json_file = open(os.path.join(os.getcwd(), 'Info.json'))
json_data = json.load(json_file)

dst = json_data['Destinations']
const = 'Matatu Booking | '


def available_destinations():
    routes = json_data['routes']
    arr = []

    for a in routes:
        b = routes[a]

        temp = [a, '-->']
        for x in b:
            temp.append(x)

        temp = str(temp)
        arr.append(temp)

    return arr

# co-ordinate request and html responses
def home(request):
    '''
    handles empty request --> 'localhost/'
    :param request:
    :return:
    '''

    if request.method == 'POST':
        form = forms.BookingForm(request.POST)

        if form.is_valid():
            fro = form.data.get('fro')
            to = form.data.get('to')
            datestr = [int(x) for x in (form.data.get('date').split('-'))]
            date = dt.date(datestr[0], datestr[1], datestr[2])

            to_exists = True
            try:
                route_id = json_data['routes'][fro.lower()][to.lower()]
            except KeyError:
                to_exists = False

            if fro.lower() not in json_data['Destinations'] or not to_exists:
                errors = [f'The route enter does not exist {fro.title()} --> {to.title()}', 'Available Routes']
                errors += available_destinations()
                return render(request, 'errors.html', {
                    'errors': errors,
                    'title': 'Error!'
                })

            if date < dt.date.today():
                return render(request, 'errors.html', {
                    'errors': ['Error: Invalid date. Date should be greater than or equal to today'],
                    'title': 'Error!'
                })

            return HttpResponseRedirect(f'/booking/{fro}-{to}-{route_id}&date={date}')

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
        pass

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
        pass

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
        else:
            return render(request, 'signup.html', {
                'title': const+'Sign UP',
                'errors': form.errors,
                'email': form.data.get('email'),
                'username': form.data.get('username'),
                'f_name': form.data.get('first_name'),
                'l_name': form.data.get('last_name'),
            })

    return render(request, 'signup.html', {
        'title': const + 'Sign Up',
        'errors': None
    })


def log_in(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            uname = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=raw_password)

            try:
                login(request, user)
            except AttributeError:

                return render(request, 'login.html', {
                    'title': const + ' Login',
                    'invalid': True,
                    'username': form.data.get('username'),
                })
            return redirect('home')

    return render(request, 'login.html', {
        'title': const + ' Login',
        'invalid': False
    })


def log_out(request):
    logout(request)
    return redirect('home')


