from django.shortcuts import render
from .models import *


# index/home view
def index(request):
    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'index.html', context=context)

# about view
def about(request):
    return render(request, 'about.html')