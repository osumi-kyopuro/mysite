# Generated by Django 2.2.1 on 2020-10-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance2', '0005_attendance_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='work_time',
            field=models.DurationField(blank=True, null=True, verbose_name='労働時間'),
        ),
    ]
