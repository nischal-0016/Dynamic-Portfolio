from django.contrib import admin
from .models import Profile, AboutDetail, AboutMe, Skill,Projects,Contact,ContactMessage

admin.site.register(Profile)
admin.site.register(AboutDetail)
admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Projects)
admin.site.register(Contact)
admin.site.register(ContactMessage)

