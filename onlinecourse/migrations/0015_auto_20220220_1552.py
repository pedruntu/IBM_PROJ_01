# Generated by Django 3.1.3 on 2022-02-20 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0014_auto_20220220_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question_id',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question'),
            preserve_default=False,
        ),
    ]
