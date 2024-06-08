from django.urls import path
from . import views  # Importamos views para poder usar as suas funções

app_name = 'artigos'

urlpatterns = [
    path('authors/', views.authors_list_view, name='author-list'),
    path('authors/<int:author_id>/', views.author_detail_view, name='author-detail'),
    path('articles/', views.articles_list_view, name='index'), ## INDEX DA PAGINA
    path('articles/<int:article_id>/', views.article_detail_view, name='article-detail'),
    path('comments/<int:comment_id>/', views.comment_detail_view, name='comment-detail'),
    path('ratings/<int:rating_id>/', views.rating_detail_view, name='rating-detail'),
]
