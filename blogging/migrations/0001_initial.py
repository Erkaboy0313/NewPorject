# Generated by Django 5.1.4 on 2025-01-09 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('view', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft'), ('blocked', 'Blocked')], default='draft', max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('dislike', models.ManyToManyField(related_name='dislike_set', to='user.profile')),
                ('likes', models.ManyToManyField(related_name='like_set', to='user.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('like', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogging.blog')),
                ('reply', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogging.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
