# Generated by Django 4.2.1 on 2023-06-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('m', 'Мужской'), ('w', 'Женский')], max_length=7),
        ),
    ]
