from django.shortcuts import render
from .models import *
from course import models

# Create your views here.
def home(request):
    projects = Project.objects.all()
    courses = models.Course.objects.all()
    context = {'projects': projects,'courses': courses}

    return render(request, 'portfolio/home.html', context)

def about_us(request):
    return render(request, 'portfolio/about.html')
