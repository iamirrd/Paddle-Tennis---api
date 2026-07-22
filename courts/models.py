from django.db import models
from django.core.exceptions import ValidationError

class BaseModel(models.Model):
    
    created_at          = models.DateTimeField(auto_now_add=True , verbose_name="تاریخ ایجاد")
    updated_at          = models.DateTimeField(auto_now=True , verbose_name="تاریخ آخرین به روز رسانی")
    
    class Meta:
        abstract = True 


class Facility(models.Model):
    name                = models.CharField(max_length=100 , verbose_name="نام امکانات")
    description         = models.TextField(verbose_name="توضیحات" , blank=True)
    
    class Meta:
        verbose_name_plural = "امکانات"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Court(BaseModel):
    COURT_TYPES = (
        ('PADDLE', 'پدل'),
        ('TENNIS', 'تنیس'),
    )
    CITY_CHOICES = (
        ('تهران', 'تهران'),
        ('کرج', 'کرج'),
        ('تبریز', 'تبریز'),
        ('کیش', 'کیش'),
        ('اصفهان', 'اصفهان'),
        ('شیراز', 'شیراز'),
        ('قزوین', 'قزوین'),
        ('مرکزی', 'مرکزی'),
    )

    name                = models.CharField(max_length=100 , verbose_name="نام زمین")
    address             = models.CharField(max_length=100 , verbose_name="آدرس")
    city                = models.CharField(verbose_name="شهر" , choices=CITY_CHOICES , db_index=True , default="تهران")
    max_players         = models.IntegerField(verbose_name="تعداد بازیکنان مجاز")
    base_price_per_hour = models.DecimalField(verbose_name="قیمت پایه برای هر ساعت" , max_digits=10 , decimal_places=2 , default=0)
    description         = models.TextField(verbose_name="توضیحات" , blank=True)
    is_active           = models.BooleanField(default=True , verbose_name="فعال یا غیرفعال" , db_index=True)
    facilities          = models.ManyToManyField(Facility, blank=True , verbose_name="کارت ها")
    court_type          = models.CharField(max_length=10 , choices=COURT_TYPES , default="PADDLE" , verbose_name="نوع زمین")
    
    class Meta:
        verbose_name_plural = "زمین ها"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
class CourtImage(BaseModel):
    court               = models.ForeignKey(Court , on_delete=models.CASCADE , verbose_name="زمین" , related_name="images")
    image               = models.ImageField(verbose_name="تصویر" , upload_to='court_images/%Y/%m/%d/')
    is_primary          = models.BooleanField(default=False , verbose_name="اصلی یا دیگر")

    class Meta:
        verbose_name_plural = "تصاویر زمین"
        ordering = ['is_primary']

    def __str__(self):
        return self.court.name
    
class Schedule(BaseModel):
    DAYS_OF_WEEK = (
        (0, 'شنبه'),
        (1, 'یکشنبه'),
        (2, 'دوشنبه'),
        (3, 'سه شنبه'),
        (4, 'چهارشنبه'),
        (5, 'پنجشنبه'),
        (6, 'جمعه'),
    )
    court               = models.ForeignKey(Court , on_delete=models.CASCADE , verbose_name="زمین" , related_name="schedules")
    day_of_week         = models.IntegerField(choices=DAYS_OF_WEEK , verbose_name="روز" , db_index=True)
    start_time          = models.TimeField(verbose_name="زمان شروع")
    end_time            = models.TimeField(verbose_name="زمان پایان")
    is_active           = models.BooleanField(default=True , verbose_name="فعال یا غیرفعال" , db_index=True)

    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError("زمان شروع باید بعد از زمان پایان باشد")

    
    class Meta:
        verbose_name_plural = "زمان‌ها"
        ordering = ['court', 'day_of_week', 'start_time']
        constraints = [
            models.UniqueConstraint(fields=['court', 'day_of_week', 'start_time', 'end_time'], name='unique_schedule'),
        ]
            
    def __str__(self):
        return f"{self.court.name} - {'اصلی' if self.is_primary else 'فرعی'}"


class TimeSlot(BaseModel):
    SLOT_STATUS = (
        ('AVAILABLE', 'آزاد'),
        ('RESERVED', 'رزرو شده'),
        ('BLOCKED', 'مسدود'),
        ('EXPIRED', 'منقضی شده'),
    ) 
    court               = models.ForeignKey(Court , on_delete=models.CASCADE , verbose_name="زمین" , related_name="time_slots")
    start_time          = models.TimeField(verbose_name="زمان شروع")
    end_time            = models.TimeField(verbose_name="زمان پایان")
    status              = models.CharField(max_length=10 , choices=SLOT_STATUS , default="AVAILABLE" , verbose_name="وضعیت" , db_index=True)
    date                = models.DateField(verbose_name="تاریخ", db_index=True)
    special_price       = models.DecimalField(verbose_name="قیمت ویژه" , max_digits=10 ,
                        decimal_places=2 , blank=True , null=True ,
                        help_text="در صورت خالی بودن، قیمت پایه زمین استفاده می‌شود"
)
    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError("زمان شروع باید بعد از زمان پایان باشد")
    
    class Meta:
        verbose_name ='بازه زمانی'
        verbose_name_plural = "بازه های زمانی"
        ordering = ['court', 'date', 'start_time']
        constraints = [
            models.UniqueConstraint(
                fields=['court', 'date', 'start_time', 'end_time'],
                name='unique_timeslot_court_date_time'
            )
        ]
            
    def __str__(self):
        return f"{self.court.name} - {self.date} ({self.start_time} تا {self.end_time})"
    
class CourtPricing(BaseModel):
    PRICING_TYPES = (
        ('WEEKDAY', 'روز های عادی'),
        ('WEEKEND', 'آخر هفته'),
        ('SPECIAL', 'مناسبات خاص'),
        ('HOLIDAY', 'تعطیلات'),
    )
    court               = models.ForeignKey(Court , on_delete=models.CASCADE , verbose_name="زمین" , related_name="pricing")
    price_multiplier    = models.DecimalField(verbose_name="مقیاس قیمت" , max_digits=10 , decimal_places=2 , default=1.00)
    description         = models.TextField(verbose_name="توضیحات" , blank=True)
    is_active           = models.BooleanField(default=True , verbose_name="فعال یا غیرفعال" , db_index=True)
    pricing_type        = models.CharField(max_length=10 , choices=PRICING_TYPES , default="WEEKDAY" , verbose_name="نوع قیمت گذاری")

    @property
    def final_price(self):
        return self.court.base_price_per_hour * self.price_multiplier
    
    class Meta:
        verbose_name_plural = "قیمت های زمین"
        ordering = ['court']
        constraints = [
            models.UniqueConstraint(
                fields=['court', 'pricing_type'],
                name='unique_courtpricing_court_type'
            )
        ]
        
    def __str__(self):
        return f"{self.court.name} - {self.get_pricing_type_display()}"
        
class BlockedSlot(BaseModel):
    court               = models.ForeignKey(Court , on_delete=models.CASCADE , verbose_name="زمین" , related_name="blocked_slots")
    date                = models.DateField(verbose_name="تاریخ" , db_index=True)
    start_time          = models.TimeField(verbose_name="زمان شروع")
    end_time            = models.TimeField(verbose_name="زمان پایان")
    description         = models.TextField(verbose_name="توضیحات" , blank=True)
    is_active           = models.BooleanField(default=True , verbose_name="فعال یا غیرفعال" , db_index=True)

    
    def clean(self):
        if self.start_time and self.end_time:
            if self.start_time >= self.end_time:
                raise ValidationError("زمان شروع باید بعد از زمان پایان باشد")
    
    class Meta:
        verbose_name ='بازه مسدود'
        verbose_name_plural = "بازه های مسدود"
        ordering = ['court', 'date', 'start_time']
        constraints = [
            models.UniqueConstraint(
                fields=['court', 'date', 'start_time', 'end_time'],
                name='unique_blocked_slot_court_date_time'
            )
        ]
                
    def __str__(self):
        return f"{self.court.name} - {self.date} ({self.start_time} تا {self.end_time})"