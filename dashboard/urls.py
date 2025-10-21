from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('profile/', views.profile_view, name='profile'),
    path('users/', views.user_management, name='user_management'),
    path('users/<int:user_id>/edit-role/', views.edit_user_role, name='edit_user_role'),
    path('activity/', views.activity_log, name='activity_log'),
]