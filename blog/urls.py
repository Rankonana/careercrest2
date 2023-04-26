from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from . sitemaps import  PostSitemap


sitemaps = {
        "posts": PostSitemap
}
urlpatterns = [
    path('',views.post_list,name="post_list"),
    path('blog/<int:id>/<str:title>/',views.post_detail,name="post_detail"),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
	# 					name='django.contrib.sitemaps.views.sitemap'),
]

#Before calling static
# urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
