from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import fanStatus
from . serializers import fanStatusSerializer

# Create your views here
class statusList(APIView):

    def get(self, request):
        statusInfo = fanStatus.objects.all()
        serializer = fanStatusSerializer(statusInfo, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = fanStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    
    # def delete(request, pk):
    #     statusInfo = fanStatus.objects.get(id=pk)
    #     statusInfo.delete()

        return Response("Successfully deleted")



 
def home(request):
    return render(request, "smartfan/home.html")