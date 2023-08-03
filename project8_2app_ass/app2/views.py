from django.shortcuts import render

# Create your views here.
def index_app2(request):
    return render(request,'index_app2.html')

def index_2(request):
    return render(request,'index2.html')