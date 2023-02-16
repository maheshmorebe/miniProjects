from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
#from .mypagination import MyPageNumberPagination
from .mypagination import MyLimitOffsetPagination

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
#   pagination_class = MyPageNumberPagination
    pagination_class = MyLimitOffsetPagination

