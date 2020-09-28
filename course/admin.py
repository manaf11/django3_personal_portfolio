from django.contrib import admin
from .models import *


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'examCode', 'duration', 'cost', 'Instructors', 'Prerequists', 'level')


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'Tutoring')
    pass

admin.site.register(AllCourses)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Course, CourseAdmin)
