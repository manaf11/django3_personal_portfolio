# Generated by Django 3.1.1 on 2020-09-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20200922_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='course/images')),
                ('age', models.DateField()),
                ('Degree', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=800)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='coursename',
            new_name='course_name',
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(default='40 Hours', max_length=10),
        ),
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequiste',
            field=models.ManyToManyField(blank=True, to='course.Courses'),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(blank=True, to='course.Instructor'),
        ),
    ]
