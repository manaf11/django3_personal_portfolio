from django.urls import path
from .views import *
app_name = 'course'
urlpatterns = [
    path('', allCourses, {'a': ''},name = 'all_courses'),
    path('<int:a>', detail, name = 'course_detail'),
    path('About_us', about_us, name = 'about_us'),
]