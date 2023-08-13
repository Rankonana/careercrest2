from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from . sitemaps import JobSitemap,StaticSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
		"jobs": JobSitemap,
        'static': StaticSitemap
}

urlpatterns = [
    path('',views.home,name="home"),
    path('job/<int:id>/<str:title>/',views.job,name="job"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('joblist/',views.joblist,name="joblist"),
    path('testimonial/',views.testimonial,name="testimonial"),
    path('notfound/',views.notfound,name="notfound"),
    
    path('our-services/',views.ourservices,name="our-services"),
    path('privacy-policy/',views.privacypolicy,name="privacy-policy"),
    path('terms-and-conditions/',views.termsandconditions,name="terms-and-conditions"),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
						name='django.contrib.sitemaps.views.sitemap'),
    path('ads.txt', views.ads_txt, name='ads_txt'),
    path('notfound/', views.notfound, name='notfound'),

    
    path('xxx/<int:page>/',views.xxx,name="xxx"),
    path("terms.json",views.listing_api,name="terms-api"),
    path('loadmore/',views.loadmore,name="loadmore"),

    path('post-a-job/',views.post_job,name="post-a-job"),





]

#Before calling static
# urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
