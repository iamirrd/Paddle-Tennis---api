from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display    = ('user', 'court', 'rating', 'is_approved', 'created_at') 
    search_fields   = ('user__username', 'court__name')
    list_filter     = ('rating', 'is_approved')
    list_editable   = ('is_approved',)
    readonly_fields = ('created_at', 'updated_at' , 'id' )
    date_hierarchy  = 'created_at'
    ordering        = ('-created_at',)