# Generated by Django 3.0.6 on 2020-08-31 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200831_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.NewsletterUser'),
        ),
    ]
