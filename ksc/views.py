from math import ceil
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import ImageSlider
from .models import Slider

from ksc.models import ImageSlider, Slider 

# Create your views here.
def index(request):
    ImageSliders = ImageSlider.objects.all().order_by('-id')
    slide = Slider.objects.all().order_by('-id') #For slider at top of the page...
    print(ImageSliders)
    n = len(ImageSliders)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'ImageSlider': ImageSliders, 'Slider':slide}
    
    return render(request, 'ksc/index.html', params)

def about(request):
    return render(request, 'ksc/about.html')

def donate(request):
    return render(request, 'ksc/donate.html')

def contact(request):
    slide = Slider.objects.all()
    context = { 
               'Slider':slide
               }
    return render(request, 'ksc/contact.html', context)
