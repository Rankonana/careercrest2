# Generated by Django 4.1.7 on 2023-04-25 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('salary', models.CharField(blank=True, max_length=200, null=True)),
                ('remotePosition', models.BooleanField(blank=True, null=True)),
                ('positionFilled', models.BooleanField(blank=True, null=True)),
                ('featuredListing', models.BooleanField(blank=True, null=True)),
                ('importantInformation', models.CharField(blank=True, max_length=200, null=True)),
                ('expiryDate', models.DateField(blank=True, null=True)),
                ('applicationLinkOrEmail', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('companyname', models.CharField(max_length=200)),
                ('seodescription', models.TextField(blank=True, null=True)),
                ('companylogo', models.ImageField(blank=True, default='logo.png', null=True, upload_to='')),
                ('companylogoexternal', models.URLField(blank=True, null=True)),
                ('jobCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.jobcategories')),
                ('jobType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.jobtypes')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
