from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('blog/',include('blog.urls')),

    path('resume/',include('resume.urls')),
    path('api/',include('resume.api.urls')),


]

