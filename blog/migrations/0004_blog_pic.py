# Generated by Django 3.0.6 on 2020-08-10 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200809_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pic',
            field=models.ImageField(null=True, upload_to='images//'),
        ),
    ]
