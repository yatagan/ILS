# Generated by Django 4.0.5 on 2022-09-24 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_bookinstance_format_book'),
        ('library_reception', '0010_bookinstanceorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstanceorder',
            name='status',
        ),
        migrations.AlterField(
            model_name='bookinstanceorder',
            name='books',
            field=models.ManyToManyField(to='core.bookinstance', verbose_name='Назва книги:'),
        ),
    ]
