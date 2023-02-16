from django.shortcuts import render

# Create your views here.
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

