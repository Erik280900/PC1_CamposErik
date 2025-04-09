from django import forms
from .models import Playlist, Song

# Formulario para crear una nueva Playlist
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['nombre', 'canciones']  # Puedes incluir más campos si lo deseas

# Formulario para agregar canciones a una Playlist
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['titulo', 'artista', 'enlace']
