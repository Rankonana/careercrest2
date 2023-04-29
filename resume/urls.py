from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="resume-home"),
    path('create-basic/<str:tracking>',views.createBasic,name="create-basic"),
    path('list-work/<str:tracking>',views.listWork,name="list-work"),
    path('add-edit-work/<str:tracking>',views.addEditWork,name="add-edit-work"),

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
