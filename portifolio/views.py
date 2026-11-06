from django.shortcuts import render

from .models import Project, Skill


def home(request):
    projects = Project.objects.order_by('-created')
    skills = Skill.objects.order_by('name')
    return render(request, 'portifolio/home.html', {
        'projects': projects,
        'skills': skills,
    })


def about(request):
    return render(request, 'portifolio/about.html')
