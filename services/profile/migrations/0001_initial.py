# Generated by Django 4.1.7 on 2023-03-29 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalPersonnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6)),
                ('profession', models.CharField(max_length=200)),
                ('hospital', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6)),
                ('address', models.CharField(max_length=250)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB-', 'AB+'), ('AB-', 'AB-')], max_length=6)),
                ('genotype', models.CharField(blank=True, choices=[('AA', 'AA'), ('AS', 'AS'), ('AC', 'AC'), ('SS', 'SS'), ('SC', 'SC')], max_length=11)),
                ('phone', models.CharField(max_length=14, unique=True)),
                ('medical_history', models.ImageField(default='blank_profile_pic.png', upload_to='profile_image')),
                ('profile_picture', models.ImageField(default='blank_profile_pic.png', upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__first_name', 'user__last_name'],
                'permissions': [('view_history', 'Can view history')],
            },
        ),
    ]
