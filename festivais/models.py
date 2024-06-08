from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.nome

class Localizacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Festival(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)
    bandas = models.ManyToManyField(Banda)
    ano = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_festivais/', null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.ano}'
