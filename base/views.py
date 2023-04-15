from django.shortcuts import render
from .models import Job,JobCategories,JobTypes
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import JsonResponse


def my_view(request):
    data = Job.objects.all()
    print(data.count())

    # Set the number of items per page
    items_per_page = 2

    paginator = Paginator(data, items_per_page)

    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, return the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range, return the last page
        page_obj = paginator.page(paginator.num_pages)

    serialized_data = []
    for obj in page_obj:
        # Serialize the data
        data = {
            'id': obj.id, 'title': obj.title,
            'title': obj.title,
            'description': obj.description,
            'location': obj.location,
            'salary': obj.salary,
            'remotePosition': obj.remotePosition,
            'jobType': str(obj.jobType),
            'jobCategory': [str(category) for category in obj.jobCategory.all()],
            'positionFilled': obj.positionFilled,
            'featuredListing': obj.featuredListing,
            'importantInformation': obj.importantInformation,
            'expiryDate': str(obj.expiryDate),
            'applicationLinkOrEmail': obj.applicationLinkOrEmail,
            'created': str(obj.created),
            'updated': str(obj.updated),
            'companyname': obj.companyname,
            'companylogo': obj.companylogo
            }
        serialized_data.append(data)

    return JsonResponse({'data': serialized_data})


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