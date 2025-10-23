from django.db import models

class Animal(models.Model):
    SEXO_CHOICES = (
        ('H', 'Hembra'),
        ('M', 'Macho'),
        ('D', 'Desconocido'),
    )

    nombre = models.CharField(max_length=100, help_text="Nombre o número del animal")
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    estado_actual = models.CharField(max_length=100)
    foto_animal = models.ImageField(upload_to='img_animales/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.raza} ({self.get_sexo_display()})"

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animales"

class Eventos_Sanitarios(models.Model):
    # Enlace con la tabla Animal por ID y nombre
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='eventos_sanitarios')

    fecha = models.DateField()
    tratamiento = models.CharField(max_length=200)
    evento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=50)
    veterinario = models.CharField(max_length=100)

    def __str__(self):
        # Usamos self.animal.nombre para mostrar el nombre del animal
        return f"Evento Sanitario de {self.animal.nombre} - {self.evento} ({self.fecha})"

    class Meta:
        verbose_name = "Evento Sanitario"
        verbose_name_plural = "Eventos Sanitarios"