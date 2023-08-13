from django.contrib import admin

# Register your models here.

from .models import Job,JobTypes,JobCategories, Post

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



admin.site.register(Job)
admin.site.register(JobTypes)
admin.site.register(JobCategories)


