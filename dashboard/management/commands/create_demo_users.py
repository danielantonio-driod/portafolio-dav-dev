from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from dashboard.models import UserProfile
from contact.models import ContactMessage
from orders.models import Order
import random
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Crea usuarios de demostración y datos de prueba'

    def add_arguments(self, parser):
        parser.add_argument(
            '--with-data',
            action='store_true',
            help='Crear también datos de prueba (mensajes y órdenes)',
        )

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write('Creando usuarios de demostración...')
            
            # Crear superusuario admin
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@portfolio-django.com',
                    'first_name': 'Administrador',
                    'last_name': 'Sistema',
                    'is_staff': True,
                    'is_superuser': True,
                    'is_active': True
                }
            )
            if created:
                admin_user.set_password('admin123')
                admin_user.save()
                UserProfile.objects.create(
                    user=admin_user,
                    role='admin',
                    phone='+57 300 123 4567',
                    address='Bogotá, Colombia'
                )
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Usuario admin creado - Contraseña: admin123')
                )
            else:
                self.stdout.write('- Usuario admin ya existe')

            # Crear usuario gerente
            manager_user, created = User.objects.get_or_create(
                username='manager',
                defaults={
                    'email': 'manager@portfolio-django.com',
                    'first_name': 'María',
                    'last_name': 'García',
                    'is_staff': True,
                    'is_active': True
                }
            )
            if created:
                manager_user.set_password('manager123')
                manager_user.save()
                UserProfile.objects.create(
                    user=manager_user,
                    role='manager',
                    phone='+57 301 234 5678',
                    address='Medellín, Colombia'
                )
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Usuario manager creado - Contraseña: manager123')
                )
            else:
                self.stdout.write('- Usuario manager ya existe')

            # Crear usuario staff
            staff_user, created = User.objects.get_or_create(
                username='staff',
                defaults={
                    'email': 'staff@portfolio-django.com',
                    'first_name': 'Carlos',
                    'last_name': 'Rodríguez',
                    'is_staff': True,
                    'is_active': True
                }
            )
            if created:
                staff_user.set_password('staff123')
                staff_user.save()
                UserProfile.objects.create(
                    user=staff_user,
                    role='staff',
                    phone='+57 302 345 6789',
                    address='Cali, Colombia'
                )
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Usuario staff creado - Contraseña: staff123')
                )
            else:
                self.stdout.write('- Usuario staff ya existe')

            # Crear usuario cliente
            customer_user, created = User.objects.get_or_create(
                username='cliente',
                defaults={
                    'email': 'cliente@ejemplo.com',
                    'first_name': 'Ana',
                    'last_name': 'López',
                    'is_active': True
                }
            )
            if created:
                customer_user.set_password('cliente123')
                customer_user.save()
                UserProfile.objects.create(
                    user=customer_user,
                    role='customer',
                    phone='+57 303 456 7890',
                    address='Barranquilla, Colombia'
                )
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Usuario cliente creado - Contraseña: cliente123')
                )
            else:
                self.stdout.write('- Usuario cliente ya existe')

            # Crear datos de prueba si se solicita
            if options['with_data']:
                self.stdout.write('\nCreando datos de prueba...')
                self.create_sample_messages()
                self.create_sample_orders()

            self.stdout.write(
                self.style.SUCCESS('\n¡Usuarios de demostración creados exitosamente!')
            )
            self.stdout.write('\nCredenciales de acceso:')
            self.stdout.write('Admin: admin / admin123')
            self.stdout.write('Manager: manager / manager123')
            self.stdout.write('Staff: staff / staff123')
            self.stdout.write('Cliente: cliente / cliente123')

    def create_sample_messages(self):
        """Crear mensajes de contacto de prueba"""
        sample_messages = [
            {
                'name': 'Juan Pérez',
                'email': 'juan.perez@email.com',
                'phone': '+57 300 111 2222',
                'subject': 'Consulta sobre servicios',
                'message': 'Hola, me gustaría conocer más sobre sus servicios de desarrollo web. ¿Podrían enviarme información detallada?',
                'priority': 'medium',
                'status': 'new'
            },
            {
                'name': 'Laura Martínez',
                'email': 'laura.martinez@empresa.com',
                'phone': '+57 301 333 4444',
                'subject': 'Propuesta de proyecto',
                'message': 'Tenemos un proyecto de e-commerce que nos gustaría desarrollar. ¿Pueden ayudarnos? Necesitamos una cotización.',
                'priority': 'high',
                'status': 'in_progress'
            },
            {
                'name': 'Diego Silva',
                'email': 'diego.silva@gmail.com',
                'subject': 'Soporte técnico',
                'message': 'Estoy experimentando algunos problemas con la aplicación. ¿Podrían ayudarme a resolverlos?',
                'priority': 'urgent',
                'status': 'new'
            },
            {
                'name': 'Ana Rojas',
                'email': 'ana.rojas@startup.co',
                'phone': '+57 302 555 6666',
                'subject': 'Colaboración',
                'message': 'Somos una startup y nos interesa colaborar en proyectos de tecnología. ¿Podemos agendar una reunión?',
                'priority': 'low',
                'status': 'resolved'
            }
        ]

        for msg_data in sample_messages:
            ContactMessage.objects.get_or_create(
                email=msg_data['email'],
                defaults=msg_data
            )

        self.stdout.write('✓ Mensajes de contacto de prueba creados')

    def create_sample_orders(self):
        """Crear órdenes de prueba"""
        staff_users = User.objects.filter(is_staff=True)
        
        sample_orders = [
            {
                'customer_name': 'Empresa ABC',
                'customer_email': 'contacto@empresaabc.com',
                'customer_phone': '+57 300 777 8888',
                'customer_address': 'Calle 123 #45-67, Bogotá',
                'product_name': 'Desarrollo de sitio web corporativo',
                'product_description': 'Sitio web responsivo con sistema de gestión de contenidos',
                'quantity': 1,
                'unit_price': 2500000,
                'status': 'confirmed',
                'priority': 'high'
            },
            {
                'customer_name': 'María González',
                'customer_email': 'maria.gonzalez@freelancer.com',
                'customer_phone': '+57 301 888 9999',
                'customer_address': 'Carrera 7 #10-20, Medellín',
                'product_name': 'Aplicación móvil',
                'product_description': 'App para gestión de inventarios',
                'quantity': 1,
                'unit_price': 5000000,
                'status': 'in_progress',
                'priority': 'medium'
            },
            {
                'customer_name': 'TechStart SAS',
                'customer_email': 'info@techstart.co',
                'customer_address': 'Zona Rosa, Cali',
                'product_name': 'Sistema de facturación',
                'product_description': 'Sistema web para facturación electrónica',
                'quantity': 1,
                'unit_price': 3500000,
                'status': 'pending',
                'priority': 'urgent'
            }
        ]

        for order_data in sample_orders:
            if staff_users.exists():
                order_data['assigned_to'] = random.choice(staff_users)
            
            Order.objects.get_or_create(
                customer_email=order_data['customer_email'],
                defaults=order_data
            )

        self.stdout.write('✓ Órdenes de prueba creadas')