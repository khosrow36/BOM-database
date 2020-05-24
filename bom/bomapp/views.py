from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from .models import Product

class IndexView(generic.ListView):
    template_name = 'bomapp/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all
