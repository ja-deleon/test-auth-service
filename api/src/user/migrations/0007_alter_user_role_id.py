# Generated by Django 3.2.9 on 2021-11-29 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_role_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.CharField(default='0', max_length=120, null=True),
        ),
    ]
