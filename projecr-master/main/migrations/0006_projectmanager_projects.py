# Generated by Django 5.0.2 on 2024-03-10 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_projectmanager_employees_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmanager',
            name='projects',
            field=models.ManyToManyField(blank=True, to='main.project', verbose_name='Projects'),
        ),
    ]
