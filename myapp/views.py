from django.shortcuts import render
from .models import Project, Skill

def home(request):
    projects = Project.objects.order_by('-created')
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'skills': skills})