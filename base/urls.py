from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('job/<str:pk>/',views.job,name="job"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('joblist/',views.joblist,name="joblist"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('notfound/',views.notfound,name="notfound"),
    
    path('our-services/',views.ourservices,name="our-services"),
    path('privacy-policy/',views.privacypolicy,name="privacy-policy"),
    path('terms-and-conditions/',views.termsandconditions,name="terms-and-conditions"),
    
    path('xxx/<int:page>/',views.xxx,name="xxx"),
    path("terms.json",views.listing_api,name="terms-api"),
    path('loadmore/',views.loadmore,name="loadmore"),



]