"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from playlists import views  # Cambia esta línea

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.playlist_list, name='playlist_list'),  # Agrega la vista para la lista de playlists
    path('playlist/create/', views.playlist_create, name='playlist_create'),
    path('playlist/<int:pk>/', views.playlist_detail, name='playlist_detail'),
    path('song/create/', views.song_create, name='song_create'),
]
