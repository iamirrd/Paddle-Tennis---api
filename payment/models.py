from django.db import models
from USERS.models import User
from courts.models import Court
from Reservations.models import Reservation

class Payment(models.Model):
    PAYMENT_STATUS = (
        ('PENDING', 'در انتظار'),
        ('PAID', 'پرداخت شده'),
        ('FAILED', 'ناموفق'),
        ('REFUNDED', 'برگشت داده شده'),
    )
    
    user            = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    reservation     = models.ForeignKey(Reservation, on_delete=models.CASCADE, verbose_name="رزرو")
    amount          = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مبلغ")
    status          = models.CharField(max_length=20, choices=PAYMENT_STATUS, default="PENDING", verbose_name="وضعیت")
    tracking_code   = models.CharField(max_length=100, blank=True, verbose_name="کد پیگیری")
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at      = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")
    
    class Meta:
        verbose_name_plural = "پرداخت‌ها"
        verbose_name = 'پرداخت'
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.status}"