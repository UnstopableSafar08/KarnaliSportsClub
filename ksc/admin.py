from django.contrib import admin

# Register your models here.
from .models import ImageSlider
from .models import Slider

admin.site.register(ImageSlider)
admin.site.register(Slider)