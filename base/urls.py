from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('job/<str:pk>/',views.job,name="job"),
    path('category/',views.category,name="category"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('joblist/',views.joblist,name="joblist"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('notfound/',views.notfound,name="notfound"),
    
    path('our-services/',views.ourservices,name="our-services"),
    path('privacy-policy/',views.privacypolicy,name="privacy-policy"),
    path('terms-and-conditions/',views.termsandconditions,name="terms-and-conditions"),
    
    path('my_view/',views.my_view,name="my_view"),
]