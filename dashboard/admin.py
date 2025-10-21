from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import UserProfile, ActivityLog

# Unregister the default User admin
admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfil'
    fields = ['role', 'phone', 'address', 'birth_date', 'profile_picture', 'is_active_profile']

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = [
        'username', 'email', 'first_name', 'last_name', 
        'role_badge', 'is_active', 'is_staff', 'date_joined'
    ]
    list_filter = ['is_active', 'is_staff', 'is_superuser', 'userprofile__role']
    
    def role_badge(self, obj):
        if hasattr(obj, 'userprofile'):
            colors = {
                'admin': 'danger',
                'manager': 'warning',
                'staff': 'info',
                'customer': 'success'
            }
            color = colors.get(obj.userprofile.role, 'secondary')
            return format_html(
                '<span class="badge bg-{}">{}</span>',
                color,
                obj.userprofile.get_role_display()
            )
        return format_html('<span class="badge bg-light text-dark">Sin perfil</span>')
    role_badge.short_description = 'Rol'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'role_badge', 'phone', 'is_active_profile', 
        'created_at', 'updated_at'
    ]
    list_filter = ['role', 'is_active_profile', 'created_at']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at']
    
    def role_badge(self, obj):
        colors = {
            'admin': 'danger',
            'manager': 'warning',
            'staff': 'info',
            'customer': 'success'
        }
        color = colors.get(obj.role, 'secondary')
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            color,
            obj.get_role_display()
        )
    role_badge.short_description = 'Rol'

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'action_badge', 'model_name', 'object_repr', 
        'timestamp', 'ip_address'
    ]
    list_filter = ['action', 'model_name', 'timestamp']
    search_fields = ['user__username', 'object_repr', 'description']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    list_per_page = 50
    
    def action_badge(self, obj):
        colors = {
            'create': 'success',
            'update': 'warning',
            'delete': 'danger',
            'login': 'info',
            'logout': 'secondary',
            'view': 'light'
        }
        color = colors.get(obj.action, 'primary')
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            color,
            obj.get_action_display()
        )
    action_badge.short_description = 'Acción'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

# Personalizar el sitio de administración
admin.site.site_header = 'Portfolio Django - Administración'
admin.site.site_title = 'Portfolio Django Admin'
admin.site.index_title = 'Panel de Administración'
