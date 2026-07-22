from django.contrib import admin
from .models import Court, CourtImage, Schedule, TimeSlot, BlockedSlot, CourtPricing
from django.utils.html import format_html


class CourtImageInline(admin.TabularInline):
    model = CourtImage
    extra = 3
    fields = ('image', 'is_primary')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'max_players', 'base_price_per_hour', 'is_active')
    search_fields = ('name', 'address', 'city')
    list_filter = ('city', 'is_active', 'max_players')
    list_editable = ('is_active',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [CourtImageInline]
    

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('court', 'day_of_week', 'start_time', 'end_time', 'is_active')
    search_fields = ('court__name',)
    list_filter = ('day_of_week', 'is_active')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('court', 'date', 'start_time', 'end_time', 'status')
    search_fields = ('court__name',)
    list_filter = ('status', 'date')
    list_editable = ('status',)
    date_hierarchy = 'date'
    ordering = ('-date', 'start_time')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(BlockedSlot)
class BlockedSlotAdmin(admin.ModelAdmin):
    list_display = ('court', 'date', 'start_time', 'end_time', 'description', 'is_active')
    search_fields = ('court__name', 'description')
    list_filter = ('is_active',)
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(CourtPricing)
class CourtPricingAdmin(admin.ModelAdmin):
    list_display = ('court', 'pricing_type', 'price_multiplier', 'is_active')
    search_fields = ('court__name', 'pricing_type')
    list_filter = ('pricing_type', 'is_active')
    list_editable = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')
