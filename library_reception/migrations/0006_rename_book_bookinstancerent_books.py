# Generated by Django 4.1 on 2022-09-14 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_reception', '0005_rename_title_book_bookinstancerent_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstancerent',
            old_name='book',
            new_name='books',
        ),
    ]