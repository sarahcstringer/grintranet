# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTestimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField(verbose_name='added at')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorTestimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField(verbose_name='added at')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Personal Biography'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='instructor',
            name='facebook',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='instructor',
            name='instagram',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='instructor',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='instructor',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='instructor',
            name='twitter',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='course_testimonials',
            field=models.ManyToManyField(to='courses.CourseTestimonials'),
        ),
        migrations.AddField(
            model_name='instructor',
            name='testimonials',
            field=models.ManyToManyField(to='courses.InstructorTestimonials'),
        ),
    ]