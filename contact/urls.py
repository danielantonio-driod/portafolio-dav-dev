from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # Formulario de contacto público
    path('', views.contact_form, name='contact_form'),
    path('success/', views.contact_success, name='contact_success'),
    
    # Gestión de mensajes (admin)
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:message_id>/', views.message_detail, name='message_detail'),
    path('messages/<int:message_id>/read/', views.mark_as_read, name='mark_as_read'),
    path('messages/<int:message_id>/delete/', views.delete_message, name='delete_message'),
]