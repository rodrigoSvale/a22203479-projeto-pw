from django import forms
from .models import Banda, Album, Musica
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {'password': forms.PasswordInput}

class BandaForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    class Meta:
        model = Banda
        fields = '__all__'
        help_texts = {
            'nome': 'Insira o nome da banda.',
            'nacionalidade': 'Insira a nacionalidade da banda.',
            'genero': 'Escolha o gênero musical da banda.',
            'ano': 'Insira o ano de formação da banda.',
            'foto': 'Insira uma fotografia da banda.',
            'biografia': 'Insira uma breve biografia da banda.',
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        help_texts = {
            'banda': 'Insira o nome da banda.',
            'titulo': 'Insira o título do álbum.',
            'ano': 'Insira o ano de lançamento.',
            'capa': 'Insira uma fotografia da capa do álbum.',
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        help_texts = {
            'album': 'Insira o nome do álbum.',
            'titulo': 'Insira o título da música.',
            'duracao': 'Insira a duração.',
            'spotify_link': 'Insira o link do Spotify.',
            'letra': 'Insira a letra da música.',
            'biografia': 'Insira uma breve biografia da música.',
        }
