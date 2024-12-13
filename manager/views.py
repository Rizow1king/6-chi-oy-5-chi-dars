from django.shortcuts import render
from .models import Course, Student


def home(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    context = {
        'courses': courses,
        'students': students
    }
    return render(request, 'index.html', context)


def courses_by_id(request, course_id):
    courses = Course.objects.filter(pk=course_id)
    students = Student.objects.filter(course_id=course_id)
    context = {
        'courses': courses,
        'students': students
    }
    return render(request, 'index.html', context)


def courses_detail(request, detailed_course_id):
    course = Course.objects.get(id=detailed_course_id)
    context = {
        'courses': course
    }
    return render(request, 'detail.html', context)