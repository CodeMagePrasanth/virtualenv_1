from django.shortcuts import render

from django.views.generic import TemplateView


class Temp(TemplateView):
    template_name='Temp.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='preeti'
        ECDO['SFO']=