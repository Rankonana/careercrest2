from django.contrib import admin

# Register your models here.

from .models import Job,JobTypes,JobCategories, Post


admin.site.register(Job)
admin.site.register(JobTypes)
admin.site.register(JobCategories)


