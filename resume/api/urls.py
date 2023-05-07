from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('softwares/', views.getSoftwares),
    path('softwares/<str:pk>/', views.getSoftware),
    path('add-edit-software/<str:softwaretracking>/', views.software_detail),


]