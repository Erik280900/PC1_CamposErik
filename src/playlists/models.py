from django.db import models

# Create your models here.

class Song(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    enlace = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Playlist(models.Model):
    nombre = models.CharField(max_length=100)  # El nombre ahora expresa el mood
    canciones = models.ManyToManyField(Song, related_name='playlists')

    def __str__(self):
        return self.nombre
