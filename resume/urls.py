from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="resume-home"),
    path('create-basic/<str:tracking>',views.createBasic,name="create-basic"),

    path('create-summary/<str:tracking>',views.createSummary,name="create-summary"),

    path('list-work/<str:tracking>',views.listWork,name="list-work"),
    path('addeditwork/<str:tracking>/<str:worktracking>',views.addEditWork,name="addeditwork"),
    path('deletework/<str:tracking>/<str:worktracking>',views.deleteWork,name="deletework"),

    path('list-edu/<str:tracking>',views.listEdu,name="list-edu"),
    path('addeditedu/<str:tracking>/<str:edutracking>',views.addEditEdu,name="addeditedu"),
    path('deleteedu/<str:tracking>/<str:edutracking>',views.deleteEdu,name="deleteedu"),





]

#Before calling static
# urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
