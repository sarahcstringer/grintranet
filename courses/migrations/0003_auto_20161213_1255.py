# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161212_1830'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseTestimonials',
            new_name='CourseTestimonial',
        ),
        migrations.RenameModel(
            old_name='InstructorTestimonials',
            new_name='InstructorTestimonial',
        ),
    ]
