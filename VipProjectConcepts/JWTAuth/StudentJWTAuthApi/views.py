from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
