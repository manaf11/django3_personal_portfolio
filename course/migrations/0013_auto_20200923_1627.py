# Generated by Django 3.1.1 on 2020-09-23 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20200923_1619'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='courses',
            new_name='AllCourses',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterField(
            model_name='instructor',
            name='material',
            field=models.ManyToManyField(blank=True, related_name='_instructor_material_+', to='course.Course'),
        ),
    ]
