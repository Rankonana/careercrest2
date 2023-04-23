import requests
from lxml import html
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET


url = "https://professionaljobcentre.gpg.gov.za/Public/ViewJob.aspx?u=ErUkqRIUQtfSFFQ8Rtykfw=="
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') 

title = soup.find(id="body_lblDesc").text
description = soup.find("div", {"class": "row contentbody"})
location =  soup.find(id="body_lblCentre").text
salary =  soup.find(id="body_lblPackage").text
remotePosition =""
jobType = "1"
jobCategory="6"
positionFilled=""
featuredListing=""
importantInformation=""
expiryDate= soup.find(id="body_lblClosingDate")
applicationLinkOrEmail= url
# created= ""
# updated= ""
companyname = "Gauteng " + soup.find(id="body_lblDepartmentName").text
requirementsstring = soup.find("div", {"class": "row contentbody"}).text
index = requirementsstring.find("Requirements :")
index += 14
duties = requirementsstring[index:index+150]


seodescription = "Requirements :" + duties
companylogo= ""
companylogoexternal = "https://professionaljobcentre.gpg.gov.za/lib/images/logo.png"

job = Job(title = title,
description = description ,
location = location,
salary = salary ,
remotePosition = remotePosition,
jobType = jobType,
jobCategory = jobCategory,
positionFilled = positionFilled,
featuredListing = featuredListing,
importantInformation = importantInformation,
expiryDate = expiryDate,
applicationLinkOrEmail = applicationLinkOrEmail,
companyname = companyname,
seodescription = seodescription,
companylogo = companylogo,
companylogoexternal = companylogoexternal)

job.save()

# with open('jobs.csv', 'w', newline='') as file:
#      writer = csv.writer(file,delimiter='z')
#      writer.writerow(["title","description ","location","salary ","remotePosition",
#                     "jobType","jobCategory","positionFilled","featuredListing","importantInformation",
#                     "expiryDate","applicationLinkOrEmail","companyname","seodescription",
#                     "companylogo","companylogoexternal"])
#      writer.writerow([title,description ,location,salary ,remotePosition,jobType,jobCategory,
#                       positionFilled,featuredListing,importantInformation,expiryDate,applicationLinkOrEmail,
#                       companyname,seodescription,companylogo,companylogoexternal])

