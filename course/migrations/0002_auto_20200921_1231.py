# Generated by Django 3.1.1 on 2020-09-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequiste',
            field=models.ManyToManyField(null=True, to='course.courses'),
        ),
    ]
