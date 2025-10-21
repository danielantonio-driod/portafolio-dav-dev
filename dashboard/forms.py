from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """Formulario para el perfil de usuario"""
    
    class Meta:
        model = UserProfile
        fields = ['role', 'phone', 'address', 'birth_date', 'profile_picture']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+57 XXX XXX XXXX'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Dirección completa'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }
        labels = {
            'role': 'Rol del Usuario',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'birth_date': 'Fecha de Nacimiento',
            'profile_picture': 'Foto de Perfil'
        }

class UserUpdateForm(forms.ModelForm):
    """Formulario para actualizar información básica del usuario"""
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            })
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico'
        }

class UserRoleForm(forms.ModelForm):
    """Formulario para gestión de roles (solo admins)"""
    
    class Meta:
        model = UserProfile
        fields = ['role', 'is_active_profile']
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
            'is_active_profile': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {
            'role': 'Rol del Usuario',
            'is_active_profile': 'Perfil Activo'
        }