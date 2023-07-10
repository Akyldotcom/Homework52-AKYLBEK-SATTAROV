from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound

from webapp.forms import ArticleForm
from webapp.models import Article


def articles_list_view(request):
    articles = Article.objects.order_by("-updated_at")
    context = {"articles": articles}
    return render(request, "index.html", context)


def article_create_view(request):
    if request.method == "GET":
        form = ArticleForm()
        return render(request, "create_article.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop("types")
            article = Article.objects.create(title=form.cleaned_data.get("title"),
                                             content=form.cleaned_data.get("content"),
                                             author=form.cleaned_data.get("author")),
            article.types.set(types)
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
            "content": article.content
        })
        return render(request, "update_article.html", {"form": form})
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = request.POST.get("title")
            article.content = request.POST.get("content")
            article.author = request.POST.get("author")
            article.save()
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
