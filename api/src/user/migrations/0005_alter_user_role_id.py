# Generated by Django 3.2.9 on 2021-11-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_user_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
