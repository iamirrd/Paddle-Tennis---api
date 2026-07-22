from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display     = ('user', 'court', 'slot', 'total_price', 'players_count', 'status', 'is_paid', 'created_at')
    search_fields    = ('user__username', 'court__name')
    list_filter      = ('status', 'is_paid', 'slot__date', 'slot__start_time')
    list_editable    = ('is_paid',)
    readonly_fields  = ('created_at',)
    date_hierarchy   = 'created_at'
    ordering         = ('-created_at',)