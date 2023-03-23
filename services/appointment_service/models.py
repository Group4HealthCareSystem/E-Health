from django.db import models
from django.contrib.auth import get_user_model


class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='appointments_as_patient')
    doctor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='appointments_as_doctor')
    date_time = models.DateTimeField()
    duration = models.DurationField()
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        ordering = ('date_time',)
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f'Appointment with {self.doctor} - {self.date_time.strftime("%d/%m/%Y %H:%M")}'