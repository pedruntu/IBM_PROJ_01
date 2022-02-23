# Generated by Django 3.1.3 on 2022-02-18 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0008_remove_submission_choices'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='choice_id',
        ),
        migrations.AddField(
            model_name='answer',
            name='choice_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.choice'),
        ),
    ]