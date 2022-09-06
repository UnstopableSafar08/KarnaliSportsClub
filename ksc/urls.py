
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='KarnaliSportsClub Home'),
    path('about/', views.about, name='About us'),
    path('contact/', views.contact, name='About us'),
    path('donate/', views.donate, name='Donate'),
    
    path('blog/', views.blog, name='KSC-Blog'),
    path('postview/<str:slug>', views.postview, name='KSC-Posts'),
    
    path('event/', views.event, name='KSC-event'),
    path('eventview/<str:slug>', views.eventview, name='KSC-Event Post'),
    
    path('testimonials/', views.testimonials, name='KSC-Testimonials'),
    path('test/', views.test, name='KSC-test'),
]
