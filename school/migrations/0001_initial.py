# Generated by Django 3.0 on 2020-04-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExamScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('math', 'คณิตศาสตร์'), ('sci', 'วิทยาศาสตร์'), ('art', 'ศิลปะ'), ('eng', 'ภาษาอังกฤษ'), ('social', 'สังคมศึกษา'), ('thai', 'ภาษาไทย')], default='math', max_length=200)),
                ('student_name', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
