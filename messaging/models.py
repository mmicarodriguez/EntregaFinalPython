from django.db import models

class Mensaje(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()

    def __str__(self):
        return self.nombre
