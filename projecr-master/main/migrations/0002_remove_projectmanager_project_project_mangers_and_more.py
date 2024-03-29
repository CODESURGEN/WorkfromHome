# Generated by Django 5.0.2 on 2024-03-09 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmanager',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='mangers',
            field=models.ManyToManyField(blank=True, to='main.projectmanager', verbose_name='Managers'),
        ),
        migrations.AddField(
            model_name='projectmanager',
            name='employees',
            field=models.ManyToManyField(blank=True, to='main.employee', verbose_name='Employees'),
        ),
        migrations.AlterField(
            model_name='projectmanager',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
