# Generated by Django 4.0.4 on 2022-05-23 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumecreator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_info',
            name='about_you',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='job1details',
            field=models.TextField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='job2details',
            field=models.TextField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='job3details',
            field=models.TextField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='references',
            field=models.TextField(max_length=500),
        ),
    ]