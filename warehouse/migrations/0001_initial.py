# Generated by Django 4.1 on 2022-09-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_rack', models.IntegerField(default=0)),
                ('number_shell', models.IntegerField(default=0)),
            ],
        ),
    ]