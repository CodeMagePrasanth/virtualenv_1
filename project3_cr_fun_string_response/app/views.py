from django.shortcuts import render
from django.http import HttpResponse

def string1_response(request):
    return HttpResponse('<marquee><h1>This is my first String respose</h1></marquee>')
