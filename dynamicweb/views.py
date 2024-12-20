from django.shortcuts import render, redirect
from .models import Profile, AboutDetail, AboutMe, Skill, Projects, Contact,ContactMessage
from django.contrib import messages

def portfolio(request):
    profiles = Profile.objects.first()
    about_details = AboutDetail.objects.all()
    about_me = AboutMe.objects.first()
    frontend_skills = Skill.objects.filter(category='frontend')
    backend_skills = Skill.objects.filter(category='backend')
    projects = Projects.objects.all()
    contact = Contact.objects.first()  
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('portfolio')
        else:
            messages.error(request, 'All fields are required. Please try again.')

    context = {
        'profiles': profiles,
        'about_details': about_details,
        'about_me': about_me,
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills,
        'projects': projects,
        'contact': contact,
    }

    return render(request, 'pages/portfolio.html', context)