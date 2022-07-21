from math import ceil
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .models import ImageSlider
from ksc.models import ImageSlider

# Create your views here.
def index(request):
    ImageSliders = ImageSlider.objects.all().order_by('-id')
    print(ImageSliders)
    n = len(ImageSliders)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'ImageSlider': ImageSliders}
    return render(request, 'ksc/index.html', params)

def about(request):
    return render(request, 'ksc/about.html')

def contact(request):
    return render(request, 'ksc/contact.html')
