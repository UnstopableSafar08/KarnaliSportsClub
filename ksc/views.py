from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ksc/index.html')

def about(request):
    return render(request, 'ksc/about.html')

def contact(request):
    return render(request, 'ksc/contact.html')
