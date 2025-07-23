from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from reservas.models import Resource, Booking
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = "Crea recursos y reservas de prueba para el calendario"

    def handle(self, *args, **kwargs):
        # Crear un usuario demo si no existe
        user, created = User.objects.get_or_create(username='demo_user')
        if created:
            user.set_password('demo1234')
            user.save()
            self.stdout.write(self.style.SUCCESS("Usuario demo_user creado."))

        # Crear un recurso demo si no existe
        recurso, creado = Resource.objects.get_or_create(name='Pista Pádel 1', defaults={'description': 'Pista de pádel exterior'})
        if creado:
            self.stdout.write(self.style.SUCCESS("Recurso Pista Pádel 1 creado."))

        # Crear reservas de prueba para los próximos días
        Booking.objects.all().delete()  # Limpia reservas anteriores
        hoy = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

        for i in range(5):  # 5 días
            for j in range(3):  # 3 reservas al día
                inicio = hoy + timedelta(days=i, hours=j * 2)
                fin = inicio + timedelta(hours=1)
                Booking.objects.create(
                    user=user,
                    resource=recurso,
                    start_time=inicio,
                    end_time=fin
                )
        self.stdout.write(self.style.SUCCESS("Reservas demo creadas correctamente."))
