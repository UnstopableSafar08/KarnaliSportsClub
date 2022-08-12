
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='KarnaliSportsClub Home'),
    path('about/', views.about, name='About us'),
    path('contact/', views.contact, name='About us'),
    path('donate/', views.donate, name='Donate'),
    path('blog/', views.blog, name='KSC-Blog'),
    path('event/', views.event, name='KSC-event'),
    path('postview/<int:id>', views.postview, name='KSC-Posts'),
 
]
