# Generated by Django 4.1 on 2022-09-17 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_reception', '0007_delete_bookreservation_delete_librarycard_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookInstanceRent',
        ),
    ]