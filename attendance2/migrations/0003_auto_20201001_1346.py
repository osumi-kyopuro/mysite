# Generated by Django 2.2.1 on 2020-10-01 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance2', '0002_attendance_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='work_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='労働時間'),
        ),
    ]