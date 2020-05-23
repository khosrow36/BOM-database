from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from .models import BOM

class IndexView(generic.ListView):
    template_name = 'bomapp/index.html'
    context_object_name = 'bom_list'

    def get_queryset(self):
        return BOM.objects.all
