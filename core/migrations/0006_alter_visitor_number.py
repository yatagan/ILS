# Generated by Django 4.0.4 on 2022-06-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_bookinstance_isbn_visitor_date_added_visitor_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
