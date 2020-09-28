from django.urls import path

from .views import *

app_name = 'portfolio'
urlpatterns = [
    path('', home, name='home'),
    path('About_us', about_us, name='about_us'),

]
