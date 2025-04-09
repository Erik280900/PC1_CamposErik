from django.shortcuts import render, redirect
from .models import Playlist, Song
from .forms import PlaylistForm, SongForm

# Vista para ver todas las playlists
def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlist_list.html', {'playlists': playlists})

# Vista para crear una nueva playlist
def playlist_create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_list')  # Redirige a la lista de playlists
    else:
        form = PlaylistForm()
    return render(request, 'playlist_form.html', {'form': form})

# Vista para ver los detalles de una playlist
def playlist_detail(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    return render(request, 'playlist_detail.html', {'playlist': playlist})

# Vista para agregar una nueva canción
def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('playlist_list')  # Redirige a la lista de playlists
    else:
        form = SongForm()
    return render(request, 'song_form.html', {'form': form})
