# Generated by Django 4.2.1 on 2023-06-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=7),
        ),
    ]