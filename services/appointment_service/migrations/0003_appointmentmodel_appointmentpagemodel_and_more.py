# Generated by Django 4.1.7 on 2023-03-31 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('profile', '0001_initial'),
        ('appointment_service', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('meeting_date', models.DateField()),
                ('message', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profile.patientmodel')),
            ],
            options={
                'ordering': ['submit_time'],
                'permissions': [('cancel_appointment', 'Can cancel appointment')],
            },
        ),
        migrations.CreateModel(
            name='AppointmentPageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appoint', to='appointment_service.appointmentmodel')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='hospital_details', to='hospital.hospitalmodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]
