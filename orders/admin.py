from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number', 'customer_name', 'product_name', 'quantity',
        'total_price_formatted', 'status_badge', 'priority_badge',
        'assigned_to', 'created_at', 'actions_column'
    ]
    list_filter = ['status', 'priority', 'assigned_to', 'created_at']
    search_fields = [
        'order_number', 'customer_name', 'customer_email', 
        'product_name', 'customer_address'
    ]
    readonly_fields = ['order_number', 'total_price', 'created_at', 'updated_at']
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información de la Orden', {
            'fields': ('order_number', 'status', 'priority', 'assigned_to')
        }),
        ('Información del Cliente', {
            'fields': ('customer_name', 'customer_email', 'customer_phone', 'customer_address')
        }),
        ('Detalles del Producto', {
            'fields': ('product_name', 'product_description', 'quantity', 'unit_price', 'total_price')
        }),
        ('Fechas y Notas', {
            'fields': ('due_date', 'notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def total_price_formatted(self, obj):
        return f"${obj.total_price:,.2f}"
    total_price_formatted.short_description = 'Precio Total'
    
    def status_badge(self, obj):
        colors = {
            'pending': 'warning',
            'confirmed': 'info',
            'in_progress': 'primary',
            'shipped': 'secondary',
            'delivered': 'success',
            'cancelled': 'danger'
        }
        color = colors.get(obj.status, 'secondary')
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'Estado'
    
    def priority_badge(self, obj):
        colors = {
            'low': 'success',
            'medium': 'warning',
            'high': 'danger',
            'urgent': 'dark'
        }
        color = colors.get(obj.priority, 'secondary')
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            color,
            obj.get_priority_display()
        )
    priority_badge.short_description = 'Prioridad'
    
    def actions_column(self, obj):
        return format_html(
            '<a class="btn btn-sm btn-outline-primary" href="{}">Ver</a>',
            reverse('admin:orders_order_change', args=[obj.pk])
        )
    actions_column.short_description = 'Acciones'
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)
