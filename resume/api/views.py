from rest_framework.decorators import api_view
from rest_framework.response import Response
from resume.models import *
from .serializers import *
from rest_framework import status


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
        serializer = SoftwareSerializer(software, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteSoftware(request,pk):
    software = Software.objects.get(id=pk)
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
        serializer = LanguageSerializer(language, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def deleteLanguage(request,pk):
    language = Languages.objects.get(id=pk)
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
def deleteCertification(request,pk):
    certification = Certifications.objects.get(id=pk)
    certification.delete()
    return Response(status=status.HTTP_200_OK)
