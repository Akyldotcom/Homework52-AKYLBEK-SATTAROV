from django.urls import path

from webapp.views import articles_list_view, article_create_view, article_view

urlpatterns = [
    path('', articles_list_view, name="index"),
    path('articles/add/', article_create_view, name="article_add"),
    path('article/<int:pk>/', article_view, name="article_view")
]
