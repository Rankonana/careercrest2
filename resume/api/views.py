from rest_framework.decorators import api_view
from rest_framework.response import Response
from resume.models import Software
from .serializers import SoftwareSerializer
from rest_framework import status


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/'
        'GET /api/softwares',
        'GET /api/softwares/1'
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
def software_detail(request,softwaretracking):
    try:
        software = Software.objects.get(softwaretracking=softwaretracking)
    except Software.DoesNotExist:
        software = None

    if request.method == 'POST':
        serializer = SoftwareSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(softwaretracking=softwaretracking)
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
