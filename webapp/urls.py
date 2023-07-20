from django.urls import path
from django.views.generic import RedirectView


from webapp.views.views import \
    ArticleListView, ArticleCreateView, ArticleDView,  ArticleDeleteView, ArticleUpdateView


app_name = "webapp"

urlpatterns = [
    path('', RedirectView.as_view(pattern_name="webapp:index")),
    path('articles/', ArticleListView.as_view(), name="index"),
    path('articles/add/', ArticleCreateView.as_view(), name="article_add"),
    path('article/<int:pk>/', ArticleDView.as_view(), name="article_view"),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name="article_update_view"),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete_view")
]
