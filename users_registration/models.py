from django.db import models
from django.contrib.auth.models import AbstractUser
from  django.core.validators import MinLengthValidator, MaxLengthValidator
from . manager import UserModelManager


# Create your models here.

class Register(AbstractUser):
    phone = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=250, validators = [MinLengthValidator(7, message='Your password is too short! Minimum of 8 length is required')])
    email = models.EmailField(unique=True)
    username = None


    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserModelManager()







