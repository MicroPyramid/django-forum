# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-19 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_simple_forum', '0010_forumcategory_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_id', models.CharField(max_length=100)),
                ('facebook_url', models.CharField(default='', max_length=200)),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('verified', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('language', models.CharField(default='', max_length=200)),
                ('hometown', models.CharField(default='', max_length=200)),
                ('email', models.CharField(db_index=True, default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
                ('dob', models.DateField(blank=True, null=True)),
                ('location', models.CharField(default='', max_length=200)),
                ('timezone', models.CharField(default='', max_length=200)),
                ('accesstoken', models.CharField(default='', max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_facebook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GitHub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git_url', models.URLField()),
                ('git_id', models.CharField(max_length=50)),
                ('disk_usage', models.CharField(max_length=200)),
                ('private_gists', models.IntegerField(default=0)),
                ('public_gists', models.IntegerField(default=0)),
                ('public_repos', models.IntegerField(default=0)),
                ('hireable', models.BooleanField(default=False)),
                ('total_private_repos', models.IntegerField(default=0)),
                ('owned_private_repos', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
                ('followers', models.IntegerField(default=0)),
                ('company', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('user_from', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_github', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('google_id', models.CharField(default='', max_length=200)),
                ('google_url', models.CharField(default='', max_length=1000)),
                ('verified_email', models.CharField(default='', max_length=200)),
                ('family_name', models.CharField(default='', max_length=200)),
                ('name', models.CharField(default='', max_length=200)),
                ('picture', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=10)),
                ('dob', models.CharField(default='', max_length=50)),
                ('given_name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(db_index=True, default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_google', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.CharField(default='', max_length=100)),
                ('screen_name', models.CharField(default='', max_length=100)),
                ('oauth_token', models.CharField(default='', max_length=200)),
                ('oauth_secret', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_twitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
