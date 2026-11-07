from django.shortcuts import render

from .models import Experience, Project, Skill


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portifolio/home.html', {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
    })


def about(request):
    return render(request, 'portifolio/about.html')
