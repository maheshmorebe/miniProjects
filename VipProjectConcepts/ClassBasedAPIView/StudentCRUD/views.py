from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status


class StudentAPI(APIView):
    def get(self,request, pk=None, format = None):
        if pk is not None:
            stud = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stud)
            return Response(serializer.data)
        studs = Student.objects.all()
        serializer = StudentSerializer(studs,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,format = None):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student created successfully!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk,format = None):
        data = request.data
        stud = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stud,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Update successful!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format = None):
        data = request.data
        stud = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stud,data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial update successful!'})
        return Response(serializer.errors)

    def delete(self,request,pk,format = None):
        stud = Student.objects.get(pk=pk)
        if stud:
            stud.delete()
            return Response({'msg':'Deleted successfully!'})
        return Response({'msg':'No matched record!'})