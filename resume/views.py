from django.shortcuts import render
from django.http import HttpResponse
#from .forms import ResumeForm, WorkExperienceForm, EducationForm, SkillForm
from .forms import ResumeForm
from django.shortcuts import render, redirect
from .models import Resume, WorkExperience
from django.db.models import Q
import random
import string




# Create your views here.
def generate_random_string(length=10):
    """Generate a random string of given length"""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def home(request):
    tracking = generate_random_string(20)
    return render(request, 'resume/resume_home.html',{'tracking': tracking})
    
def createBasic(request,tracking):
    if request.method == 'POST':
        title = request.POST.get('title')
        summary = request.POST.get('professional_summary')

        if Resume.objects.get(tracking=tracking):
            resume = Resume(user=request.user, title=title, professional_summary=summary,tracking= tracking)
            resume.save()
            return redirect('create-work',tracking=tracking)
        else:
            resume = Resume(user=request.user, title=title, professional_summary=summary,tracking= tracking)
            resume.save()
            return redirect('create-work',tracking=tracking)
    else:
        try:
            resume = Resume.objects.get(tracking=tracking)
            context = {'resume': resume}
            return render(request, 'resume/resume_basic.html',context)
        except:
            resume = Resume()
            context = {'resume': resume}
            print("not exist")
            print(tracking)
            return render(request, 'resume/resume_basic.html',context)

    
def createWork(request,tracking):
    if request.method == 'POST':
        resume = Resume.objects.get(tracking=tracking)
        job_title = request.POST.get('job_title')
        employer = request.POST.get('employer')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        job_description = request.POST.get('job_description')
        work = WorkExperience(resume=resume, 
                                job_title=job_title,
                                employer=employer,
                                start_date= start_date,
                                end_date= end_date,
                                job_description=job_description)
        work.save()
        return redirect('create-work',tracking=tracking)
    else:
        try:
            resume = Resume.objects.get(tracking=tracking)
            works = WorkExperience.objects.filter(
                                                Q(resume = resume)
                                                )
            context = {'works': works}
        except:
            works = WorkExperience()
            context = {'works': works}
    return render(request, 'resume/resume_work.html',context)

