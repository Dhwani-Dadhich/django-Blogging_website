# Generated by Django 3.0.6 on 2020-09-01 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_blog_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='blog',
        ),
    ]
