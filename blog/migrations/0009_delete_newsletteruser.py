# Generated by Django 3.0.6 on 2020-08-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_newsletteruser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsletterUser',
        ),
    ]