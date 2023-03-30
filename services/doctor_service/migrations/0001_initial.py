# Generated by Django 4.1.7 on 2023-03-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=16)),
                ('specialty', models.CharField(choices=[('epidemiologist', 'Epidemiologist'), ('general practitioner', 'General practitioner'), ('pediatrician', 'Pediatrician'), ('dentist', 'Dentist'), ('surgeon', 'Surgeon'), ('dermatologist', 'Dermatologist'), ('plastic surgeon', ' Plastic Surgeon'), ('psychiatrist', 'Psychiatrist')], default='psychiatrist', max_length=20)),
                ('available_days', models.DateTimeField()),
            ],
            options={
                'ordering': ('available_days',),
            },
        ),
    ]
