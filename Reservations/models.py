from django.db import models
from USERS.models import User
from courts.models import Court
from courts.models import TimeSlot
from django.core.validators import MinValueValidator , MaxValueValidator


class Reservation(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'در انتظار'),
        ('CONFIRMED', 'تایید شده'),
        ('CANCELLED', 'لغو شده'),
        ('COMPLETED', 'تکمیل شده'),
    )

    user            = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر" , related_name='reservations')
    court           = models.ForeignKey(Court, on_delete=models.CASCADE, verbose_name="زمین" , related_name='reservations')
    slot            = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, verbose_name="اسلات" , related_name='reservations')
    total_price     = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت کل")
    players_count   = models.IntegerField(verbose_name="تعداد بازیکنان" , validators=[MinValueValidator(1) , MaxValueValidator(8)])
    status          = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name="وضعیت" , db_index=True)
    is_paid         = models.BooleanField(default=False, verbose_name="پرداخت شده")
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name_plural = "رزروها"
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'court', 'slot'],
                name='unique_reservation_user_court_slot'
            )
        ]
    def __str__(self):
        return f"{self.user} - {self.court.name} - {self.slot.date}"
    
    def cancel(self):
        self.status = 'CANCELLED'
        self.save()
        if self.slot.status == 'RESERVED':
            self.slot.status = 'AVAILABLE'
            self.slot.save()