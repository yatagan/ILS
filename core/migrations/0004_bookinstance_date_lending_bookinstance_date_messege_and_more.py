# Generated by Django 4.1 on 2022-09-08 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_delete_rack'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='date_lending',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='date_messege',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='format_book',
            field=models.IntegerField(choices=[(1, 'paper'), (2, 'electorinic')], default=0),
        ),
    ]
