# Generated by Django 3.1.1 on 2020-09-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20200923_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequiste',
            field=models.ManyToManyField(blank=True, to='course.Courses'),
        ),
    ]