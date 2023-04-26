from django.shortcuts import render , get_object_or_404, redirect
from django.http import Http404
from .models import Job,JobCategories,JobTypes, Post
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView, DetailView


def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 10)

    keyword = request.GET.get("keyword", "")
    category = request.GET.get("jobCategory", "")
    location = request.GET.get("location", "")


    jobs = []
    jobs = Job.objects.all()

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
    paginator = Paginator(jobs, per_page)
    page_obj = paginator.get_page(page_number)

    data = [
    {
        "title": jb.title[:80],
        "id": jb.id,
        "description": jb.description,
        "location": jb.location,
        "salary": jb.salary,
        "remotePosition": jb.remotePosition,
        "jobType": str(jb.jobType),
        "jobCategory": str(jb.jobCategory),
        "positionFilled": jb.positionFilled,
        "featuredListing": jb.featuredListing,
        "importantInformation": jb.importantInformation,
        "expiryDate": str(jb.expiryDate),
        "applicationLinkOrEmail": jb.applicationLinkOrEmail,
        "created": str(jb.created),
        "updated": str(jb.updated),
        "companyname": jb.companyname,
        "companylogo": jb.companylogoexternal if jb.companylogoexternal else (jb.companylogo.url if jb.companylogo else None),
        "theurl": jb.get_absolute_url(),
        "seodescription": jb.seodescription
    } 
    for jb in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)



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

def job(request, id,title):
    try:
        job = Job.objects.get(id=id)
        if(job.companylogoexternal):
            job.companylogo = job.companylogoexternal
        else:
            job.companylogo = "https://careercrest.co.za" + str(job.companylogo.url)

        jobtypename = job.jobType
        jobtype = JobTypes.objects.get(name = jobtypename)
        context = {'job': job,'jobtype': jobtype}
    except Job.DoesNotExist:
        return render(request,'base/notfound.html')
    return render(request,'base/job.html',context)

def about(request):
    return render(request,'base/about.html')

# def category(request): 
#     jobs = Job.objects.all()
#     categories = JobCategories.objects.all()
#     context = {'categories': categories,'jobs': jobs}
#     return render(request,'base/category.html',context)

def contact(request):
    return render(request,'base/contact.html')
def joblist(request):
    categories = JobCategories.objects.all()
    context = {'categories': categories}
    return render(request,'base/job-list.html',context)
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

def ads_txt(request):
    content = "google.com, pub-4323271819190092, DIRECT, f08c47fec0942fa0"
    response = HttpResponse(content, content_type='text/plain')
    return response

def xxx(request, page):
    jobs = Job.objects.all()
    paginator = Paginator(jobs, per_page=2)
    page_object = paginator.get_page(page)
    page_object.adjusted_elided_pages = paginator.get_elided_page_range(page)
    context = {"page_obj": page_object}
    return render(request, "base/xxx.html", context)
def loadmore(request):
    return render(request,'base/loadmore.html')

# Blog
def post_list(request):
    posts = Post.objects.all() 
    # search
    query = request.GET.get("q")
    if query:
        posts=Post.objects.filter(Q(title__icontains=query) ).distinct()
            
    
    paginator = Paginator(posts, 2) # 10 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
   
        
    return render(request,'base/post_list.html',{'posts':posts, page:'pages'})

def post_detail(request, id,title):
    try:
        post = Post.objects.get(id=id)
        context = {'post': post}
    except Post.DoesNotExist:
        return render(request,'base/notfound.html')
    return render(request,'base/post_detail.html',context)