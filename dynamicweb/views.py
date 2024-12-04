from django.shortcuts import render
from .models import Profile, AboutDetail, AboutMe, Skill, Projects

def portfolio(request):
    profiles = Profile.objects.first()
    about_details = AboutDetail.objects.all()
    about_me = AboutMe.objects.first()
    frontend_skills = Skill.objects.filter(category='frontend')
    backend_skills = Skill.objects.filter(category='backend')
    projects = Projects.objects.all() 
    context = {
        'profiles': profiles,
        'about_details': about_details,
        'about_me': about_me,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'projects': projects,
    }

    return render(request, 'pages/portfolio.html', context)
