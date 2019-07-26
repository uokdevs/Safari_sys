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
        resultset = models.BusData.objects.filter(route_id=route_id, date=date, seats_left__gt=0).values().order_by('depature')

        return render(request, 'booking.html', {
            'resultset': resultset,
            'title': 'MatTrans | Booking'
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
                departure_time = mod.depature
                departure_date = mod.date
                time_booked = dt.datetime.now().time()
                date_booked = dt.date.today()
                inst = models.Booked(date_booked=date_booked, time_booked=time_booked, owner=authinfo_object,
                                     str_route=route, transaction_id=form.data.get('code').upper(),
                                     departure_date=departure_date, departure_time=departure_time)
                inst.save()

                return redirect('/')

        paybill = 29076545
        return render(request, 'payment.html', {
            'price': '500',
            "paybill": paybill,
            'title': 'MatTrans | Payment'
        })

    else:
        return redirect('/login')
