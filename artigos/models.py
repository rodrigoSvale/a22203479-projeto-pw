from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField()

    def __str__(self):
        return self.user.username

class Article(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='artigos')
    title = models.CharField(max_length=200)
    corpo = models.TextField()
    data_postada = models.DateTimeField(auto_now_add=True)
    ultima_modificacao = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# Modelo para os comentários
class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'comentario de {self.author.username} acerca {self.article.title}'

# Modelo para as avaliações/ratings
class Rating(models.Model):
    article = models.ForeignKey(Article, related_name='ratings', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'Rating {self.score} for {self.article.title}'
