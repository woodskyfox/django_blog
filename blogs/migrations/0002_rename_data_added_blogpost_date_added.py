# Generated by Django 4.1.7 on 2023-02-23 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
