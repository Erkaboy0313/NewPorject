# Generated by Django 5.1.4 on 2025-01-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=7),
        ),
    ]
