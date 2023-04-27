from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="resume-home"),
    path('create-basic/<str:tracking>',views.createBasic,name="create-basic"),
    path('create-work/<str:tracking>',views.createWork,name="create-work"),

    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),
    # path('',views.home,name="resume-home"),

]

#Before calling static
# urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
