# Generated by Django 5.1 on 2024-12-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamicweb', '0011_remove_aboutdetail_icon_remove_skill_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='profile_pics/')),
            ],
        ),
    ]
