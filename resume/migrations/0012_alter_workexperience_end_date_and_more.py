# Generated by Django 4.2.1 on 2023-06-06 22:13

from django.db import migrations
import resume.models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_alter_resume_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=resume.models.MonthYearField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=resume.models.MonthYearField(blank=True, null=True),
        ),
    ]
