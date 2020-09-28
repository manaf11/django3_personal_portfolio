from django.shortcuts import render
from .models import *


# Create your views here.
def allCourses(request, a):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course/all_courses.html', context)


def detail(request, a):
    reqCourse = Course.objects.filter(pk=a).get()
    # print('name', name)
    # reqCourse = Course.objects.filter(title=name)
    print('aaaaaaa ',reqCourse)
    context = {'reqCourse': reqCourse}
    return render(request, 'course/detail.html', context)

def about_us(request):
    return render(request, 'course/about.html')
