from csv import reader
import datetime
from email import message
from email.policy import default
from pickle import TRUE
from pyexpat import model
from sqlite3 import Date, Time, Timestamp
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

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


#class for blogPosts 
class blogPost(models.Model):
    sno=models.AutoField(primary_key=True)
    author=models.CharField(max_length=50, default="KSC")
    slug=models.CharField(max_length=130, null=False, unique= True)
    timeStamp=models.DateTimeField(auto_now_add=True)
    
    blogPostName = models.CharField(max_length=150, default="Enter Blog Title Here")
    blog_post_desc = models.TextField(max_length=1000, default="Blog Post's Desc only show in Blog page, It does not shown in Blog post View page")
    content = RichTextUploadingField()
    
    #image Upload
    thumbnail = models.ImageField(upload_to="ksc/blogImage", default="" )
    
    
    def __str__(self):
        return self.blogPostName + "- - - by - - - >>> " + self.author
       
#class Event Post 
class eventPost(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=80, default="Enter Event Name here")
    slug=models.CharField(max_length=130, null=False, unique=True)
    eventCategory = models.CharField(max_length=50, default="Enter Event Category here")
    #eventH1 = models.CharField(max_length=80, default="Enter Event Heading1 here")
    event_post_desc = models.TextField(max_length=1000, default="Event Post Desc only for Event page, It does not shown in Event View page")
    content = RichTextUploadingField()
    eventDateFrom = models.DateField(default="")
    eventDateTo = models.DateField(default="")
    
    #image Upload
    thumbnail = models.ImageField(upload_to="ksc/blogImage", default="" )
    
    def __str__(self):
        return self.eventName

#class Testinomials 
class Testimonial(models.Model): 
    testId=models.AutoField
    name = models.CharField(max_length=80, default="Enter Person Name here")
    title = models.CharField(max_length=80, default="Enter Person's Postion/working Area")
    desc = models.CharField(max_length=1000, default="Enter desc of person")
    img = models.ImageField(upload_to= "ksc/testimonialsImage", default="")
    
    def __str__(self):
        return self.name + " - - - - - - " + self.title
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=500, default="")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)


    def __str__(self):
        return f'{self.name} ---> at --- > {self.date} --- > {self.time}'