from django import forms
from .models import Animal, Eventos_Sanitarios # ¡Cambiado!

class AnimalForm(forms.ModelForm):
    # Sobrescribir el campo de fecha para usar un widget de calendario (opcional)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Animal
        fields = ['nombre', 'raza', 'sexo', 'fecha_nacimiento', 'estado_actual', 'foto_animal']

class EventosSanitariosForm(forms.ModelForm):
    # Sobrescribir el campo de fecha
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Eventos_Sanitarios
        # 'animal' se manejará en la vista
        fields = ['fecha', 'tratamiento', 'evento', 'dosis', 'veterinario']