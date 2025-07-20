from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def htmlforms(request):
    if request.method == 'POST': # this is for checking POST method are Active state or not
     
     return HttpResponse('data is get it') # just return one response

    return render(request,'htmlforms.html')