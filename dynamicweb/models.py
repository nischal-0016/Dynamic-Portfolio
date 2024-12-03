from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AboutDetail(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class AboutMe(models.Model):
    introduction = models.TextField()
    arrow_image = models.ImageField(upload_to='about_icons/', null=True, blank=True)

    def __str__(self):
        return "About Me Section"
    


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES) 
    level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.category})"