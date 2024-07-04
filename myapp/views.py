from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Student
from myapp.serializers import StudentSerializer

class StudentViewsets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
