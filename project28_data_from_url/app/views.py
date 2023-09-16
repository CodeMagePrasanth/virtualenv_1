from django.shortcuts import render

from django.http import HttpResponse

def data_from_url(request,name):
    return HttpResponse(f'hai {name}')