# Generated by Django 5.0 on 2023-12-19 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imdbapp', '0006_review_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_user',
        ),
    ]