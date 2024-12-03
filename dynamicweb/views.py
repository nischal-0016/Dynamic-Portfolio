from django.shortcuts import render
from .models import Project
from .models import AboutDetail, AboutMe


def portfolio(request):
    projects = Project.objects.all()
    about_details = AboutDetail.objects.all()
    about_me = AboutMe.objects.first()  # Assumes one "About Me" entry
    return render(request, 'pages/portfolio.html', {
        'projects': projects,
        'about_details': about_details,
        'about_me': about_me
    })