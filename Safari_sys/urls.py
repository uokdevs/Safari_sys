"""Safari_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path(r'', views.home, name='home'),
    path(r'FAQ', views.FAQs, name='FAQ'),
    path(r'index', views.home, name='index'),
    path(r'contact_us', views.contact_us, name='contact_us'),
    path(r'webfonts/<path:doc_path>', views.ret_fontawesome),
    path(r'static/<str:dir>', views.ret_static),
    path(r'booking/', include('booking.urls')),
    path(r'Sign-up', views.sign_up, name='sign-up'),
    path(r'login', views.log_in, name='login'),

]
