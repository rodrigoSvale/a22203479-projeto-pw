from django.db import models

class Curso(models.Model):
    apresentacao = models.CharField(max_length=100)
    objetivos = models.CharField(max_length=100)
    competencias = models.CharField(max_length=100)

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

class Docente(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, blank=True, null=True)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricularUnitReadableCode = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    docentes = models.ManyToManyField(Docente, related_name='disciplinas')

class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)
    versao = models.CharField(max_length=15, blank=True, null=True)

class Projeto(models.Model):
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    tecnologias_usadas = models.TextField()
    linguagens = models.ManyToManyField(LinguagemProgramacao, related_name='projetos')
    imagem = models.ImageField(upload_to='imagens_projetos/')
    link_video = models.URLField(max_length=200)
    link_github = models.URLField(max_length=200, blank=True, null=True)