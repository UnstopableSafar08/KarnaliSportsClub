from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import ImageSlider
from ksc.models import ImageSlider

# Create your views here.
def index(request):
    return render(request, 'ksc/index.html')

def about(request):
    return render(request, 'ksc/about.html')

def contact(request):
    return render(request, 'ksc/contact.html')
