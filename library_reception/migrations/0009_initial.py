# Generated by Django 4.1 on 2022-09-17 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visitors', '0002_alter_librarian_options_alter_member_options'),
        ('core', '0008_alter_bookinstance_status'),
        ('library_reception', '0008_delete_bookinstancerent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstanceRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_rent_date', models.DateField()),
                ('return_date', models.DateField()),
                ('books', models.ManyToManyField(to='core.bookinstance', verbose_name='Назва книги:')),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.librarian', verbose_name='Книгу видав:')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visitors.member', verbose_name='Книгу отримав')),
            ],
        ),
    ]