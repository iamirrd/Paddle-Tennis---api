from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display    = ('user', 'reservation', 'amount', 'status', 'created_at') 
    search_fields   = ('user__username', 'reservation__court__name')
    list_filter     = ('status',)
    list_editable   = ('status',)
    readonly_fields = ('created_at', 'updated_at' , 'id' )
    date_hierarchy  = 'created_at'        
    ordering        = ('-created_at',)