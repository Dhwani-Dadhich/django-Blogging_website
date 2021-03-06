# Generated by Django 3.0.6 on 2020-08-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_newsletteruser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=300, null=True)),
                ('last', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
