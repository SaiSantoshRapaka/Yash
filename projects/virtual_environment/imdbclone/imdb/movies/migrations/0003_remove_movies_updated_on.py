# Generated by Django 4.2.4 on 2023-08-27 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_movies_release_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='updated_on',
        ),
    ]
