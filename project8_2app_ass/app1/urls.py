from django.urls import path

app_name='hi there'

from app1.views import *

urlpatterns=[
    path('index/',index,name='index'),
    path('index_1/',index_1,name='index_1')

]
