from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
import time


# Create your models here.

class JobTypes(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class JobCategories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    location  = models.CharField(max_length=200,null=True,blank=True)
    salary  = models.CharField(max_length=200,null=True,blank=True)
    remotePosition  = models.BooleanField(null=True,blank=True)
    jobType  =  models.ForeignKey(JobTypes,on_delete=models.SET_NULL,null=True,blank=True)
    jobCategory  =  models.ManyToManyField(JobCategories,null=True,blank=True)
    positionFilled  = models.BooleanField(null=True,blank=True)
    featuredListing  = models.BooleanField(null=True,blank=True)
    importantInformation  = models.CharField(max_length=200,null=True,blank=True)
    expiryDate  = models.DateField(null=True, blank=True)
    applicationLinkOrEmail  = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    companyname = models.CharField(max_length=200)
    companylogo = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ['-updated','-created']
    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse("job",
                            args=[self.id])

