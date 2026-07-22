from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone        = models.CharField(max_length=11, blank=True, null=True, verbose_name="شماره تماس")
    is_verified  = models.BooleanField(default=False, verbose_name="احراز هویت شده")
    
    class Meta:
        verbose_name        = "کاربر"
        verbose_name_plural = "کاربران"
    
    def __str__(self):
        return self.username