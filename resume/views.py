from django.shortcuts import render
from django.http import HttpResponse
#from .forms import ResumeForm, WorkExperienceForm, EducationForm, SkillForm
from .forms import ResumeForm , WorkForm
from django.shortcuts import render, redirect
from .models import Resume, WorkExperience
from django.db.models import Q
import random
import string
from django.shortcuts import get_object_or_404





# Create your views here.
def generate_random_string(length=10):
    """Generate a random string of given length"""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def home(request):
    tracking = generate_random_string(20)
    return render(request, 'resume/resume_home.html',{'tracking': tracking})
    
def createBasic(request,tracking):
    form = ResumeForm()
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            resume, created = Resume.objects.update_or_create(
                            tracking = tracking,
                            defaults={
                                       'user': request.user,
                                       'title' : form.cleaned_data['title'],
                                       'professional_summary': form.cleaned_data['professional_summary']},
                            )
            return redirect('list-work',tracking=tracking)
        else:
            print(form.errors)
    else:
        # get values of existing resume
        initial_values = {'title': 'hello'}
        # form = ResumeForm(initial=initial_values)
        try:
            rm = get_object_or_404(Resume,tracking=tracking)
            form_data = {'title': rm.title, 'professional_summary': rm.professional_summary}
            print(rm.title)
            form = ResumeForm(data=form_data)
        except:
            pass
    context = {'form': form }
    return render(request, 'resume/resume_basic.html',context)

def listWork(request,tracking):
    try:
        resume = Resume.objects.get(tracking=tracking)
        works = WorkExperience.objects.filter(
            Q(resume = resume)
            )
        context = {'works': works}
    except:
        works = WorkExperience()
        context = {'works': works}
    return render(request, 'resume/resume_workList.html',context)

def addEditWork(request,tracking):
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
        return redirect('list-work',tracking=tracking)
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
    return render(request, 'resume/resume_workList.html',context)
