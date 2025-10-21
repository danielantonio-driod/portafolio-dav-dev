from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import ContactMessage
from .forms import ContactForm, ContactMessageUpdateForm

def contact_form(request):
    """Vista para mostrar y procesar el formulario de contacto"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(
                request, 
                f'¡Gracias {contact_message.name}! Tu mensaje ha sido enviado exitosamente. '
                'Nos pondremos en contacto contigo pronto.'
            )
            return redirect('contact:contact_success')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact_form.html', {
        'form': form,
        'page_title': 'Formulario de Contacto'
    })

def contact_success(request):
    """Vista de confirmación después de enviar el formulario"""
    return render(request, 'contact/contact_success.html', {
        'page_title': 'Mensaje Enviado'
    })

@login_required
def message_list(request):
    """Vista para listar mensajes de contacto (admin)"""
    # Verificar permisos
    if not hasattr(request.user, 'userprofile') or not request.user.userprofile.can_manage_messages():
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('home')
    
    # Filtros
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    is_read_filter = request.GET.get('is_read', '')
    
    # Consulta base
    messages_query = ContactMessage.objects.all()
    
    # Aplicar filtros
    if search_query:
        messages_query = messages_query.filter(
            Q(name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(subject__icontains=search_query) |
            Q(message__icontains=search_query)
        )
    
    if status_filter:
        messages_query = messages_query.filter(status=status_filter)
    
    if priority_filter:
        messages_query = messages_query.filter(priority=priority_filter)
    
    if is_read_filter:
        is_read = is_read_filter.lower() == 'true'
        messages_query = messages_query.filter(is_read=is_read)
    
    # Paginación
    paginator = Paginator(messages_query, 10)  # 10 mensajes por página
    page_number = request.GET.get('page')
    messages_page = paginator.get_page(page_number)
    
    # Estadísticas
    stats = {
        'total': ContactMessage.objects.count(),
        'new': ContactMessage.objects.filter(status='new').count(),
        'unread': ContactMessage.objects.filter(is_read=False).count(),
        'high_priority': ContactMessage.objects.filter(priority__in=['high', 'urgent']).count(),
    }
    
    context = {
        'messages': messages_page,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'is_read_filter': is_read_filter,
        'stats': stats,
        'status_choices': ContactMessage.STATUS_CHOICES,
        'priority_choices': ContactMessage.PRIORITY_CHOICES,
        'page_title': 'Gestión de Mensajes'
    }
    
    return render(request, 'contact/message_list.html', context)

@login_required
def message_detail(request, message_id):
    """Vista para ver y actualizar un mensaje específico"""
    # Verificar permisos
    if not hasattr(request.user, 'userprofile') or not request.user.userprofile.can_manage_messages():
        messages.error(request, 'No tienes permisos para acceder a esta sección.')
        return redirect('home')
    
    message = get_object_or_404(ContactMessage, id=message_id)
    
    # Marcar como leído si no lo está
    if not message.is_read:
        message.is_read = True
        message.save(update_fields=['is_read'])
    
    if request.method == 'POST':
        form = ContactMessageUpdateForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, 'El mensaje ha sido actualizado exitosamente.')
            return redirect('contact:message_detail', message_id=message.id)
    else:
        form = ContactMessageUpdateForm(instance=message)
    
    return render(request, 'contact/message_detail.html', {
        'message': message,
        'form': form,
        'page_title': f'Mensaje: {message.subject}'
    })

@login_required
@require_http_methods(["POST"])
def mark_as_read(request, message_id):
    """Vista AJAX para marcar un mensaje como leído/no leído"""
    if not hasattr(request.user, 'userprofile') or not request.user.userprofile.can_manage_messages():
        return JsonResponse({'success': False, 'error': 'Sin permisos'}, status=403)
    
    message = get_object_or_404(ContactMessage, id=message_id)
    message.is_read = not message.is_read
    message.save(update_fields=['is_read'])
    
    return JsonResponse({
        'success': True,
        'is_read': message.is_read,
        'message': 'Estado actualizado correctamente'
    })

@login_required
@require_http_methods(["POST"])
def delete_message(request, message_id):
    """Vista para eliminar un mensaje"""
    if not hasattr(request.user, 'userprofile') or not request.user.userprofile.can_manage_messages():
        messages.error(request, 'No tienes permisos para realizar esta acción.')
        return redirect('home')
    
    message = get_object_or_404(ContactMessage, id=message_id)
    message_subject = message.subject
    message.delete()
    
    messages.success(request, f'El mensaje "{message_subject}" ha sido eliminado.')
    return redirect('contact:message_list')
