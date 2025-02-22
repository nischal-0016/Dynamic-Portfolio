# Generated by Django 5.1 on 2024-12-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicweb', '0007_alter_skill_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.ImageField(default='skills/icons/default_icon.png', upload_to='skills/icons/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(max_length=50),
        ),
    ]
