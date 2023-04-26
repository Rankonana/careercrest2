from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    body=RichTextUploadingField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='featured_image/%Y/%m/%d/', blank=True, null=True) #this

    
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    def __str__(self):
        return self.title
     
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.id,self.title.replace(" ", "-").replace("/", "-").replace("\\", "-").lower()])
 