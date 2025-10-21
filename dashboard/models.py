from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    """Perfil extendido de usuario para roles y permisos adicionales"""
    
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('manager', 'Gerente'),
        ('staff', 'Personal'),
        ('customer', 'Cliente'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    role = models.CharField(
        max_length=15, 
        choices=ROLE_CHOICES, 
        default='customer',
        verbose_name="Rol"
    )
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    address = models.TextField(blank=True, null=True, verbose_name="Dirección")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    profile_picture = models.ImageField(
        upload_to='profiles/', 
        blank=True, 
        null=True,
        verbose_name="Foto de Perfil"
    )
    is_active_profile = models.BooleanField(default=True, verbose_name="Perfil Activo")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
    
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username
    
    def can_manage_orders(self):
        """Verifica si el usuario puede gestionar órdenes"""
        return self.role in ['admin', 'manager', 'staff']
    
    def can_manage_messages(self):
        """Verifica si el usuario puede gestionar mensajes"""
        return self.role in ['admin', 'manager', 'staff']
    
    def can_access_dashboard(self):
        """Verifica if el usuario puede acceder al dashboard"""
        return self.role in ['admin', 'manager', 'staff']

class ActivityLog(models.Model):
    """Registro de actividades del sistema"""
    
    ACTION_CHOICES = [
        ('create', 'Crear'),
        ('update', 'Actualizar'),
        ('delete', 'Eliminar'),
        ('login', 'Iniciar Sesión'),
        ('logout', 'Cerrar Sesión'),
        ('view', 'Ver'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, verbose_name="Acción")
    model_name = models.CharField(max_length=50, verbose_name="Modelo")
    object_id = models.PositiveIntegerField(blank=True, null=True, verbose_name="ID del Objeto")
    object_repr = models.CharField(max_length=200, verbose_name="Representación del Objeto")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name="Dirección IP")
    timestamp = models.DateTimeField(default=timezone.now, verbose_name="Fecha y Hora")
    
    class Meta:
        verbose_name = "Registro de Actividad"
        verbose_name_plural = "Registros de Actividad"
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.user.username} - {self.get_action_display()} - {self.model_name}"
