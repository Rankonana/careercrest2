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
        if works:
            print("big e")
        else:
            worktracking = generate_random_string(10)
            return redirect('addeditwork',tracking,worktracking)
        context = {'works': works,'tracking': tracking,'worktracking':worktracking}
    except:
        newone = generate_random_string(10)
        context = {'works': works,'tracking': tracking,'newone': newone}
    return render(request, 'resume/resume_workList.html',context)

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
                          'start_date': wk.start_date,
                          'end_date': wk.end_date,
                          'job_description': wk.job_description                    
                          }
            print(form_data)
            form = WorkForm(data=form_data)
        except:
            pass
    context = {'form': form}
    return render(request, 'resume/edit_delete_work.html',context)