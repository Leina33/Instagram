# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-04 05:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null='False', upload_to='pictsagram/')),
                ('caption', models.CharField(max_length=700)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(default='default.jpg', upload_to='ProfilePIcture/')),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('bio', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(blank=True, default=False, related_name='likes', to='socials.Profile'),
        ),
        migrations.AddField(
            model_name='image',
            name='uploader_profile',
            field=models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='socials.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='imagecomment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_comments', to='socials.Image'),
        ),
    ]
