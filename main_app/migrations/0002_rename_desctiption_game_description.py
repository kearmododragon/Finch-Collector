# Generated by Django 4.2 on 2023-04-12 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='desctiption',
            new_name='description',
        ),
    ]