"""
URL configuration for portfolio_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth import views as auth_views

def home_view(request):
    """Vista principal del sitio"""
    return render(request, 'home.html')

def register_view(request):
    """Vista de registro de usuarios"""
    from orders.forms import CustomUserCreationForm
    from django.contrib.auth import login
    from django.shortcuts import redirect
    from django.contrib import messages
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear perfil de usuario
            from dashboard.models import UserProfile
            UserProfile.objects.create(user=user, role='customer')
            
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.get_full_name()}! Tu cuenta ha sido creada exitosamente.')
            return redirect('dashboard:profile')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    
    # Autenticación
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', register_view, name='register'),
    
    # Apps
    path('contact/', include('contact.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('orders/', include('orders.urls')),
]

# Servir archivos media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
