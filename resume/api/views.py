from rest_framework.decorators import api_view
from rest_framework.response import Response
from resume.models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import requests



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/'
        'GET /api/softwares',
        'GET /api/softwares/1',
        'DELETE /api/delete-software/1',

        'GET /api/languages',
        'GET /api/languages/1',
        'DELETE /api/delete-language/1'
    ]
    return Response(routes)

@api_view(['GET'])
def getworkJobtitle(request,search_query):
    url = 'https://builder.zety.com/eb/api/v1/content/jobtitles'
    headers = {
        'authority': 'builder.zety.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie' : 'vssessionuid=8469741e-768a-4c40-9dc1-35cdff43f118; ajs_anonymous_id=ef02ddfd-204c-41d3-80f2-272a9ff9bcbe; vstr=1f6a228f-8f60-469f-9b0e-629e6a0c445b; vsuid=040d792b-8b88-4880-b9f3-03c196118638; ref=20264; visitinfo=[City,Bloemfontein]&[State,FS]&[Country,ZA]&[PostalCode,9301]&[BrowserName,Chrome]&[BrowserVersion,111]&[DeviceType,]&[OSName,Windows]&[DeviceModel,Unknown]&[OSVersion,10.0]; vsutms=af810937-af66-46fc-b2d2-e05db7ff924a#1f6a228f-8f60-469f-9b0e-629e6a0c445b#040d792b-8b88-4880-b9f3-03c196118638#1683322935##||||; _gcl_au=1.1.397478923.1683322935; gdprconsentvariant=3; zety-cookie-consent={"consent":{"analytics":true,"personalization":true,"advertising":true,"necessary":true},"accepted":true,"dateAllowed":1683322935063}; cookiepolicystatus=dismiss; _hjFirstSeen=1; _hjIncludedInSessionSample_215629=0; _hjSession_215629=eyJpZCI6ImYzZDMwYWI2LWFiODYtNDI1YS04ZDg5LTU0MWMzNWIyNWI5MCIsImNyZWF0ZWQiOjE2ODMzMjI5MzUyMTUsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; _fbp=fb.1.1683322935409.1209898503; _gid=GA1.2.321291989.1683322936; x-georegion=198,ZA,,CAPETOWN,,,,,,-33.92,18.42,GMT+2,,AF,,mobile,16637,vhigh,5000; COOKIE_CONSENT={"key":"0cOpFQlpJcrupdOamB93IQN+SQHeax3ilz3eGDC++JUYkDQvd+Dq6BnlfwQiCQOE0xMtYmuFVjZJrZJLic/QHCKQk+33Z9TsThk0td1+f3g=","consent":{"analytics":true,"personalization":true,"advertising":true,"necessary":true},"accepted":true}; bm_mi=48E3A92E39820F0B004A872898D881F9~YAAQT2IVAnpg2uqHAQAAorzd7RM/Th5mt/j3s/hnFwrgmWMYO9FVl7saAYLZ12qqOj5wZwVmeVc1rJpKgxObjSYZFgHNGR6x1NhUzBvogFz7ogE5jaOEyIlPFUoaOeFf/RR42alNIdb1BZF0Y+nIkOOASjVXnIwvAmsAOsZ3bEjbSeWX3pTAv1+eG1BVp2EZCJ24MoUkKirPuJuHnvvG+YlwkTiMlEX+x3SC94lwaTDovd+yRqXuwFHO53KYWAj00KoNZbtwu1d6VSkDbMxQYeiHc5yJXizZbsVKFc3CxAc6oDQKzWKx+pXxUSpBOuPetsVBF3gkqx3dFax81JQHwRDS~1; UserStatus={"IsUserLoggedIn":false,"User":{"Role":0,"UserId":"1f2b6b6c-4c9e-40a5-94f8-154e9be5315c","AccDisplayName":"Guest","CreatedOn":"5/5/2023 9:42:27 PM"}}; acc_session={584c384d-0fb6-458e-9f59-bdc0c35e8b04}; ak_bmsc=4AF0531A13EDC14A12CB6DCF45F80963~000000000000000000000000000000~YAAQT2IVAuFh2uqHAQAAmM7d7ROWHufMCGGI3ZKD6j+3gAwCYYPGGF+m6SyFS5kpRN6NYYP0pD510GcPc8lWUY6tNdsxyUsXNmOIxxtNvvT9f9Q2RdJPsV93nsPFAMPcWtD/b1N8t3Zw1bdOD58svqrlDLLzk7zLkTk1zlXjqg4H7S3EEklnyJrcaKSXi02sFgSEsRk+BcEsxpmQ7ZIlEgtlUSpvqOx2nWKRA42aY0s7KdXpkic8u+0Jd065Z4jZ3vUYbyKRRvMHeVZNCb8irgH2uR3e/kfzpJ6tlobz3jR+wQIAOtPY6LwAW46gOGrdRIa4LKmjCdfznt74NunAoRBfFDDccHFdzxI+sPtH2YPKgB7h+BRACYuCBbjJZ0Xy9l5P4V0c+CDcMNtFxznEML3WuASfCap3PVEoG2PES1r8W2OllpA9wchZLFuQNpcGvQ==; fs_user=0; _ga=GA1.1.1981420595.1683322936; ajs_user_id=1f2b6b6c-4c9e-40a5-94f8-154e9be5315c; _hjSessionUser_215629=eyJpZCI6IjIzNzYyYmVmLTNkMjEtNWVlNi1hOGU3LWUzNTRmNzBmMDE5YyIsImNyZWF0ZWQiOjE2ODMzMjI5MzUyMDEsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; vstrType=1; DocumentID=6eef0ad4-42a2-4397-b9ce-fec56fc75322; _gali=content; Auth=QnezwhwtQDChVGsi9E4TPkDq_bu3Xge6IyO57nEI8cR5K__EF8RrZ4HQjWw5Ln1T6fhM7YEtVaRpwmlixB-1ylaJhNnFvWamvflkY_hzvV3caE8PucHVsaghPE05YGCokXFzfDsgXDv7XSRCcxLdzM4NggeqCVSHGbbRbD1it__yd-kl1iNhtJooPrdcvSU8xHJeoalyS2WKMAL--tJtYfOy_PnJYtveYCHAccwhTiqDTPqhdWW2e76KyoqzygHpBFrPYuT3X4UIDmRAHFXU4slw7OvgQfk9qM_agAdYgBOJc1T6eaFI-9B8EuMnB7-_zkRpqfqo-hBkSewcEkvVn9DdIvCN_ealu1q_y39iZQJ6aVoHHp2uJCeDJe2CTc507itenqOiX55fPexCjPXzJTCIIWWnzOkTuZy7vS4PrEqPJb3JVyarV1bPuRiSBteqKH0reCpj9RpaPJXEdf4Ma6dt8i7i6G3gzgbZFZ8y48jp_rcuMb9nASLicU0My48VvVQuA6n_wn2aqNrRuqT9350iuPWYSF9xPMwqMnyjXsUgGfEPycjQeNqAllA6bzu3WFkBMA4qCrlSNQ55EMgm-NpnddnLDaNMMCVCCMgtTD1m0yFTGsJ2X-hV5PG41XvMJUjIHoUGucZpoeeBUry7XJ4VP2eP_DlRbQUiVzOtDDdd10sLOfGI8DgkV5L3dYKir7kWy7NCAE1IpSQXeGjHViv59nQNCqlrYOSHOhKOvt7ms_HhMtqMNSTLRkzPbK97rhpENahtQrKsvwPaaSiAimZEvZqE5h6tfVVCo7ZxYzhWExMa5scMZADDF2KMVcVU3BVvprljARxOYn2TCgvjvwx4vvtZtomiewbqRTbUbz-hX_0qlfpkP7Bw6FahHIrou3ZofyAlMr7qIvFbP_vamdgED5gGcSEc82E5JkLuiUi8UVALj5tJGejrD431vCRAGbtEvFzvQ5rxJVduPWSU2B8BcPft87heNxtfUGUuy_1bZnIc9nFMh9Uom8RKTbWcX5JqlB_pZzVNslNgerFwYoqoaJbBx1r8LXJF6G7Xqsu3WGmx4EgwWz_RtCCJ9eEvsY9Xavj7DnzzmGrlNmMOxk7Q7ARw7K8Q2IBcjHlQ987VzKPt72qRbV0Yoz_wL1zr8n8FgjvMvM9E7xrnQ9SAr5f5vDcd7N3X8a6Sf35D3yIStGqCwkZOFi1DAFTWwJaAKrZLn2KENaqXSP99Wh-GvA; bm_sv=033A827ABC0F9E118A4E4C300D553213~YAAQT2IVAv502uqHAQAAEsPe7RPw3Gzu3fR2X9oXocUqlLOcCNXibW0A77F4OyAu0cJedkly2QXwupe9Zk4nZ3qVke/TS/ohiBGscLdVxX+9umMSPIZ5ANbjfkC0OAEj8fFGbGfg//yHYf+rynbexxlyeMb8SNBQHvjUGU+7NmlENIyfRK/K2WZcOAo5BdmQ/aBMU6B4h2m5WnUnypT1N3YjFG9ZfoL4UqTjzcl5xd8Dv8+RCJJmudaFgOTfOdA=~1; _ga_P712SPXFF2=GS1.1.1683322935.1.1.1683323011.54.0.0; mixpanelprops=%7B%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24referrer%22%3A%22https%3A//zety.com/resume-builder%22%2C%22%24referring_domain%22%3A%22zety.com%22%2C%22%24current_url%22%3A%22https%3A//builder.zety.com/resume/section/expr%22%2C%22%24browser_version%22%3A111%2C%22%24screen_height%22%3A720%2C%22%24screen_width%22%3A1280%2C%22mp_lib%22%3A%22Segment%3A%20web%22%2C%22%24lib_version%22%3A%222.47.0%22%2C%22%24insert_id%22%3A%22mv6ufb8k12latl4g%22%2C%22time%22%3A1683323017%2C%22distinct_id%22%3A%221f2b6b6c-4c9e-40a5-94f8-154e9be5315c%22%2C%22%24device_id%22%3A%22187edddd4e01b8d-01c1601ed31e06-26031851-e1000-187edddd4e01b8d%22%2C%22%24initial_referrer%22%3A%22https%3A//zety.com/resume-builder%22%2C%22%24initial_referring_domain%22%3A%22zety.com%22%2C%22device%20type%22%3A%22desktop%22%2C%22%24user_id%22%3A%221f2b6b6c-4c9e-40a5-94f8-154e9be5315c%22%2C%22mp_name_tag%22%3A%221f2b6b6c-4c9e-40a5-94f8-154e9be5315c%22%2C%22userId%22%3A%221f2b6b6c-4c9e-40a5-94f8-154e9be5315c%22%2C%22id%22%3A%221f2b6b6c-4c9e-40a5-94f8-154e9be5315c%22%2C%22%24email%22%3A%22TshepoMokoenax@gmail.com%22%7D',
        'origin': 'https://builder.zety.com',
        'referer': 'https://builder.zety.com/resume/section/expr',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    data = {
        'AcceptLanguage': 'en-US',
        'countrycd': 'ZA',
        'DocumentID': '6eef0ad4-42a2-4397-b9ce-fec56fc75322',
        'Placement': 'Experience',
        'PortalCD': 'ZTY',
        'ProductCD': 'RWZ',
        'SearchString': search_query,
        'UserID': '1f2b6b6c-4c9e-40a5-94f8-154e9be5315c',
        'isTypeAheadWithFuzzy': False,
        'isPoolParty': True,
        'poolPartyPhase': 'v1'
    
    }
    response = requests.post(url, headers=headers, json=data)
    json_data = response.json()
    return Response(json_data)

@api_view(['GET'])
def getworkJobdescription(request,search_query):
    url = 'https://builder.zety.com/eb/api/v1/content/texttunercontent'
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://builder.zety.com/resume/section/expr',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'user_uid': 'a9784149-9f0e-4520-8f3a-4fafdec75430',
        'sectionTypeCD': 'EXPR',
        'productCD': 'RWZ',
        'Jobtitle': search_query,
        'searchItemType': 'jobTitle',
        'documentID': '675c2397-ee11-4187-9db0-511e551e63f5',
        'cultureCD': 'en-US',
        'TagScoreSort': 'false',
        'enableFuzzySearch': 'false',
        'includeKGSkills': 'false',
        'fuzzySearchVariation': 'fuzzy',
        'contentMatchVariance': 'baseline',
        'includeUSContentInFallback': 'false',
        'curatedSkillVariance': 'baseline',
        'includeSynonymInIntlFallback': 'false',
        'isPoolParty': 'true',
        'poolPartyPhase': 'v1',
    }
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    return Response(json_data)

@api_view(['GET'])
def getSoftwares(request):
    softwares = Software.objects.all()
    serializer = SoftwareSerializer(softwares, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSoftware(request,pk):
    software = Software.objects.get(id=pk)
    serializer = SoftwareSerializer(software, many=False)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def software_detail(request):
    try:
        software = Software.objects.get(softwaretracking=request.data.get('softwaretracking'))
    except Software.DoesNotExist:
        software = None

    if request.method == 'POST':
        
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        serializer = SoftwareSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if software is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        serializer = SoftwareSerializer(software, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteSoftware(request,softwaretracking):
    software = Software.objects.get(softwaretracking=softwaretracking)
    software.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def getLanguages(request):
    languages = Languages.objects.all()
    serializer = LanguageSerializer(languages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getLanguage(request,pk):
    language = Languages.objects.get(id=pk)
    serializer = LanguageSerializer(language, many=False)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def language_detail(request):
    try:
        language = Languages.objects.get(languagetracking=request.data.get('languagetracking'))
    except Languages.DoesNotExist:
        language = None


    if request.method == 'POST':
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        serializer = LanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if language is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        #
        serializer = LanguageSerializer(language, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteLanguage(request,languagetracking):
    language = Languages.objects.get(languagetracking=languagetracking)
    language.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def getCertifications(request):
    certifications = Certifications.objects.all()
    serializer = CertificationSerializer(certifications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCertification(request,pk):
    certification = Certifications.objects.get(id=pk)
    serializer = CertificationSerializer(certification, many=False)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def certification_detail(request):
    try:
        print("reached")
        print(request.data)
        certification = Certifications.objects.get(certificationtracking=request.data.get('certificationtracking'))
        print("exist")
    except Certifications.DoesNotExist:
        certification = None

    resumeid = Resume.objects.get(tracking =request.data.get('resume') )
    data = request.data.copy()
    data['resume'] = resumeid.pk
    if request.method == 'POST':
        

        serializer = CertificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if certification is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CertificationSerializer(certification, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteCertification(request,certificationtracking):
    certification = Certifications.objects.get(certificationtracking=certificationtracking)
    certification.delete()
    return Response(status=status.HTTP_200_OK)

# image
@api_view(['GET'])
def getImage(request,tracking):
    resume = Resume.objects.get(tracking=tracking)
    serializer = ImageSerializer(resume, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteImage(request, tracking):
    try:
        resume = Resume.objects.get(tracking=tracking)
    except Resume.DoesNotExist:
        return Response({'error': 'Resume not found.'}, status=status.HTTP_404_NOT_FOUND)

    if resume.image:
        storage, path = resume.image.storage, resume.image.path
        storage.delete(path)
        resume.image = None
        resume.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Resume does not have an image.'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST', 'PUT'])
@parser_classes((MultiPartParser, FormParser))
def add_or_update_resume(request):
    try:
        resume = Resume.objects.get(tracking=request.data['tracking'])
    except Resume.DoesNotExist:
        resume = None

    if request.method == 'POST':
        if not resume:
            serializer = ResumeSerializer(data=request.data)
            if serializer.is_valid():
                resume = serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        image = request.data.get('image')
        if image:
            resume.image = image
            resume.save()
            return Response(ResumeSerializer(resume).data)

    elif request.method == 'PUT':
        if not resume:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ResumeSerializer(resume, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def getSocialLinks(request):
    socialLinks = SocialLinks.objects.all()
    serializer = SocialLinkSerializer(socialLinks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSocialLink(request,pk):
    socialLink = SocialLinks.objects.get(id=pk)
    serializer = SocialLinkSerializer(socialLink, many=False)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def socialLink_detail(request):
    try:
        socialLink = SocialLinks.objects.get(socialtracking=request.data.get('socialtracking'))
    except SocialLinks.DoesNotExist:
        socialLink = None

    if request.method == 'POST':
        #
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        #
        serializer = SocialLinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if socialLink is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        #
        serializer = SocialLinkSerializer(socialLink, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['DELETE'])
def deleteSocialLink(request,socialtracking):
    socialLink = SocialLinks.objects.get(socialtracking=socialtracking)
    socialLink.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def getSkills(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSkill(request,pk):
    skill = Skill.objects.get(id=pk)
    serializer = SkillSerializer(skill, many=False)
    return Response(serializer.data)

@api_view(['POST', 'PUT'])
def skill_detail(request):
    try:
        skill = Skill.objects.get(skilltracking=request.data.get('skilltracking'))
    except Skill.DoesNotExist:
        skill = None


    if request.method == 'POST':
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        serializer = SkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        if skill is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        #
        resumeid = Resume.objects.get(tracking =request.data.get('resume') )
        data = request.data.copy()
        data['resume'] = resumeid.pk
        #
        serializer = SkillSerializer(skill, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteSkill(request,skilltracking):
    skill = Skill.objects.get(skilltracking=skilltracking)
    skill.delete()
    return Response(status=status.HTTP_200_OK)
