# Generated by Django 4.1.7 on 2023-04-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_jobcategories_jobtypes_job_jobcategory_job_jobtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='importantInformation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
