from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'inv/index.html')


def display_laptops(request):
    items = Laptops.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)
