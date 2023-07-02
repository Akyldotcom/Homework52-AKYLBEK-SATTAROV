from django.urls import path

from webapp.views import articles_list_view, article_create_view, article_view, article_delete_view, article_update_view

urlpatterns = [
    path('', articles_list_view, name="index"),
    path('articles/add/', article_create_view, name="article_add"),
    path('article/<int:pk>/', article_view, name="article_view"),
    path('article/<int:pk>/deleting/', article_delete_view, name="deleting_view"),
    path('article/<int:pk>/update/', article_update_view, name="article_update")
]
