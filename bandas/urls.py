from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('bandas/<int:banda_id>/', views.banda_view, name='banda'),
    path('albuns/<int:album_id>/', views.album_view, name='album'),
    path('musicas/<int:musica_id>/', views.musica_view, name='musica'),
    path('nova_banda/', views.nova_banda_view, name='nova_banda'),
    path('edita_banda/<int:banda_id>/', views.edita_banda_view, name='edita_banda'),
    path('apaga_banda/<int:banda_id>/', views.apaga_banda_view, name='apaga_banda'),
    path('novo_album/<int:banda_id>/', views.novo_album_view, name='novo_album'),
    path('edita_album/<int:album_id>/', views.edita_album_view, name='edita_album'),
    path('apaga_album/<int:album_id>/', views.apaga_album_view, name='apaga_album'),
    path('nova_musica/<int:album_id>/', views.nova_musica_view, name='nova_musica'),
    path('edita_musica/<int:musica_id>/', views.edita_musica_view, name='edita_musica'),
    path('apaga_musica/<int:musica_id>/', views.apaga_musica_view, name='apaga_musica'),
    path('list/', views.banda_list_view, name='list'),  # Adicionado para corrigir o erro
]
