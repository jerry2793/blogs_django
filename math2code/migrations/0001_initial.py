# Generated by Django 3.1.3 on 2020-11-29 03:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Math2codeContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('header_image', models.ImageField(upload_to='math2code/images/')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('problem', models.TextField()),
                ('explaination_problem', models.TextField()),
                ('code', models.FileField(upload_to='math2code/code')),
                ('code_type', models.CharField(choices=[('1', 'Python'), ('2', 'JavaScript')], default='1', max_length=25)),
                ('explaination_code', models.TextField()),
                ('url', models.URLField(blank=True, default=None, max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('when_publish', models.DateTimeField(default=datetime.datetime(2020, 11, 28, 19, 47, 24, 733964))),
                ('author', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Math2codeComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='math2code.math2codecontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Math2codeCommentReplies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math2code.math2codecomments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.profile')),
            ],
        ),
    ]
