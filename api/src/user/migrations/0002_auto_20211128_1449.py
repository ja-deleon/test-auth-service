# Generated by Django 3.2.9 on 2021-11-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
