# Generated by Django 2.2.1 on 2020-10-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance2', '0004_remove_attendance_work_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='work_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='労働時間'),
        ),
    ]