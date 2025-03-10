# Generated by Django 4.0.4 on 2022-05-25 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of project ', max_length=50)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='Date created')),
                ('completion_time', models.DateTimeField(help_text='Completion time', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Task Title', max_length=50)),
                ('description', models.TextField(help_text='Task description=')),
                ('time_estimation', models.IntegerField(help_text='The task estimation time')),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
    ]
