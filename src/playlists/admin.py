from django.contrib import admin
from .models import Playlist, Song

# Registro de la clase Song en el admin
class SongAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'artista', 'enlace')  # Lo que se muestra en la lista
    search_fields = ('titulo', 'artista')  # Habilita la búsqueda por título y artista

# Registro de la clase Playlist en el admin
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Lo que se muestra en la lista
    search_fields = ('nombre',)  # Habilita la búsqueda por nombre de playlist
    filter_horizontal = ('canciones',)  # Agrega un filtro para la relación many-to-many con canciones

# Registrar los modelos en el admin
admin.site.register(Song, SongAdmin)
admin.site.register(Playlist, PlaylistAdmin)
