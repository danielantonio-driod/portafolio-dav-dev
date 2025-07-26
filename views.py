from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
import json

@csrf_exempt
def contacto_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            nombre = data.get("nombre")
            email = data.get("email")
            mensaje = data.get("mensaje")

            contenido = f"Nombre: {nombre}\nEmail: {email}\nMensaje:\n{mensaje}"

            send_mail(
                subject=f"Nuevo mensaje de contacto: {nombre}",
                message=contenido,
                from_email="no-reply@tu-dominio.dev",  # Puede ser el mismo remitente configurado
                recipient_list=["d.arrietavega@gmail.com"],
                fail_silently=False,
            )

            return JsonResponse({"mensaje": "ok"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Método no permitido"}, status=405)
