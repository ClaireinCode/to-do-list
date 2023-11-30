from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import List
from .serializers import ListSerializer
# Create your views here.

class All_Lists(APIView):
    def get(self, request):
        lists = List.objects.all()
        serialized_students = ListSerializer(lists, many=True)
        return Response(serialized_students.data)
    
class A_List(APIView):
    def get(self, request, id):
        list = get_object_or_404(List, id = id)
        return Response(ListSerializer(list).data)