from math import ceil
from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import ImageSlider, Member, blogPost, Testimonial, eventPost
from .models import Slider

from ksc.models import ImageSlider, Slider ,ImgGall

# Create your views here.
def index(request):
    ImageSliders = ImageSlider.objects.all().order_by('-id')
    gall = ImgGall.objects.all().order_by('-id')[0:12]
    slide = Slider.objects.all().order_by('-id') #For slider at top of the page...
    testm = Testimonial.objects.all()
    n = len(ImageSliders)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'ImageSlider': ImageSliders, 'Slider':slide, 'ImgGall':gall, 'testm':testm}
    
    return render(request, 'ksc/index.html', params)

def about(request):
    mem = Member.objects.all()
    context = {
        'Member':mem
    }
    return render(request, 'ksc/about.html', context)

def donate(request):
    return render(request, 'ksc/donate.html')

def contact(request):
    slide = Slider.objects.all()
    context = { 
               'Slider':slide
               }
    return render(request, 'ksc/contact.html', context)

def blog(request):
    allPosts = blogPost.objects.all()
    context = { 
               'Post':allPosts
               }
    return render(request, 'ksc/blog.html', context)

def postview(request, slug):
    post=blogPost.objects.filter(slug=slug)[0]
    return render(request, 'ksc/postview.html', {'post':post}) 

    
def event(request):
    evpost = eventPost.objects.all()
    context={
        'evpost':evpost
    }
    return render(request, 'ksc/event.html', context)

def eventview(request, slug):
    post=eventPost.objects.filter(slug=slug)[0]
    return render(request, 'ksc/eventview.html', {'post':post}) 

def test(request):
    slide = Slider.objects.all()
    testm = Testimonial.objects.all()
    return render(request,'ksc/test.html', {'slide':slide, 'testm':testm})

def testimonials(request):
    testm = Testimonial.objects.all()
    return render(request,'ksc/test.html', {'testm':testm}) 