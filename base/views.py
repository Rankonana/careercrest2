from django.shortcuts import render , get_object_or_404
from django.http import Http404
from .models import Job,JobCategories,JobTypes
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from lxml import html
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET


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
        "title": jb.title[:100],
        "id": jb.id,
        "description": jb.description,
        "location": jb.location,
        "salary": jb.salary[:20],
        "remotePosition": jb.remotePosition,
        "jobType": str(jb.jobType),
        "jobCategory":  str(jb.jobCategory),
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

    urllist = ["https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ErUkqRIUQtfSFFQ8Rtykfw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqU3PwB2X8QEA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpUql0hvQJ7JQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrw3hgdjbQuIg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpV6NwE5a5jGA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq7VR0JwjwHBg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrOWfTeD5bLYg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrVB90nrV9XLQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYzzLJE3r3ReUQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpEXBUVd8yBJg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrGy9pLTSdwWA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpg/LexPVTwNw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQocsgtznSiFdw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQply3h2cOva5Q==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpTjQBGBK9CUQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqKVJnQ3ONzSg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqB30KLreE+9Q==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrjUzkwtpVwVQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoEWVry6xdgeg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrbTg9ZVXnGEw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqQaIf5z243Xw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrRX0goRCVr9g==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqqEcvH2Zrwpg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrdYaJCAWtXyg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQquSvmH3FQxQg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpXZl7Ho1OyUQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYzcZXooil4W9A==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpwLzXWjka3WQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQo8xZzv2JyJxQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqGqMLadrVhrg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrLm0u8fJ8xEQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQr7Ld+LCzW1ow==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYxetW4qU4PLYg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrr6aND7kiEnA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYxdv0MW8tKkpQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=OUVL9XPuNqn3oHmh9nIFmQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqYyYfufpcc5g==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQp+/XhkSR07nQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoQJXzVlpMWPw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq+NVI2kwMpbw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrM+sNy7idR/A==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpUG/tIPGXFRg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoQeC42M/i0UQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq8tkxfbaqLXg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqhiiq0fEX5JQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpLIqeoL6exNg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqRuRORBspMIQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoXlpqyPth0vA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrdsB3yF8ZULg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrbesa4fJDNbA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrLGwNhZu1Tdw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq8ddox7PPESQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq65DxHmVcYqQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrlc8fT/zMGFg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqwo/lWJtxcow==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq6xwW+CYgLiQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQo6mVXDj1kFQg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQp1VUX9LUNc3A==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq+YU4RXHdg3Q==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqe98UWMmDYeg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpGzIUDfR6Rbg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoqPSktjc9ZZw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqIQ3uN6uhFJA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqBYt+yfESvWw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpDXbVrnP3YGg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoAdYQPKFoQLA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ErUkqRIUQteYIjo/t8P+pg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoitjyFRSh6hQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQo+6gg6CuivcQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpe0Oc7muiLKA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpIkdUIbwWB/A==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqyO1Rf31SBfg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpGD67s81peIg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYzoBygwJHtciw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=OUVL9XPuNqm9KBqaLXHLog==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=OUVL9XPuNqlQdi9u1W+/Sw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYwZnvNEab509g==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYw+IS6GhsRvSQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYwDQruqfG9gFA==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYwIrb72jK5RRQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYxNWiL0z7XFcw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYzsZ2KTjyk0Ww==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=+46iViC5wYzMzNMaTFV3xg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqjYk69WzSSpg==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpqfvCSv/CizQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoszrioLFNGaQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQrajHkqMnjQqw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoo88JRMItnig==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ErUkqRIUQtdBDmAo1+FplQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQo6j+PytR1dwQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=OUVL9XPuNqlE9DdZ1rVp/g==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQqXGhC7yJnsKw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoCVnuXrelbcQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQpDoNVhR8maBw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQoeC/Ebmvc2jQ==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQq0+CdTplytBw==",
                "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ykENptjslQp+QOn654CQTA=="]
    # for x in urllist:
    #     try:
    #         url = str(x)
    #         page = requests.get(url)
    #         soup = BeautifulSoup(page.content, 'html.parser') 

    #         title = soup.find(id="body_lblDesc").text
    #         description = str(soup.find("div", {"class": "row contentbody"}))
    #         location =  str(soup.find(id="body_lblCentre").text)
    #         salary =  str(soup.find(id="body_lblPackage").text[:20])
    #         remotePosition =""
    #         jobType = JobTypes.objects.get(id=1)
    #         jobCategory= JobCategories.objects.get(id=1)
    #         positionFilled= None
    #         featuredListing= None
    #         importantInformation= None
    #         expiryDate= None #str(soup.find(id="body_lblClosingDate"))
    #         applicationLinkOrEmail= str(url)
    #         companyname = str("Gauteng " + soup.find(id="body_lblDepartmentName").text)
    #         requirementsstring = str(soup.find("div", {"class": "row contentbody"}).text)
    #         index = requirementsstring.find("Requirements :")
    #         index += 14
    #         duties = requirementsstring[index:index+150]


    #         seodescription = "Requirements :" + str(duties)
    #         companylogo= ""
    #         companylogoexternal = str("http://careercrest.co.za/media/Government_of_Gauteng_logo.svg_vsJwFkS.png")

    #         job = Job(title = title,    description = description ,    location = location,    salary = salary ,    remotePosition = remotePosition,
    #                 jobType = jobType,    jobCategory = jobCategory,    positionFilled = positionFilled,    featuredListing = featuredListing,
    #                 importantInformation = importantInformation,    expiryDate = expiryDate,    applicationLinkOrEmail = applicationLinkOrEmail,
    #                 companyname = companyname,    seodescription = seodescription,    companylogo = companylogo,    companylogoexternal = companylogoexternal)


    #         job.save()
    #     except:
    #         print("skip" + str(x))
    return render(request,'base/contact.html')
def joblist(request):
    categories = JobCategories.objects.all()
    context = {'categories': categories}
    return render(request,'base/job-list.html',context)
def testimonial(request):
    return render(request,'base/testimonial.html')
def notfound(request,exception):

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