from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField()
    def __str__(self):
        return self.title
