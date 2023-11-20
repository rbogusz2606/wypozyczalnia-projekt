from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Cars
from .serializers import CarsSerializer
from rest_framework import status

@api_view(['GET'])
def getData(request):
    objects = Cars.objects.all()
    serializer = CarsSerializer(objects, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addObject(request):
    serializer = CarsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def PutDeteteFunc(request, id):
    GetbyPk = Cars.objects.get(pk=id)
    if request.method == 'PUT':
        serializer = CarsSerializer(GetbyPk, data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        GetbyPk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
