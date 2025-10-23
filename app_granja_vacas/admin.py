from django.contrib import admin
from .models import Animal, Eventos_Sanitarios # ¡Cambiado!

admin.site.register(Animal)
admin.site.register(Eventos_Sanitarios)