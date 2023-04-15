from django.shortcuts import render
from .models import Job,JobCategories,JobTypes
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import JsonResponse




def xxx(request, page):
    keywords = Job.objects.all()
    paginator = Paginator(keywords, per_page=2)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    context = {"page_obj": page_object}
    return render(request, "base/xxx.html", context)

def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 2)
    startswith = request.GET.get("startswith", "")
    keywords = Job.objects.filter(
        title__startswith=startswith
    )
    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"title": kw.title} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)

def loadmore(request):
    return render(request,'base/loadmore.html')

jobs=[]
def home(request):
    category = request.GET.get('category') if request.GET.get('category') != None else ''
    keyword = request.GET.get('keyword') if request.GET.get('keyword') != None else ''
    location = request.GET.get('location') if request.GET.get('location') != None else ''

    if category == '1':
        category = ''

    jobs = Job.objects.all()
    total_obj = Job.objects.count()       


    if category == ''  and keyword == '' and location == '':
        jobs = jobs

    if category != '':
        jobs = jobs.filter(
            Q(jobCategory = category)
            )
    if keyword != '':
        jobs = jobs.filter(
        Q(title__icontains=keyword) |
        Q(description__icontains=keyword)| 
        Q(location__icontains=keyword)| 
        Q(importantInformation__icontains=keyword)| 
        Q(companyname__icontains=keyword)            
        )

    if location != '':
        jobs = jobs.filter(
        Q(location__icontains=location) 
        )
        
    categories = JobCategories.objects.all()
    context = {'jobs':jobs, 'categories': categories,'total_obj': total_obj}
    return render(request,'base/home.html',context)

def job(request,pk):
    job = Job.objects.get(id=pk)
    jobtypename = job.jobType
    jobtype = JobTypes.objects.get(name = jobtypename)

    context = {'job': job,'jobtype': jobtype}
    return render(request,'base/job.html',context)

def about(request):
    return render(request,'base/about.html')
def category(request):
    return render(request,'base/category.html')
def contact(request):
    return render(request,'base/contact.html')
def joblist(request):
    return render(request,'base/job-list.html')
def testimonial(request):
    return render(request,'base/testimonial.html')
def notfound(request):
    return render(request,'base/notfound.html')

def ourservices(request):
    return render(request,'base/our-services.html')
def privacypolicy(request):
    return render(request,'base/privacy-policy.html')
def termsandconditions(request):
    return render(request,'base/terms-and-conditions.html')