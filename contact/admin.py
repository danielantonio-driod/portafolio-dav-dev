from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'email', 'subject', 'priority_badge', 'status_badge', 
        'is_read_badge', 'created_at', 'actions_column'
    ]
    list_filter = ['status', 'priority', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 20
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Información del Contacto', {
            'fields': ('name', 'email', 'phone', 'subject')
        }),
        ('Mensaje', {
            'fields': ('message', 'priority')
        }),
        ('Estado y Gestión', {
            'fields': ('status', 'is_read', 'admin_notes')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
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
    
    def status_badge(self, obj):
        colors = {
            'new': 'primary',
            'in_progress': 'warning',
            'resolved': 'success',
            'closed': 'secondary'
        }
        color = colors.get(obj.status, 'secondary')
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            color,
            obj.get_status_display()
        )
    status_badge.short_description = 'Estado'
    
    def is_read_badge(self, obj):
        if obj.is_read:
            return format_html('<span class="badge bg-success">Leído</span>')
        else:
            return format_html('<span class="badge bg-warning">No leído</span>')
    is_read_badge.short_description = 'Leído'
    
    def actions_column(self, obj):
        return format_html(
            '<a class="btn btn-sm btn-outline-primary" href="{}">Ver</a>',
            reverse('admin:contact_contactmessage_change', args=[obj.pk])
        )
    actions_column.short_description = 'Acciones'
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }
        js = ('admin/js/custom_admin.js',)
