# Generated by Django 3.1.3 on 2022-02-18 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0006_auto_20220218_0850'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
    ]