# Generated by Django 3.0.6 on 2020-09-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
