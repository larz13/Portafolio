from django.db import models
from cloudinary.models import CloudinaryField


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = CloudinaryField('image')  # Se usa CloudinaryField en vez de ImageField
    link = models.URLField(blank=True)
    technologies = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Se guarda la fecha del envío

    def __str__(self):
        return f"Mensaje de {self.name} : {self.message}"