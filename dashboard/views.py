from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, ActivityLog
from .forms import UserProfileForm, UserUpdateForm, UserRoleForm
from contact.models import ContactMessage
from orders.models import Order

@login_required
def dashboard_home(request):
    """Vista principal del dashboard"""
    # Verificar permisos
    if not hasattr(request.user, 'userprofile') or not request.user.userprofile.can_access_dashboard():
        messages.error(request, 'No tienes permisos para acceder al dashboard.')
        return redirect('home')
    
    # Estadísticas generales
    stats = {
        'total_messages': ContactMessage.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'new_messages': ContactMessage.objects.filter(status='new').count(),
        'urgent_messages': ContactMessage.objects.filter(priority='urgent').count(),
        
        'total_orders': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'in_progress_orders': Order.objects.filter(status='in_progress').count(),
        'delivered_orders': Order.objects.filter(status='delivered').count(),
        
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
        'staff_users': User.objects.filter(is_staff=True).count(),
    }
    
    # Mensajes recientes
    recent_messages = ContactMessage.objects.select_related().order_by('-created_at')[:5]
    
    # Órdenes recientes
    recent_orders = Order.objects.select_related('assigned_to').order_by('-created_at')[:5]
    
    # Actividad reciente
    recent_activity = ActivityLog.objects.select_related('user').order_by('-timestamp')[:10]
    
    # Estadísticas por fecha (últimos 7 días)
    end_date = timezone.now()
    start_date = end_date - timedelta(days=7)
    
    daily_stats = []
    for i in range(7):
        date = start_date + timedelta(days=i)
        daily_stats.append({
            'date': date.strftime('%Y-%m-%d'),
            'messages': ContactMessage.objects.filter(
                created_at__date=date.date()
            ).count(),
            'orders': Order.objects.filter(
                created_at__date=date.date()
            ).count(),
        })
    
    context = {
        'stats': stats,
        'recent_messages': recent_messages,
        'recent_orders': recent_orders,
        'recent_activity': recent_activity,
        'daily_stats': daily_stats,
        'user_role': request.user.userprofile.role,
        'page_title': 'Dashboard Principal'
    }
    
    return render(request, 'dashboard/dashboard_home.html', context)

@login_required
def profile_view(request):
    """Vista del perfil de usuario"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                user=request.user,
                action='update',
                model_name='UserProfile',
                object_id=profile.id,
                object_repr=str(profile),
                description='Perfil actualizado'
            )
            
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('dashboard:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'page_title': 'Mi Perfil'
    }
    
    return render(request, 'dashboard/profile.html', context)

@login_required
def user_management(request):
    """Vista de gestión de usuarios (solo admin y managers)"""
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role not in ['admin', 'manager']:
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('dashboard:dashboard_home')
    
    # Filtros
    search_query = request.GET.get('search', '')
    role_filter = request.GET.get('role', '')
    status_filter = request.GET.get('status', '')
    
    # Consulta base
    users_query = User.objects.select_related('userprofile').prefetch_related('groups')
    
    # Aplicar filtros
    if search_query:
        users_query = users_query.filter(
            Q(username__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    if role_filter:
        users_query = users_query.filter(userprofile__role=role_filter)
    
    if status_filter == 'active':
        users_query = users_query.filter(is_active=True)
    elif status_filter == 'inactive':
        users_query = users_query.filter(is_active=False)
    
    users = users_query.order_by('-date_joined')
    
    context = {
        'users': users,
        'search_query': search_query,
        'role_filter': role_filter,
        'status_filter': status_filter,
        'role_choices': UserProfile.ROLE_CHOICES,
        'page_title': 'Gestión de Usuarios'
    }
    
    return render(request, 'dashboard/user_management.html', context)

@login_required
def edit_user_role(request, user_id):
    """Vista para editar el rol de un usuario"""
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role not in ['admin', 'manager']:
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('dashboard:dashboard_home')
    
    user = get_object_or_404(User, id=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = UserRoleForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                user=request.user,
                action='update',
                model_name='UserProfile',
                object_id=profile.id,
                object_repr=str(profile),
                description=f'Rol actualizado para {user.username}'
            )
            
            messages.success(request, f'El rol de {user.username} ha sido actualizado.')
            return redirect('dashboard:user_management')
    else:
        form = UserRoleForm(instance=profile)
    
    context = {
        'form': form,
        'target_user': user,
        'profile': profile,
        'page_title': f'Editar Rol - {user.username}'
    }
    
    return render(request, 'dashboard/edit_user_role.html', context)

@login_required
def activity_log(request):
    """Vista del registro de actividades"""
    if not hasattr(request.user, 'userprofile') or request.user.userprofile.role not in ['admin', 'manager']:
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('dashboard:dashboard_home')
    
    # Filtros
    user_filter = request.GET.get('user', '')
    action_filter = request.GET.get('action', '')
    date_filter = request.GET.get('date', '')
    
    # Consulta base
    activities_query = ActivityLog.objects.select_related('user')
    
    # Aplicar filtros
    if user_filter:
        activities_query = activities_query.filter(user__id=user_filter)
    
    if action_filter:
        activities_query = activities_query.filter(action=action_filter)
    
    if date_filter:
        activities_query = activities_query.filter(timestamp__date=date_filter)
    
    activities = activities_query.order_by('-timestamp')[:100]  # Limitar a 100 registros
    
    # Lista de usuarios para el filtro
    users = User.objects.filter(is_active=True).order_by('username')
    
    context = {
        'activities': activities,
        'users': users,
        'user_filter': user_filter,
        'action_filter': action_filter,
        'date_filter': date_filter,
        'action_choices': ActivityLog.ACTION_CHOICES,
        'page_title': 'Registro de Actividades'
    }
    
    return render(request, 'dashboard/activity_log.html', context)
