from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Order
from .forms import OrderForm, OrderStatusUpdateForm
from dashboard.models import ActivityLog

@login_required
def order_list(request):
    """Vista para listar órdenes"""
    # Filtros
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')
    assigned_filter = request.GET.get('assigned', '')
    
    # Consulta base
    orders_query = Order.objects.select_related('assigned_to')
    
    # Filtrar por usuario si no es staff
    if not request.user.is_staff:
        orders_query = orders_query.filter(assigned_to=request.user)
    
    # Aplicar filtros
    if search_query:
        orders_query = orders_query.filter(
            Q(order_number__icontains=search_query) |
            Q(customer_name__icontains=search_query) |
            Q(customer_email__icontains=search_query) |
            Q(product_name__icontains=search_query)
        )
    
    if status_filter:
        orders_query = orders_query.filter(status=status_filter)
    
    if priority_filter:
        orders_query = orders_query.filter(priority=priority_filter)
    
    if assigned_filter:
        orders_query = orders_query.filter(assigned_to__id=assigned_filter)
    
    # Paginación
    paginator = Paginator(orders_query.order_by('-created_at'), 10)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)
    
    # Estadísticas
    stats = {
        'total': Order.objects.count(),
        'pending': Order.objects.filter(status='pending').count(),
        'in_progress': Order.objects.filter(status='in_progress').count(),
        'delivered': Order.objects.filter(status='delivered').count(),
    }
    
    context = {
        'orders': orders,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'assigned_filter': assigned_filter,
        'stats': stats,
        'status_choices': Order.STATUS_CHOICES,
        'priority_choices': Order.PRIORITY_CHOICES,
        'page_title': 'Gestión de Órdenes'
    }
    
    return render(request, 'orders/order_list.html', context)

@login_required
def order_detail(request, order_id):
    """Vista para ver detalles de una orden"""
    order = get_object_or_404(Order, id=order_id)
    
    # Verificar permisos
    if not request.user.is_staff and order.assigned_to != request.user:
        messages.error(request, 'No tienes permisos para ver esta orden.')
        return redirect('orders:order_list')
    
    if request.method == 'POST':
        form = OrderStatusUpdateForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                user=request.user,
                action='update',
                model_name='Order',
                object_id=order.id,
                object_repr=str(order),
                description=f'Estado actualizado a {order.get_status_display()}'
            )
            
            messages.success(request, 'El estado de la orden ha sido actualizado.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = OrderStatusUpdateForm(instance=order)
    
    context = {
        'order': order,
        'form': form,
        'page_title': f'Orden #{order.order_number}'
    }
    
    return render(request, 'orders/order_detail.html', context)

@login_required
def order_create(request):
    """Vista para crear una nueva orden"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para crear órdenes.')
        return redirect('orders:order_list')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                user=request.user,
                action='create',
                model_name='Order',
                object_id=order.id,
                object_repr=str(order),
                description=f'Nueva orden creada: {order.order_number}'
            )
            
            messages.success(request, f'La orden #{order.order_number} ha sido creada exitosamente.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = OrderForm()
    
    context = {
        'form': form,
        'page_title': 'Crear Nueva Orden'
    }
    
    return render(request, 'orders/order_create.html', context)

@login_required
def order_edit(request, order_id):
    """Vista para editar una orden"""
    order = get_object_or_404(Order, id=order_id)
    
    # Verificar permisos
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para editar órdenes.')
        return redirect('orders:order_list')
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            
            # Registrar actividad
            ActivityLog.objects.create(
                user=request.user,
                action='update',
                model_name='Order',
                object_id=order.id,
                object_repr=str(order),
                description=f'Orden editada: {order.order_number}'
            )
            
            messages.success(request, 'La orden ha sido actualizada exitosamente.')
            return redirect('orders:order_detail', order_id=order.id)
    else:
        form = OrderForm(instance=order)
    
    context = {
        'form': form,
        'order': order,
        'page_title': f'Editar Orden #{order.order_number}'
    }
    
    return render(request, 'orders/order_edit.html', context)

@login_required
@require_http_methods(["POST"])
def order_delete(request, order_id):
    """Vista para eliminar una orden"""
    if not request.user.is_staff:
        messages.error(request, 'No tienes permisos para eliminar órdenes.')
        return redirect('orders:order_list')
    
    order = get_object_or_404(Order, id=order_id)
    order_number = order.order_number
    
    # Registrar actividad antes de eliminar
    ActivityLog.objects.create(
        user=request.user,
        action='delete',
        model_name='Order',
        object_id=order.id,
        object_repr=str(order),
        description=f'Orden eliminada: {order_number}'
    )
    
    order.delete()
    messages.success(request, f'La orden #{order_number} ha sido eliminada.')
    return redirect('orders:order_list')

@login_required
@require_http_methods(["POST"])
def update_order_status(request, order_id):
    """Vista AJAX para actualizar el estado de una orden"""
    order = get_object_or_404(Order, id=order_id)
    
    # Verificar permisos
    if not request.user.is_staff and order.assigned_to != request.user:
        return JsonResponse({'success': False, 'error': 'Sin permisos'}, status=403)
    
    new_status = request.POST.get('status')
    if new_status not in dict(Order.STATUS_CHOICES):
        return JsonResponse({'success': False, 'error': 'Estado inválido'}, status=400)
    
    old_status = order.status
    order.status = new_status
    order.save(update_fields=['status'])
    
    # Registrar actividad
    ActivityLog.objects.create(
        user=request.user,
        action='update',
        model_name='Order',
        object_id=order.id,
        object_repr=str(order),
        description=f'Estado cambiado de {old_status} a {new_status}'
    )
    
    return JsonResponse({
        'success': True,
        'new_status': order.status,
        'status_display': order.get_status_display(),
        'status_color': order.get_status_color()
    })
