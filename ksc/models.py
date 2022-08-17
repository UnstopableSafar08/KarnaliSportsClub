from csv import reader
from email import message
from email.policy import default
from pyexpat import model
from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class ImageSlider(models.Model):
    Image_id = models.AutoField
    Image_Name = models.CharField(max_length=80)
    Image_Desc = models.CharField(max_length=800)
    ImagePub_date= models.DateField(auto_now_add=True)
    Image = models.ImageField(upload_to="ksc/images", default="")
    
    def __str__(self):
        return self.Image_Name 
    
class Slider(models.Model):
    id = models.AutoField
    name=models.CharField(max_length=50, default="")
    date = models.DateField( default="")
    img = models.ImageField(upload_to="ksc/images", default="")
    
    def __str__(self):
        return self.name
    
class ImgGall(models.Model):
    id=models.AutoField
    imgName = models.CharField(max_length=50)
    altTxt = models.CharField(max_length=50)
    gallImg = models.ImageField(upload_to="ksc/gallery")
    def __str__(self):
        return self.imgName
class Member(models.Model):
    memberId=models.AutoField
    memberName = models.CharField(max_length=50, default="")
    memberPosition=models.CharField(max_length=50, default="")
    memberImg = models.ImageField(upload_to="ksc/images", default="")
    
    def __str__(self):
        return self.memberName + '   < - - - >   ' + self.memberPosition

class Contact(models.Model):
    msgId = models.AutoField
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    message = models.TextField(max_length=300)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class blogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130, null=False, unique= True)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField()
    thumbnail = models.ImageField(upload_to="ksc/postImage", default="" )

    def __str__(self):
        return self.title + " by " + self.author
    
class Testimonial(models.Model): 
    testId=models.AutoField
    name = models.CharField(max_length=80, default="Enter Person Name here")
    title = models.CharField(max_length=80, default="Enter Person's Postion/working Area")
    desc = models.CharField(max_length=1000, default="Enter desc of person")
    img = models.ImageField(upload_to= "ksc/testimonialsImage", default="")
    
    def __str__(self):
        return self.name + " - - - - - - " + self.title
    
    
class eventPost(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=80, default="Enter Event Name here")
    eventCategory = models.CharField(max_length=50, default="Enter Event Category here")
    eventH1 = models.CharField(max_length=80, default="Enter Event Heading1 here")
    eventDesc1 = models.TextField(max_length=2000, default="Enter Event Description here")
    eventH2 = models.CharField(max_length=80, default="")
    eventDesc2 = models.TextField(max_length=2000, default="")
    eventH3 = models.CharField(max_length=80, default="")
    eventDesc3 = models.TextField(max_length=2000, default="")
    eventDateFrom = models.DateField(default="")
    eventDateTo = models.DateField(default="")
    eventImg1 = models.ImageField(upload_to="ksc/eventImages", default="")
    eventImg2 = models.ImageField(upload_to="ksc/eventImages", default="")
    eventImg3 = models.ImageField(upload_to="ksc/eventImages", default="")
     
    def __str__(self):
        return self.eventName