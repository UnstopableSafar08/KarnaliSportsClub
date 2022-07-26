from django.contrib import admin

# Register your models here.
from .models import ImageSlider
from .models import Slider
from .models import Member
from .models import ImgGall



admin.site.register(ImageSlider)
admin.site.register(Slider)
admin.site.register(Member)
admin.site.register(ImgGall)
