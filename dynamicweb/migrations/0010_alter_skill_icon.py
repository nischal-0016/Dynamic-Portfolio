# Generated by Django 5.1 on 2024-12-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicweb', '0009_alter_skill_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='about_icons/'),
        ),
    ]
