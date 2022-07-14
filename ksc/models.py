from pyexpat import model
from django.db import models

# Create your models here.
class ImageSlider(models.Model):
    Image_id = models.AutoField
    Image_Name = models.CharField(max_length=80)
    Image_Desc = models.CharField(max_length=800)
    ImagePub_date= models.DateField()
    Image = models.ImageField(upload_to="ksc/images", default="")
    
    def __str__(self):
        return self.Image_Name 