from django.urls import path

app_name='there are'

from app2.views import *

urlpatterns=[
    path('index_app2/',index_app2,name='index_app2'),
    path('index_2/',index_ 2,name='index_2')
]