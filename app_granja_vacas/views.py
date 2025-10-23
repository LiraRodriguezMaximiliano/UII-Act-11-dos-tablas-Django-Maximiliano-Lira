from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Eventos_Sanitarios 
from .forms import AnimalForm, EventosSanitariosForm 

# --- Vistas de Animal (CRUD) ---

def listar_animales(request):
    animales = Animal.objects.all().order_by('nombre')
    return render(request, 'listar_animales.html', {'animales': animales})

def detalle_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    eventos = Eventos_Sanitarios.objects.filter(animal=animal).order_by('-fecha') 
    return render(request, 'detalle_animal.html', {'animal': animal, 'eventos': eventos})

def crear_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_granja_vacas:listar_animales')
    else:
        form = AnimalForm()
    return render(request, 'formulario_animal.html', {'form': form, 'titulo': 'Registrar Nuevo Animal'})

def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('app_granja_vacas:detalle_animal', animal_id=animal.id)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'formulario_animal.html', {'form': form, 'titulo': 'Editar Información de Animal'})

def borrar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        animal.delete()
        return redirect('app_granja_vacas:listar_animales')
    return render(request, 'confirmar_borrar.html', {'animal': animal})


# --- Vistas de Eventos Sanitarios (Crear, Editar, Borrar) ---

def registrar_evento_sanitario(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == 'POST':
        form = EventosSanitariosForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.animal = animal
            evento.save()
            return redirect('app_granja_vacas:detalle_animal', animal_id=animal.id)
    else:
        form = EventosSanitariosForm()
    return render(request, 'formulario_evento.html', {
        'form': form, 
        'animal': animal,
        'titulo': f'Registrar Evento Sanitario para {animal.nombre}'
    })

def editar_evento_sanitario(request, evento_id):
    """Permite editar un evento sanitario existente."""
    evento = get_object_or_404(Eventos_Sanitarios, id=evento_id)
    animal = evento.animal 

    if request.method == 'POST':
        form = EventosSanitariosForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('app_granja_vacas:detalle_animal', animal_id=animal.id)
    else:
        form = EventosSanitariosForm(instance=evento)
        
    return render(request, 'formulario_evento.html', {
        'form': form, 
        'animal': animal,
        'titulo': f'Editar Evento Sanitario de {animal.nombre}'
    })
    
def borrar_evento_sanitario(request, evento_id):
    """Permite confirmar y borrar un evento sanitario."""
    evento = get_object_or_404(Eventos_Sanitarios, id=evento_id)
    animal = evento.animal

    if request.method == 'POST':
        evento.delete()
        return redirect('app_granja_vacas:detalle_animal', animal_id=animal.id)
    
    return render(request, 'confirmar_borrar_evento.html', {'evento': evento, 'animal': animal})