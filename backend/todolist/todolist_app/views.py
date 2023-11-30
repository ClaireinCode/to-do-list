from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import List
from .serializers import ListSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
# Create your views here.

class All_Lists(APIView):
    def get(self, request):
        lists = List.objects.all()
        serialized_students = ListSerializer(lists, many=True)
        return Response(serialized_students.data)
    
    def post(self, request):
        new_list = ListSerializer(data=request.data)

        if new_list.is_valid():
            new_list.save()
            return Response(new_list.data, status=HTTP_201_CREATED)
        
        else:
            print(new_list.errors)
            return Response(new_list.errors, status=HTTP_400_BAD_REQUEST)
    
class A_List(APIView):
    def get(self, request, id):
        list = get_object_or_404(List, id = id)
        return Response(ListSerializer(list).data)
    
    def post(self, request):
        new_list = ListSerializer(data=request.data)

        if new_list.is_valid():
            new_list.save()
            return Response(new_list.data, status=HTTP_201_CREATED)
        
        else:
            print(new_list.errors)
            return Response(new_list.errors, status=HTTP_400_BAD_REQUEST)