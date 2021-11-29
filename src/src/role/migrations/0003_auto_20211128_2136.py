# Generated by Django 3.2.9 on 2021-11-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0002_auto_20211128_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='desc',
            field=models.CharField(default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='permissions',
            field=models.CharField(default='0', max_length=120, null=True),
        ),
    ]
