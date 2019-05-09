from django.http import HttpResponse
from django.shortcuts import render


# co-ordinate request and html response
def home(request):
    '''
    handles empty request --> 'localhost/'
    :param request:
    :return:
    '''
    return render(request, 'index.html')


def FAQs(request):
    '''
    handles 'localhost/FAQ'
    :param request:
    :return:
    '''
    return render(request, 'FAQ.html')


def contact_us(request):
    '''
    handles 'localhost/contact_us'
    :param request:
    :return:
    '''
    return render(request, 'contact-us.html')


def ret_fontawesome(request, doc_path=''):
    '''
    handles url --> localhost/wefonts/<path: docpath>/'
    for fontaweseome icons
    '''
    pathx = "webfonts/"+doc_path
    with open(pathx, 'rb') as f:
        data = f.read()

    return HttpResponse(data, content_type='application/font-woff2')
