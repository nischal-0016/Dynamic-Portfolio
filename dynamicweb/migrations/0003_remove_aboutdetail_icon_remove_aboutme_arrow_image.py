# Generated by Django 5.1 on 2024-12-02 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicweb', '0002_aboutdetail_aboutme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutdetail',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='arrow_image',
        ),
    ]