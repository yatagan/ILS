# Generated by Django 4.1 on 2022-09-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_bookinstance_isbn_alter_bookinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Технічне обслуговування'), ('o', 'Видана'), ('a', 'Доступна'), ('r', 'Зарезервована')], default='m', help_text='Змінити статус екземпляра', max_length=1),
        ),
    ]
