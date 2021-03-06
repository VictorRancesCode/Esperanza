# Generated by Django 2.0 on 2017-12-31 03:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('nickname', models.CharField(blank=True, max_length=150, verbose_name='nickname')),
                ('date', models.DateField(verbose_name='date')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='person')),
                ('comment_photo', models.CharField(blank=True, max_length=150, verbose_name='comment the photo')),
                ('age', models.IntegerField(verbose_name='age')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], default='M', max_length=150, verbose_name='gender')),
                ('detail', models.CharField(blank=True, max_length=500, verbose_name='details')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('type_publication', models.CharField(blank=True, choices=[('missing', 'missing'), ('found', 'found')], default='found', max_length=150, verbose_name='type')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
