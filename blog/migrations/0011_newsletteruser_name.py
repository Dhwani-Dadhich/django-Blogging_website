# Generated by Django 3.0.6 on 2020-08-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_newsletteruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletteruser',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
