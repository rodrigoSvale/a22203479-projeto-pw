from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100, null=True)
    ano = models.IntegerField()
    genero = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos_bandas/')
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns', null=True)
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    capa = models.ImageField(upload_to='capas_albuns/')

    def __str__(self):
        return f'{self.titulo} - {self.banda.nome}'

class Musica(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')
    titulo = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    spotify_link = models.URLField(blank=True)
    letra = models.TextField(default='', null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} - {self.duracao} - {self.album.banda.nome}'
