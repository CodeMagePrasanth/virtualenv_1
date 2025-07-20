from django.shortcuts import render

from app.forms import *
from django.http import HttpResponse

def registration(request):
    USDO = UserForm()
    PSDO = ProfileForm()
    d={'USDO':USDO,'PSDO':PSDO}

    if request.method =='POST' and request.FILES:
        UFDO= UserForm(request.POST)
        PFDO= ProfileForm(request.POST,request.FILES)

        if UFDO.is_vaild() and PFDO.is_vaild():
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(UFDO.cleaned_data['password'])
            MUFDO.save()

            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('registr successfully')
        # from django.core.mail
        # send_mail('subject','message','sendermail',[reciver's email'],fail.sliently=false or true)
    return render(request,'registration.html',d)

def dummy(request):
    return render(request,'dummy.html')

# def user_login()

# def change_password(request):
#     if request.method=='POST':
#         username=request.seesion.get('username')
#         password=request.session.get('password')
#         UO=User.objects.get(username=username)

#         UO.set_password(password)
#         UO.save()
#         return HttpResponse('change the password successfully')
#     return render(request,'change_password.html')


# def forget_password(request):
#     if request.method=='POST':
#         username=request.