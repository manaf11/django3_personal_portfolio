from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/home.html', context)