from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView

from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by("-updated_at")
        context = {"articles": articles}
        return render(request, "index.html", context)


class ArticleCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "create_article.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            genres = form.cleaned_data.pop("genres")
            article = Article.objects.create(title=form.cleaned_data.get("title"),
                                             content=form.cleaned_data.get("content"),
                                             author=form.cleaned_data.get("author")),

            article.genres.set(genres)
            return redirect("article_view", pk=article.pk)
        else:
            return render(request, "create_article.html", {"form": form})


def article_view(request, *args, pk, **kwrags):
    # article = get_object_or_404(Article, id=pk)
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponseNotFound("Not found ")
    return render(request, "article.html", {"article": article})


def article_update_view(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == "GET":
        form = ArticleForm(initial={
            "title": article.title,
            "author": article.author,
            "content": article.content,
            "genres": article.genres.all()
        })
        return render(request, "update_article.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            genres = form.cleaned_data.pop("genres")
            article.title = form.cleaned_data.get("title")
            article.content = form.cleaned_data.get("content")
            article.author = form.cleaned_data.get("author")
            article.save()
            article.genres.set(genres)
            return redirect("article_view", pk=article.pk)
        else:
            return render(request, "update_article.html", {"form": form})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == "GET":
        return render(request, "delete_article.html", {"article": article})
    else:
        article.delete()
        return redirect("index")


class ArticleDView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = get_object_or_404(Article, id=kwargs['pk'])
        return context

    def get_template_names(self):
        return "article.html"
