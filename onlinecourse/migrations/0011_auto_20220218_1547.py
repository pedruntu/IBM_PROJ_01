# Generated by Django 3.1.3 on 2022-02-18 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0010_auto_20220218_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.choice'),
        ),
    ]