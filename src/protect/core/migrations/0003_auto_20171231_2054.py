# Generated by Django 2.0 on 2017-12-31 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_person_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, help_text='Email de la Persona que esta reportando', max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='person',
            name='type_publication',
            field=models.CharField(blank=True, choices=[('missing', 'missing'), ('found', 'found')], default='missing', max_length=150, verbose_name='type'),
        ),
    ]
