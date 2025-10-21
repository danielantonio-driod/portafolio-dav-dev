from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Order(models.Model):
    """Modelo para gestión de órdenes"""
    
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('in_progress', 'En Proceso'),
        ('shipped', 'Enviada'),
        ('delivered', 'Entregada'),
        ('cancelled', 'Cancelada'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Baja'),
        ('medium', 'Media'),
        ('high', 'Alta'),
        ('urgent', 'Urgente'),
    ]
    
    order_number = models.CharField(max_length=20, unique=True, verbose_name="Número de Orden")
    customer_name = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    customer_email = models.EmailField(verbose_name="Email del Cliente")
    customer_phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    customer_address = models.TextField(verbose_name="Dirección del Cliente")
    
    product_name = models.CharField(max_length=200, verbose_name="Producto/Servicio")
    product_description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Cantidad")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Unitario")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Total")
    
    status = models.CharField(
        max_length=15, 
        choices=STATUS_CHOICES, 
        default='pending',
        verbose_name="Estado"
    )
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium',
        verbose_name="Prioridad"
    )
    
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    due_date = models.DateTimeField(blank=True, null=True, verbose_name="Fecha de Entrega")
    
    assigned_to = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        verbose_name="Asignado a"
    )
    
    notes = models.TextField(blank=True, null=True, verbose_name="Notas Internas")
    
    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Órdenes"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Orden #{self.order_number} - {self.customer_name}"
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generar número de orden automático
            import random
            import string
            self.order_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Calcular precio total
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    
    def get_status_color(self):
        """Devuelve el color CSS basado en el estado"""
        colors = {
            'pending': 'warning',
            'confirmed': 'info',
            'in_progress': 'primary',
            'shipped': 'secondary',
            'delivered': 'success',
            'cancelled': 'danger'
        }
        return colors.get(self.status, 'secondary')
    
    def get_priority_color(self):
        """Devuelve el color CSS basado en la prioridad"""
        colors = {
            'low': 'success',
            'medium': 'warning', 
            'high': 'danger',
            'urgent': 'dark'
        }
        return colors.get(self.priority, 'secondary')
