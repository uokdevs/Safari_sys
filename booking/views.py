from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from . import models, forms
import datetime as dt
from Safari_sys.models import AuthInfo
# Create your views here.


def dummy(request):
    return HttpResponse('Success trial')


def show_available_buses(request, fro='', dst='', route_id=-1, year='', month='', day=''):
    if request.user.is_authenticated:
        route_id = int(route_id)
        date = dt.date(year, month, day)
        resultset = models.BusData.objects.filter(route_id=route_id, date=date).values().order_by('depature')

        return render(request, 'booking.html', {
            'resultset': resultset
        })
    else:
        return redirect('/login')


def book(request, id=''):

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = forms.Payment(request.POST)

            if form.is_valid():
                route = (models.BusData.objects.filter(id=id).values())[0]['str_route']

                mod = models.BusData.objects.filter(id=id)[0]
                mod.seats_left -= 1
                mod.save()

                # print(route)
                # print(id, type(id))
                # raise ImportError
                authinfo_object = AuthInfo.objects.filter(username=request.user.username)[0]
                time = dt.datetime.now().time()
                date = dt.date.today()
                inst = models.Booked(date_booked=date, time_booked=time, owner=authinfo_object, str_route=route)
                inst.save()

                return redirect('/')

        paybill = 29076545
        return render(request, 'payment.html', {
            'price': '500',
            "paybill": paybill,
        })

    else:
        return redirect('/login')
