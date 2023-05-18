from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('work-job-title/<str:search_query>/', views.getworkJobtitle),
    path('work-job-title-related/<str:search_query>/', views.getworkJobtitle),

    path('work-job-description/<str:search_query>/', views.getworkJobdescription),

    path('softwares/', views.getSoftwares),
    path('softwares/<str:pk>/', views.getSoftware),
    path('add-edit-software/', views.software_detail),
    path('delete-software/<str:softwaretracking>/', views.deleteSoftware),

    path('languages/', views.getLanguages),
    path('languages/<str:pk>/', views.getLanguage),
    path('add-edit-language/', views.language_detail),
    path('delete-language/<str:languagetracking>/', views.deleteLanguage),

    path('certifications/', views.getCertifications),
    path('certifications/<str:pk>/', views.getCertification),
    path('add-edit-certification/', views.certification_detail),
    path('delete-certification/<str:certificationtracking>/', views.deleteCertification),

    path('image/<str:tracking>/', views.getImage),
    path('image-delete/<str:tracking>/', views.deleteImage),
    path('add-edit-resume/', views.add_or_update_resume),

    path('socials/', views.getSocialLinks),
    path('socials/<str:pk>/', views.getSocialLink),
    path('add-edit-social/', views.socialLink_detail),
    path('delete-social/<str:socialtracking>/', views.deleteSocialLink),

    path('skills/', views.getSkills),
    path('skills/<str:pk>/', views.getSkill),
    path('add-edit-skill/', views.skill_detail),
    path('delete-skill/<str:skilltracking>/', views.deleteSkill),






]