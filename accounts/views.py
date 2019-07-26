from django.shortcuts import render
from django.http import HttpResponseRedirect
from booking.models import Booked
# Create your views here.

def myaccount(request):
    if request.user.is_authenticated:
        username = request.user.username
        queryset = Booked.objects.filter(owner__username=username).values()
        return render(request, 'accounts/accounts.html', {
            'title': 'Mat | My Account',
            'rows': queryset
        })

    else:
        return HttpResponseRedirect('/login')