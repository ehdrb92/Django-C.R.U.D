# Generated by Django 4.0.5 on 2022-07-05 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_data',
            new_name='release_date',
        ),
    ]
