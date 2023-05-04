from django.urls import path, include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="resume-home"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerPage,name="register"),
    path('account/',views.myAccount,name="account"),


    path('create-basic/<str:tracking>',views.createBasic,name="create-basic"),

    path('create-summary/<str:tracking>',views.createSummary,name="create-summary"),

    path('list-social/<str:tracking>',views.listSocial,name="list-social"),
    path('add-edit-social/<str:tracking>/<str:socialtracking>',views.addeditSocial,name="addeditSocial"),
    path('delete-social/<str:tracking>/<str:socialtracking>',views.deleteSocial,name="deletesocial"),


    path('list-work/<str:tracking>',views.listWork,name="list-work"),
    path('add-edit-work/<str:tracking>/<str:worktracking>',views.addEditWork,name="addeditwork"),
    path('delete-work/<str:tracking>/<str:worktracking>',views.deleteWork,name="deletework"),

    path('list-edu/<str:tracking>',views.listEdu,name="list-edu"),
    path('add-edit-edu/<str:tracking>/<str:edutracking>',views.addEditEdu,name="addeditedu"),
    path('delete-edu/<str:tracking>/<str:edutracking>',views.deleteEdu,name="deleteedu"),

    path('list-skill/<str:tracking>',views.listSkill,name="list-skill"),
    path('add-edit-skill/<str:tracking>/<str:skilltracking>',views.addeditSkill,name="addeditSkill"),
    path('delete-skill/<str:tracking>/<str:skilltracking>',views.deleteSkill,name="deleteskill"),


    path('list-language/<str:tracking>',views.listLanguage,name="list-language"),
    path('add-edit-language/<str:tracking>/<str:languagetracking>',views.addeditLanguage,name="addeditLanguage"),
    path('delete-language/<str:tracking>/<str:languagetracking>',views.deleteLanguage,name="deletelanguage"),

    path('list-interest/<str:tracking>',views.listInterest,name="list-interest"),
    path('add-edit-interest/<str:tracking>/<str:interesttracking>',views.addeditInterest,name="addeditInterest"),
    path('delete-interest/<str:tracking>/<str:interesttracking>',views.deleteInterest,name="deleteinterest"),

    path('list-accomplishment/<str:tracking>',views.listAccomplishment,name="list-accomplishment"),
    path('add-edit-accomplishment/<str:tracking>/<str:accomplishmenttracking>',views.addeditAccomplishment,name="addeditAccomplishment"),
    path('delete-accomplishment/<str:tracking>/<str:accomplishmenttracking>',views.deleteAccomplishment,name="deleteaccomplishment"),

    path('list-affiliation/<str:tracking>',views.listAffiliation,name="list-affiliation"),
    path('add-edit-affiliation/<str:tracking>/<str:affiliationtracking>',views.addeditAffiliation,name="addeditAffiliation"),
    path('delete-affiliation/<str:tracking>/<str:affiliationtracking>',views.deleteAffiliation,name="deleteaffiliation"),

    path('list-additional-info/<str:tracking>',views.listAdd,name="list-add"),
    path('add-edit-additional-info/<str:tracking>/<str:additionalinfotracking>',views.addeditAdd,name="addeditAdd"),
    path('delete-additional-info/<str:tracking>/<str:additionalinfotracking>',views.deleteAdd,name="deleteadd"),

    path('list-software/<str:tracking>',views.listSoftware,name="list-software"),
    path('add-edit-software/<str:tracking>/<str:softwaretracking>',views.addeditSoftware,name="addeditSoftware"),
    path('delete-software/<str:tracking>/<str:softwaretracking>',views.deleteSoftware,name="deletesoftware"),

    path('list-certification/<str:tracking>',views.listCertification,name="list-cert"),
    path('add-edit-certification/<str:tracking>/<str:certificationtracking>',views.addeditCertification,name="addeditCert"),
    path('delete-certification/<str:tracking>/<str:certificationtracking>',views.deleteCertification,name="deletecert"),

    path('list-yourown/<str:tracking>',views.listYourown,name="list-yourown"),
    path('add-edit-yourown/<str:tracking>/<str:yourowntracking>',views.addeditYourown,name="addeditYourown"),
    path('delete-yourown/<str:tracking>/<str:yourowntracking>',views.deleteYourown,name="deleteyourown"),


]

#Before calling static
# urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
