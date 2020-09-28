from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


levels = (('BEGINNER', 'BEGINNER'),
          ('INTERMEDIATE', 'INTERMEDIATE'),
          ('ADVANCED', 'ADVANCED'))


class AllCourses(models.Model):
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return self.course_name


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='course/images')
    age = models.DateField()
    material = models.ManyToManyField('Course', blank=True, related_name='+')
    Degree = models.CharField(max_length=50)
    description = models.TextField(max_length=800)
    phone = PhoneNumberField()
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')

    def Tutoring(self):
        return ', '.join([a.title for a in self.material.all()])

    def __str__(self):
        return self.name


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=30)
    source = models.CharField(max_length=30, default='Redhat')
    examCode = models.CharField(max_length=15)
    description = models.TextField(max_length=800)
    instructor = models.ManyToManyField(Instructor,  blank=True)
    image = models.ImageField(upload_to='course/images')
    level = models.CharField(max_length=30, choices=levels)
    prerequiste = models.ManyToManyField(AllCourses,  blank=True)
    duration = models.CharField(max_length=10, default='40 Hours')
    cost = models.CharField(max_length=10, default='60,000 SP')

    class Meta:
        verbose_name_plural = "Courses"

    def Instructors(self):
        return ', '.join([ins.name for ins in self.instructor.all()])

    def Prerequists(self):
        return ', '.join([pres.course_name for pres in self.prerequiste.all()])

    def __str__(self):
        return self.title
