from django.db import models
from USERS.models import User
from courts.models import Court
from courts.models import BaseModel


class Review(BaseModel):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user        = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر" , related_name='reviews' , db_index=True)
    court       = models.ForeignKey(Court, on_delete=models.CASCADE, verbose_name="زمین" , related_name='reviews' , db_index=True)
    rating      = models.IntegerField(choices=RATING_CHOICES, default=1 , verbose_name="امتیاز" , db_index=True)
    comment     = models.TextField(blank=True, verbose_name="نظر")
    is_approved = models.BooleanField(default=False, verbose_name="تایید شده" , db_index=True)
    
    class Meta:
        verbose_name_plural   = "نظرات"
        verbose_name          = 'نظر'    
        ordering              = ['-created_at']
        
        constraints = [
            models.UniqueConstraint(
                fields=['user' , 'court'],
                name='unique_user_court_review'
            )
        ]
    def __str__(self):
        return f"{self.user.username} - {self.court.name} - {self.rating}"
