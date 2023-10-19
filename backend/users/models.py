from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TestKit(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    test_kit_id = models.CharField(max_length=64)

class User(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=32, null=True, blank=True)
    test_kit_id = models.ForeignKey(TestKit, on_delete=models.SET_NULL, null=True, blank=True)