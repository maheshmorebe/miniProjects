from django.shortcuts import render

# Create your views here.

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

   # filter_backends = [SearchFilter]           # for searching
    filter_backends = [OrderingFilter]          # for ordering
    ordering_fields = ['name']
    #search_fields = ['name','city']
    search_fields = ['^name','^city']           # starts with   --> in url 127.0.0.1:8000/studentapi/?search=s,r,a etc.letters




    # def get_queryset(self):                 # it will filter the list and give us the result by passby=user
    #     user = self.request.user
    #     return Student.objects.filter(passby=user)
