# from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Application1.models import Schools, Students
from Application1.serializers import SchoolsSerializer, StudentsSerializer


def index(request):
    return HttpResponse("Hello, welcome on our new App!")


@api_view(['GET', 'POST'])
def schools_list(request):
    """
    List all code schools, or create a new school.
    """
    if request.method == 'GET':
        schools = Schools.objects.all()
        serializer = SchoolsSerializer(schools, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SchoolsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def school_detail(request, pk):
    """
    Retrieve, update or delete a code schools.
    """
    try:
        school = Schools.objects.get(pk=pk)
    except Schools.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolsSerializer(school)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SchoolsSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def students_list(request):
    """
    List all code students, or create a new student.
    """
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    """
    Retrieve, update or delete a code student.
    """
    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        content = {'please move along': 'nothing to see here'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentsSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
