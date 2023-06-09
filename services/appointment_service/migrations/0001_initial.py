# Generated by Django 4.1.7 on 2023-03-31 11:04

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_created=django.db.models.fields.DateTimeField)),
                ('message', models.TextField()),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
                'ordering': ('date_time',),
            },
        ),
    ]
