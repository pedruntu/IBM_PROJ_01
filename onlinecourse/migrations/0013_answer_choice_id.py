# Generated by Django 3.1.3 on 2022-02-18 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0012_remove_answer_choice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='choice_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.choice'),
        ),
    ]
