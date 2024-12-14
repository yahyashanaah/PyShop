from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .models import Product, Offer
# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse("this is the students index page")


