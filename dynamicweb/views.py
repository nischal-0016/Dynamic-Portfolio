from django.shortcuts import render
from .models import Profile, AboutDetail, AboutMe, Skill

def portfolio(request):
    profiles = Profile.objects.first()  # Fetch the first Profile record
    about_details = AboutDetail.objects.all()  # Fetch About details
    about_me = AboutMe.objects.first()  # Get the first AboutMe record
    frontend_skills = Skill.objects.filter(category='frontend')  # Frontend skills
    backend_skills = Skill.objects.filter(category='backend')  # Backend skills

    context = {
        'profiles': profiles,  # Sending profiles to the template
        'about_details': about_details,
        'about_me': about_me,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
    }

    return render(request, 'pages/portfolio.html', context)

