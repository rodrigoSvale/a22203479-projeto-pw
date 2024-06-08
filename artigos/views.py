from django.shortcuts import render, get_object_or_404
from .models import *

def author_detail_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    articles = Article.objects.filter(autor=author)
    context = {
        'author': author,
        'articles': articles
    }
    return render(request, "artigos/author_detail.html", context)

def article_detail_view(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(article=article).order_by('-date_posted')
    ratings = Rating.objects.filter(article=article)
    context = {
        'article': article,
        'comments': comments,
        'ratings': ratings
    }
    return render(request, "artigos/article_detail.html", context)

def comment_detail_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    context = {
        'comment': comment
    }
    return render(request, "artigos/comment_detail.html", context)

def rating_detail_view(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    context = {
        'rating': rating
    }
    return render(request, "artigos/rating_detail.html", context)

def articles_list_view(request):
    articles = Article.objects.all().order_by('-data_Postada')
    context = {
        'articles': articles
    }
    return render(request, "artigos/article_list.html", context)

def authors_list_view(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, "artigos/author_list.html", context)
def index_view(request):
    return render(request, "artigos/index.html")
