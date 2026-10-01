from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def about_me_view(request):
    return render(request, 'pages/about_me.html')


def experience_view(request):
    return render(request, 'pages/experience.html')


def contact_view(request):
    return render(request, 'pages/contact.html')


def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'pages/projects.html', {'projects': projects})

def add_project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'pages/add_project.html', {'form': form})