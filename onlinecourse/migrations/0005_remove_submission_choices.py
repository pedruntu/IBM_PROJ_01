# Generated by Django 3.1.3 on 2022-02-17 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_auto_20220214_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='choices',
        ),
    ]
