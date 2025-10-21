from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """Formulario para mensajes de contacto"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre completo',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 XXX XXX XXXX (opcional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Asunto del mensaje',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escriba su mensaje aquí...',
                'required': True
            }),
            'priority': forms.Select(attrs={
                'class': 'form-select'
            })
        }
        labels = {
            'name': 'Nombre Completo',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'subject': 'Asunto',
            'message': 'Mensaje',
            'priority': 'Prioridad del Mensaje'
        }
    
    def clean_email(self):
        """Validación personalizada para el email"""
        email = self.cleaned_data.get('email')
        if email:
            # Verificar que el dominio no sea temporal
            blocked_domains = ['tempmail.com', '10minutemail.com', 'guerrillamail.com']
            domain = email.split('@')[1].lower()
            if domain in blocked_domains:
                raise forms.ValidationError('No se permiten correos de dominios temporales.')
        return email
    
    def clean_message(self):
        """Validación para el mensaje"""
        message = self.cleaned_data.get('message')
        if message and len(message) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 caracteres.')
        return message
    
    def save(self, commit=True):
        """Personalizar el guardado"""
        instance = super().save(commit=False)
        # Establecer valores por defecto
        instance.status = 'new'
        instance.is_read = False
        if commit:
            instance.save()
        return instance

class ContactMessageUpdateForm(forms.ModelForm):
    """Formulario para actualizar mensajes de contacto (admin)"""
    
    class Meta:
        model = ContactMessage
        fields = ['status', 'priority', 'admin_notes', 'is_read']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'admin_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Notas internas del administrador...'
            }),
            'is_read': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'status': 'Estado del Mensaje',
            'priority': 'Prioridad',
            'admin_notes': 'Notas del Administrador',
            'is_read': 'Marcar como Leído'
        }