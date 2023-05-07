from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.shortcuts import render, redirect
from .models import * 
from django.db.models import Q
import random
import string
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def generate_random_string(length=10):
    """Generate a random string of given length"""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def home(request):
    tracking = generate_random_string(20)
    context = {'tracking': tracking }
    return render(request, 'resume/resume_home.html',context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user  = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('resume-home')
        else:
            messages.error(request,'Username or password is wrong')
    tracking = generate_random_string(20)
    context = {'page': page,'tracking': tracking}
    return render(request, 'resume/login_register.html',context)


def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('resume-home')
        else:
            messages.error(request,'An error occured during registration')
    tracking = generate_random_string(20)
    context = {'form': form,'tracking': tracking}
    return render(request, 'resume/login_register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('resume-home')

def myAccount(request):
    tracking = generate_random_string(20)
    context = {'tracking': tracking}
    return render(request, 'resume/my_account.html',context)

def createBasic(request,tracking):
    if request.user.is_authenticated:
        print('good')
    else:
        print('not good')
        u= User.objects.create_user(username=tracking,password='Marea36*******',email='cdcd@gmail.com')
        u.save()
        login(request,u)
    form = ResumeForm()
    xd = None
    if request.method == "POST":
        form = ResumeForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            if not form.cleaned_data['image']:
                defaults = {
                    'user': request.user,
                    'title': form.cleaned_data['title'],
                    'firstname': form.cleaned_data['firstname'],
                    'lastname': form.cleaned_data['lastname'],
                    'profession': form.cleaned_data['profession'],
                    'city': form.cleaned_data['city'],
                    'country': form.cleaned_data['country'],
                    'postalcode': form.cleaned_data['postalcode'],
                    'phone': form.cleaned_data['phone'],
                    'email': form.cleaned_data['email']
                }
                resume, created = Resume.objects.update_or_create(
                                        tracking=tracking,
                                        defaults=defaults
                                    )
                return redirect('list-work',tracking=tracking)

            else:
                defaults = {
                    'user': request.user,
                    'image': form.cleaned_data['image'],
                    'title': form.cleaned_data['title'],
                    'firstname': form.cleaned_data['firstname'],
                    'lastname': form.cleaned_data['lastname'],
                    'profession': form.cleaned_data['profession'],
                    'city': form.cleaned_data['city'],
                    'country': form.cleaned_data['country'],
                    'postalcode': form.cleaned_data['postalcode'],
                    'phone': form.cleaned_data['phone'],
                    'email': form.cleaned_data['email']
                }
            resume, created = Resume.objects.update_or_create(
                                        tracking=tracking,
                                        defaults=defaults
                                    )
            return redirect('create-basic',tracking=tracking)

        else:
            print(form.errors)
    else:
        try:
            rm = get_object_or_404(Resume,tracking=tracking)
            xd = rm.image
            form_data = {'title': rm.title,
                         'image': rm.image,
                          'firstname': rm.firstname,
                          'lastname': rm.lastname,
                          'profession': rm.profession,
                          'city': rm.city,
                          'country': rm.country,
                          'postalcode': rm.postalcode,
                          'phone': rm.phone,
                          'email': rm.email

                          }
            form = ResumeForm(data=form_data)
        except:
            pass
    socialtracking = generate_random_string(10)
    socials  = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        socials = SocialLink.objects.filter(
                Q(resume = resume)
                )
    except:
        pass
    context = {'form': form,'tracking':tracking,'image': xd,'socials':socials ,'socialtracking': socialtracking}
    return render(request, 'resume/resume_basic.html',context)



def createSummary(request,tracking):
    form = ResumeForm()
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            resume, created = Resume.objects.update_or_create(
                            tracking = tracking,
                            defaults={
                                       'user': request.user,
                                       'professional_summary' : form.cleaned_data['professional_summary']
                                       },
                            )
            return redirect('list-work',tracking=tracking)

        else:
            print(form.errors)
    else:
        try:
            rm = get_object_or_404(Resume,tracking=tracking)
            form_data = {'professional_summary': rm.professional_summary}
            form = ResumeForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking }
    return render(request, 'resume/resume_summary.html',context)

def listSocial(request,tracking):
    try:
        resume = Resume.objects.get(tracking=tracking)
        socials = SocialLink.objects.filter(
            Q(resume = resume)
            )
        if socials:
            print("big e")
        else:
            socialtracking = generate_random_string(10)
            return redirect('list-social',tracking,socialtracking)
        context = {'socials': socials,'tracking': tracking,'socialtracking':socialtracking}
    except:
        newone = generate_random_string(10)
        context = {'socials': socials,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listsocial.html',context)

def addeditSocial(request,tracking,socialtracking):
    form = SocialForm()
    if request.method == 'POST':
        form = SocialForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            social, created = SocialLink.objects.update_or_create(
                            socialtracking = socialtracking,
                            defaults={
                                       'resume': rm,
                                       'name' : form.cleaned_data['name'],
                                       'url' : form.cleaned_data['url']
                                       },
                            )
            return redirect('create-basic',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(SocialLink,socialtracking=socialtracking)
            form_data = {'name': ed.name,
                          'url': ed.url                          }
            print(form_data)
            form = SocialForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Social.html',context)

def deleteSocial(request,tracking,socialtracking):
    sk = SocialLink.objects.get(socialtracking=socialtracking)
    sk.delete()
    return redirect('create-basic',tracking=tracking)


def listWork(request,tracking):
    works = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        works = WorkExperience.objects.filter(
            Q(resume = resume)
            )
    except:
        pass
    newone = generate_random_string(10)
    context = {'works': works,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listwork.html',context)
def addEditWork(request,tracking,worktracking):
    form = WorkForm()
    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            work, created = WorkExperience.objects.update_or_create(
                            worktracking = worktracking,
                            defaults={
                                       'resume': rm,
                                       'job_title' : form.cleaned_data['job_title'],
                                       'employer' : form.cleaned_data['employer'],
                                       'city' : form.cleaned_data['city'],
                                       'country' : form.cleaned_data['country'],
                                       'start_date' : form.cleaned_data['start_date'],
                                       'end_date' : form.cleaned_data['end_date'],
                                       'job_description': form.cleaned_data['job_description']},
                            )
            return redirect('list-work',tracking=tracking)
    else:
        try:
            wk = get_object_or_404(WorkExperience,worktracking=worktracking)
            form_data = {'job_title': wk.job_title,
                          'employer': wk.employer,
                          'city': wk.city,
                          'country': wk.country,
                          'start_date': wk.start_date,
                          'end_date': wk.end_date,
                          'job_description': wk.job_description                    
                          }
            print(form_data)
            form = WorkForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking': tracking}
    return render(request, 'resume/add_edit_work.html',context)

def deleteWork(request,tracking,worktracking):
    wk = WorkExperience.objects.get(worktracking=worktracking)
    wk.delete()
    return redirect('list-work',tracking=tracking)


def listEdu(request,tracking):
    educations = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        educations = Education.objects.filter(
            Q(resume = resume)
            )
        if educations:
            print("big e")
        else:
            edutracking = generate_random_string(10)
            return redirect('addeditedu',tracking,edutracking)
        context = {'educations': educations,'tracking': tracking,'edutracking':edutracking}
    except:
        newone = generate_random_string(10)
        context = {'educations': educations,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listedu.html',context)
def addEditEdu(request,tracking,edutracking):
    form = EduForm()
    if request.method == 'POST':
        form = EduForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            education, created = Education.objects.update_or_create(
                            edutracking = edutracking,
                            defaults={
                                       'resume': rm,
                                       'schoolname' : form.cleaned_data['schoolname'],
                                       'schoollocation' : form.cleaned_data['schoollocation'],
                                       'degree' : form.cleaned_data['degree'],
                                       'fieldofstudy' : form.cleaned_data['fieldofstudy'],
                                       'start_date' : form.cleaned_data['start_date'],
                                       'end_date' : form.cleaned_data['end_date'],
                                       'edu_description' : form.cleaned_data['edu_description']
                                       },
                            )
            return redirect('list-edu',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Education,edutracking=edutracking)
            form_data = {'schoolname': ed.schoolname,
                          'schoollocation': ed.schoollocation,
                          'degree': ed.degree,
                          'fieldofstudy': ed.fieldofstudy,
                          'start_date': ed.start_date,
                          'end_date': ed.end_date,
                          'edu_description': ed.edu_description                    
                          }
            print(form_data)
            form = EduForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_edu.html',context)
def deleteEdu(request,tracking,edutracking):
    ed = Education.objects.get(edutracking=edutracking)
    ed.delete()
    return redirect('list-edu',tracking=tracking)

def listSkill(request,tracking):
    skills = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        skills = Skill.objects.filter(
            Q(resume = resume)
            )
        if skills:
            print("big e")
        else:
            skilltracking = generate_random_string(10)
            return redirect('list-skill',tracking,skilltracking)
        context = {'skills': skills,'tracking': tracking,'skilltracking':skilltracking}
    except:
        newone = generate_random_string(10)
        context = {'skills': skills,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listskill.html',context)

def addeditSkill(request,tracking,skilltracking):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            skill, created = Skill.objects.update_or_create(
                            skilltracking = skilltracking,
                            defaults={
                                       'resume': rm,
                                       'skill_name' : form.cleaned_data['skill_name'],
                                       'proficiency' : form.cleaned_data['proficiency']
                                       },
                            )
            return redirect('list-skill',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Skill,skilltracking=skilltracking)
            form_data = {'skill_name': ed.skill_name,
                          'proficiency': ed.proficiency                          }
            print(form_data)
            form = SkillForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Skill.html',context)

def deleteSkill(request,tracking,skilltracking):
    sk = Skill.objects.get(skilltracking=skilltracking)
    sk.delete()
    return redirect('list-skill',tracking=tracking)

def listLanguage(request,tracking):
    languages = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        languages = Languages.objects.filter(
            Q(resume = resume)
            )
        if languages:
            print("big e")
        else:
            languagetracking = generate_random_string(10)
            return redirect('list-language',tracking,languagetracking)
        context = {'languages': languages,'tracking': tracking,'languagetracking':languagetracking}
    except:
        newone = generate_random_string(10)
        context = {'languages': languages,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listlanguage.html',context)

def addeditLanguage(request,tracking,languagetracking):
    form = LanguageForm()
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            language, created = Languages.objects.update_or_create(
                            languagetracking = languagetracking,
                            defaults={
                                       'resume': rm,
                                       'language_name' : form.cleaned_data['language_name'],
                                       'proficiency' : form.cleaned_data['proficiency']
                                       },
                            )
            return redirect('finalize',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Languages,languagetracking=languagetracking)
            form_data = {'language_name': ed.language_name,
                          'proficiency': ed.proficiency                          }
            print(form_data)
            form = LanguageForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Language.html',context)

def deleteLanguage(request,tracking,languagetracking):
    sk = Languages.objects.get(languagetracking=languagetracking)
    sk.delete()
    return redirect('list-language',tracking=tracking)

def listInterest(request,tracking):
    interests = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        interests = Interests.objects.filter(
            Q(resume = resume)
            )
        if interests:
            print("big e")
        else:
            interesttracking = generate_random_string(10)
            return redirect('list-interest',tracking,interesttracking)
        context = {'interests': interests,'tracking': tracking,'interesttracking':interesttracking}
    except:
        newone = generate_random_string(10)
        context = {'interests': interests,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listinterest.html',context)

def addeditInterest(request,tracking,interesttracking):
    form = InterestForm()
    if request.method == 'POST':
        form = InterestForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            interest, created = Interests.objects.update_or_create(
                            interesttracking = interesttracking,
                            defaults={
                                       'resume': rm,
                                       'interest_name' : form.cleaned_data['interest_name']
                                       },
                            )
            return redirect('finalize',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Interests,interesttracking=interesttracking)
            form_data = {'interest_name': ed.interest_name}
            print(form_data)
            form = InterestForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Interest.html',context)

def deleteInterest(request,tracking,interesttracking):
    sk = Interests.objects.get(interesttracking=interesttracking)
    sk.delete()
    return redirect('finalize',tracking=tracking)



def listAccomplishment(request,tracking):
    accomplishments = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        accomplishments = Accomplishments.objects.filter(
            Q(resume = resume)
            )
        if accomplishments:
            print("big e")
        else:
            accomplishmenttracking = generate_random_string(10)
            return redirect('list-accomplishment',tracking,accomplishmenttracking)
        context = {'accomplishments': accomplishments,'tracking': tracking,'accomplishmenttracking':accomplishmenttracking}
    except:
        newone = generate_random_string(10)
        context = {'accomplishments': accomplishments,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listacc.html',context)

def addeditAccomplishment(request,tracking,accomplishmenttracking):
    form = AccomplishmentForm()
    if request.method == 'POST':
        form = AccomplishmentForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            accomplishment, created = Accomplishments.objects.update_or_create(
                            accomplishmenttracking = accomplishmenttracking,
                            defaults={
                                       'resume': rm,
                                       'accomplishments' : form.cleaned_data['accomplishments']

                                       },
                            )
            return redirect('list-accomplishment',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Accomplishments,accomplishmenttracking=accomplishmenttracking)
            form_data = {'accomplishments': ed.accomplishments}
            print(form_data)
            form = AccomplishmentForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Acc.html',context)

def deleteAccomplishment(request,tracking,accomplishmenttracking):

    sk = Accomplishments.objects.get(accomplishmenttracking=accomplishmenttracking)
    sk.delete()
    return redirect('list-accomplishment',tracking=tracking)

def listAffiliation(request,tracking):
    affiliations = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        affiliations = Affiliations.objects.filter(
            Q(resume = resume)
            )
        if affiliations:
            print("big e")
        else:
            affiliationtracking = generate_random_string(10)
            return redirect('list-affiliation',tracking,affiliationtracking)
        context = {'affiliations': affiliations,'tracking': tracking,'affiliationtracking':affiliationtracking}
    except:
        newone = generate_random_string(10)
        context = {'affiliations': affiliations,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listafi.html',context)

def addeditAffiliation(request,tracking,affiliationtracking):
    form = AffiliationForm()
    if request.method == 'POST':
        form = AffiliationForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            affiliation, created = Affiliations.objects.update_or_create(
                            affiliationtracking = affiliationtracking,
                            defaults={
                                       'resume': rm,
                                       'affiliations' : form.cleaned_data['affiliations']
                                       },
                            )
            return redirect('list-affiliation',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Affiliations,affiliationtracking=affiliationtracking)
            form_data = {'affiliations': ed.affiliations}
            print(form_data)
            form = AffiliationForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Afi.html',context)

def deleteAffiliation(request,tracking,affiliationtracking):
    sk = Affiliations.objects.get(affiliationtracking=affiliationtracking)
    sk.delete()
    return redirect('list-affiliation',tracking=tracking)

def listAdd(request,tracking):
    adds =None
    try:
        resume = Resume.objects.get(tracking=tracking)
        adds = AdditionalInformation.objects.filter(
            Q(resume = resume)
            )
        if adds:
            print("big e")
        else:
            additionalinfotracking = generate_random_string(10)
            return redirect('list-add',tracking,additionalinfotracking)
        context = {'adds': adds,'tracking': tracking,'additionalinfotracking':additionalinfotracking}
    except:
        newone = generate_random_string(10)
        context = {'adds': adds,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listadds.html',context)

def addeditAdd(request,tracking,additionalinfotracking):
    form = AddsForm()
    if request.method == 'POST':
        form = AddsForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            add, created = AdditionalInformation.objects.update_or_create(
                            additionalinfotracking = additionalinfotracking,
                            defaults={
                                       'resume': rm,
                                       'additionalinformation' : form.cleaned_data['additionalinformation']
                                       },
                            )
            return redirect('list-add',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(AdditionalInformation,additionalinfotracking=additionalinfotracking)
            form_data = {'additionalinformation': ed.additionalinformation}
            print(form_data)
            form = AddsForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Add.html',context)

def deleteAdd(request,tracking,additionalinfotracking):
    sk = AdditionalInformation.objects.get(additionalinfotracking=additionalinfotracking)
    sk.delete()
    return redirect('list-add',tracking=tracking)

def listSoftware(request,tracking):
    softwares = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        softwares = Software.objects.filter(
            Q(resume = resume)
            )
        if softwares:
            print("big e")
        else:
            softwaretracking = generate_random_string(10)
            return redirect('list-software',tracking,softwaretracking)
        context = {'softwares': softwares,'tracking': tracking,'softwaretracking':softwaretracking}
    except:
        newone = generate_random_string(10)
        context = {'softwares': softwares,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listsoftware.html',context)

def addeditSoftware(request,tracking,softwaretracking):
    form = SoftwareForm()
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            software, created = Software.objects.update_or_create(
                            softwaretracking = softwaretracking,
                            defaults={
                                       'resume': rm,
                                       'software_name' : form.cleaned_data['software_name'],
                                       'proficiency' : form.cleaned_data['proficiency']
                                       },
                            )
            return redirect('finalize',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Software,softwaretracking=softwaretracking)
            form_data = {'software_name': ed.software_name,
                          'proficiency': ed.proficiency                          }
            print(form_data)
            form = SoftwareForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Software.html',context)

def deleteSoftware(request,tracking,softwaretracking):
    sk = Software.objects.get(softwaretracking=softwaretracking)
    sk.delete()
    return redirect('finalize',tracking=tracking)

def listCertification(request,tracking):
    certifications = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        certifications = Certifications.objects.filter(
            Q(resume = resume)
            )
        if certifications:
            print("big e")
        else:
            certificationtracking = generate_random_string(10)
            return redirect('list-cert',tracking,certificationtracking)
        context = {'certifications': certifications,'tracking': tracking,'certificationtracking':certificationtracking}
    except:
        newone = generate_random_string(10)
        context = {'certifications': certifications,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listcert.html',context)

def addeditCertification(request,tracking,certificationtracking):
    form = CertificationForm()
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            certification, created = Certifications.objects.update_or_create(
                            certificationtracking = certificationtracking,
                            defaults={
                                       'resume': rm,
                                       'certification_name' : form.cleaned_data['certification_name'],
                                       'certification_date' : form.cleaned_data['certification_date']
                                       },
                            )
            return redirect('list-cert',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(Certifications,certificationtracking=certificationtracking)
            form_data = {'certification_name': ed.certification_name,
                          'certification_date': ed.certification_date                          }
            print(form_data)
            form = CertificationForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_Cert.html',context)

def deleteCertification(request,tracking,certificationtracking):
    sk = Certifications.objects.get(certificationtracking=certificationtracking)
    sk.delete()
    return redirect('list-cert',tracking=tracking)

def listYourown(request,tracking):
    yourowns = None
    try:
        resume = Resume.objects.get(tracking=tracking)
        yourowns = YourOwn.objects.filter(
            Q(resume = resume)
            )
        if yourowns:
            print("big e")
        else:
            yourowntracking = generate_random_string(10)
            return redirect('list-yourown',tracking,yourowntracking)
        context = {'yourowns': yourowns,'tracking': tracking,'yourowntracking':yourowntracking}
    except:
        newone = generate_random_string(10)
        context = {'yourowns': yourowns,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_Listown.html',context)

def addeditYourown(request,tracking,yourowntracking):
    form = YourownForm()
    if request.method == 'POST':
        form = YourownForm(request.POST)
        if form.is_valid():
            rm = Resume.objects.get(tracking=tracking)
            yourown, created = YourOwn.objects.update_or_create(
                            yourowntracking = yourowntracking,
                            defaults={
                                       'resume': rm,
                                       'yourown_name' : form.cleaned_data['yourown_name']
                                       },
                            )
            return redirect('list-yourown',tracking=tracking)
    else:
        try:
            ed = get_object_or_404(YourOwn,yourowntracking=yourowntracking)
            form_data = {'yourown_name': ed.yourown_name}
            print(form_data)
            form = YourownForm(data=form_data)
        except:
            pass
    context = {'form': form,'tracking':tracking}
    return render(request, 'resume/add_edit_own.html',context)

def deleteYourown(request,tracking,yourowntracking):
    sk = YourOwn.objects.get(yourowntracking=yourowntracking)
    sk.delete()
    return redirect('list-yourown',tracking=tracking)

def finalize(request,tracking):
    acc_form = AccomplishmentForm()
    aff_form = AffiliationForm()
    adds_form = AddsForm()
    own_form = YourownForm()
    
    interests = None
    softwares = None
    certifications = None




    if request.method == 'POST':
        if 'acc_form_submit' in request.POST:
            form = AccomplishmentForm(request.POST)
            if form.is_valid():
                rm = Resume.objects.get(tracking=tracking)
                accomplishment, created = Accomplishments.objects.update_or_create(
                                accomplishmenttracking = tracking,
                                defaults={
                                        'resume': rm,
                                        'accomplishments' : form.cleaned_data['accomplishments']

                                        },
                                )
                return redirect('finalize',tracking=tracking)
        if 'aff_form_submit' in request.POST:
            form = AffiliationForm(request.POST)
            if form.is_valid():
                rm = Resume.objects.get(tracking=tracking)
                affiliation, created = Affiliations.objects.update_or_create(
                                affiliationtracking = tracking,
                                defaults={
                                        'resume': rm,
                                        'affiliations' : form.cleaned_data['affiliations']
                                        },
                            )
            return redirect('finalize',tracking=tracking)
        
        if 'adds_form_submit' in request.POST:
            form = AddsForm(request.POST)
            if form.is_valid():
                rm = Resume.objects.get(tracking=tracking)
                add, created = AdditionalInformation.objects.update_or_create(
                                additionalinfotracking = tracking,
                                defaults={
                                        'resume': rm,
                                        'additionalinformation' : form.cleaned_data['additionalinformation']
                                        },
                                )
            return redirect('finalize',tracking=tracking)

        if 'own_form_submit' in request.POST:
            form = YourownForm(request.POST)
            if form.is_valid():
                rm = Resume.objects.get(tracking=tracking)
                yourown, created = YourOwn.objects.update_or_create(
                                yourowntracking = tracking,
                                defaults={
                                        'resume': rm,
                                        'yourown_name' : form.cleaned_data['yourown_name']
                                        },
                                )
                return redirect('finalize',tracking=tracking)


    else:
        try:
            acc = get_object_or_404(Accomplishments,accomplishmenttracking=tracking)
            form_data = {'accomplishments': acc.accomplishments}
            acc_form = AccomplishmentForm(data=form_data)
        except:
            pass

        try:
            aff = get_object_or_404(Affiliations,affiliationtracking=tracking)
            aff_data = {'affiliations': aff.affiliations}
            aff_form = AffiliationForm(data=aff_data)
        except:
            pass

        try:
            adob = get_object_or_404(AdditionalInformation,additionalinfotracking=tracking)
            adds_data = {'additionalinformation': adob.additionalinformation}
            adds_form = AddsForm(data=adds_data)
        except:
            pass

        try:
            ownjob = get_object_or_404(YourOwn,yourowntracking=tracking)
            own_data = {'yourown_name': ownjob.yourown_name}
            own_form = YourownForm(data=own_data)
        except:
            pass

        try:
            resume = Resume.objects.get(tracking=tracking)
            interests = Interests.objects.filter(
                Q(resume = resume)
                )
        except:
            pass
        try:
            resume = Resume.objects.get(tracking=tracking)
            softwares = Software.objects.filter(
                Q(resume = resume)
                )
        except:
            pass


        try:
            resume = Resume.objects.get(tracking=tracking)
            certifications = Certifications.objects.filter(
                Q(resume = resume)
                )
        except:
            pass

    newone = generate_random_string(10)
    certificationtracking = generate_random_string(10)

    context = {'tracking': tracking,'acc_form':  acc_form,'aff_form': aff_form,
               'adds_form': adds_form,'own_form':own_form ,'interests': interests,
               'newone': newone,'softwares': softwares,
               'certifications': certifications,
               'certificationtracking':certificationtracking}
    return render(request, 'resume/finalize.html',context)