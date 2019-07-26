from django.urls import path
from . import views

urlpatterns = [
    path(r'myaccount', views.myaccount)
]