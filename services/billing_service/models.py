from django.db import models
from django.contrib.auth.models import User
from services.profile.models import PatientModel
from django.utils import timezone


# Create your models here.


class Wallet(models.Model):
    patient = models.OneToOneField(PatientModel, null=True, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, default='NGN')
    created_at = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.patient.__str__()


class WalletTransaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'deposit'),
        ('transfer', 'transfer'),
        ('withdraw', 'withdraw'),
    )
    wallet = models.ForeignKey(Wallet, null=True, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=200, null=True, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=100, null=True, decimal_places=2)
    timestamp = models.DateTimeField(default=timezone.now, null=True)
    status = models.CharField(max_length=100, default="pending")
    paystack_payment_reference = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.wallet.patient.__str__()
