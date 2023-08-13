from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.contrib.auth.models import User

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
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    location  = models.CharField(max_length=200,null=True,blank=True)
    salary  = models.CharField(max_length=200,null=True,blank=True)
    jobType  =  models.ForeignKey(JobTypes,on_delete=models.SET_NULL,null=True,blank=False)
    jobCategory  =  models.ForeignKey(JobCategories,on_delete=models.SET_NULL,null=True,blank=False)
    featuredListing  = models.BooleanField(null=True,blank=True)
    importantInformation  = models.CharField(max_length=200,null=True,blank=True)
    expiryDate  = models.DateField(null=True, blank=True)
    applicationLinkOrEmail  = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    companyname = models.CharField(max_length=200)
    seodescription = models.TextField(null=True, blank=True)
    companylogo = models.ImageField(null=True,blank=True,default="logo.png")
    companylogoexternal = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-updated','-created']
    def __str__(self) :
        return self.title
    
    def get_absolute_url(self):
        return reverse("job",
                            args=[self.id,self.title.replace(" ", "-").replace("/", "-").replace("\\", "-").lower()])

class JobApplication(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"
    
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
 