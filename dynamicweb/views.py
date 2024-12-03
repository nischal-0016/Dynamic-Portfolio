from django.shortcuts import render
from .models import Project, AboutDetail, AboutMe, Skill

def portfolio(request):
    projects = Project.objects.all() 
    about_details = AboutDetail.objects.all() 
    about_me = AboutMe.objects.first() 
    frontend_skills = Skill.objects.filter(category='frontend')  
    backend_skills = Skill.objects.filter(category='backend') 

    context = {
        'projects': projects,
        'about_details': about_details,
        'about_me': about_me, 
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills, 
    }

    return render(request, 'pages/portfolio.html', context)
