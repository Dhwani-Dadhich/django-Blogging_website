# Generated by Django 3.0.6 on 2020-08-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_delete_newsletteruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]