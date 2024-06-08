from django.contrib import admin

from .models import Author, Article, Comment, Rating

admin.site.register(Author)

admin.site.register(Article)

admin.site.register(Comment)

admin.site.register(Rating)