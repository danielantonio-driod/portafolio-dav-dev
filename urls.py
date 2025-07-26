from django.urls import path
from views import contacto_api

urlpatterns = [
    path("api/contacto/", contacto_api, name="contacto_api"),
]
