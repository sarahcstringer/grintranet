from __future__ import unicode_literals
import datetime
# from django.utils import timezone
from django.db import models

# Create your models here.

class InstructorTestimonial(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField('added at')

class CourseTestimonial(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField('added at')

class Course(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    course_testimonials = models.ManyToManyField(CourseTestimonial)

    def __str__(self):
        """Helpful representation of Course object."""

        return '{}: {}-{}'.format(self.title, self.start_date.strftime(
            '%m/%d/%Y'), self.end_date.strftime('%m/%d/%Y'))

    class Meta:
        ordering = ('start_date',)

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        blank=True,
    )
    phone = models.CharField(
        blank=True,
        max_length=10,
    )
    linkedin = models.CharField(
        blank=True,
        max_length=200,
    )
    twitter = models.CharField(
        blank=True,
        max_length=200,
    )
    instagram = models.CharField(
        blank=True,
        max_length=200,
    )
    facebook = models.CharField(
        blank=True,
        max_length=200,
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Personal Biography',
    )
    # photo = models.ImageField(
    #     upload_to='static/courses/images/instructors/')
    courses = models.ManyToManyField(Course)
    testimonials = models.ManyToManyField(InstructorTestimonial)

    def __str__(self):
        """Helpful represntation of Instructor object."""

        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('last_name',)
