# app_granja_vacas/urls.py

from django.urls import path
from . import views

app_name = 'app_granja_vacas'

urlpatterns = [
    # Rutas de Animal
    path('', views.listar_animales, name='listar_animales'),
    path('animal/<int:animal_id>/', views.detalle_animal, name='detalle_animal'),
    path('crear/', views.crear_animal, name='crear_animal'),
    path('editar/<int:animal_id>/', views.editar_animal, name='editar_animal'),
    path('borrar/<int:animal_id>/', views.borrar_animal, name='borrar_animal'),

    # Rutas de Eventos Sanitarios
    path('animal/<int:animal_id>/evento/nuevo/', views.registrar_evento_sanitario, name='registrar_evento'),
    
    # NUEVAS RUTAS
    path('evento/editar/<int:evento_id>/', views.editar_evento_sanitario, name='editar_evento'),
    path('evento/borrar/<int:evento_id>/', views.borrar_evento_sanitario, name='borrar_evento'),
]