

from django.shortcuts import render, redirect
from webapp.models import Product

def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)