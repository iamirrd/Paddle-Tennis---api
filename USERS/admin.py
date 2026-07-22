from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display        = ('username', 'email', 'phone', 'is_verified', 'is_staff', 'is_active')
    search_fields       = ('username', 'email')
    list_filter         = ('is_staff', 'is_active', 'is_verified')
    list_editable       = ('is_staff', 'is_active', 'is_verified')
    readonly_fields     = ('id', 'date_joined', 'last_login')
    ordering            = ('-date_joined',)  