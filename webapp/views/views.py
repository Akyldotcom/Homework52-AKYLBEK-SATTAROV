from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.html import urlencode
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, FormView, ListView, DeleteView, UpdateView

from webapp.forms import ArticleForm, SearchForm
from webapp.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/index.html"
    context_object_name = "articles"
    ordering = ("-updated_at",)
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context["form"] = self.form
        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.search_value)
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) |
                                       Q(author__icontains=self.search_value))
        return queryset


class ArticleCreateView(FormView):
    form_class = ArticleForm
    template_name = "articles/create_article.html"

    def form_valid(self, form):
        article = form.save()
        return redirect("article_view", pk=article.pk)


# def get(self, request, *args, **kwargs):
#     form = ArticleForm()
#     return render(request, "create_article.html", {"form": form})
#
# def post(self, request, *args, **kwargs):
#     form = ArticleForm(data=request.POST)
#     if form.is_valid():
#         genres = form.cleaned_data.pop("genres")
#         article = Article.objects.create(title=form.cleaned_data.get("title"),
#                                          content=form.cleaned_data.get("content"),
#                                          author=form.cleaned_data.get("author"),
#                                          )
#         article.genres.set(genres)
#         return redirect("article_view", pk=article.pk)
#     else:
#         return render(request, "create_article.html", {"form": form})


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/update_article.html"
    success_url = reverse_lazy("your-success-url")
    # def __init__(self, **kwargs):
    #     super().__init__(kwargs)
    #     self.article = None
    #
    # def dispatch(self, request, *args, **kwargs):
    #     self.article = self.get_object(kwargs.get("pk"))
    #     return super().dispatch(request, *args, **kwargs)
    #
    # def get_object(self, pk):
    #     return get_object_or_404(Article, id=pk)
    #
    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['instance'] = self.article
    #     return kwargs
    #
    # def form_valid(self, form):
    #     form.save()
    #     return redirect("article_view", pk=self.article.pk)
    #
    #

#
# def article_update_view(request, pk):
#     article = get_object_or_404(Article, id=pk)
#     if request.method == "GET":
#         form = ArticleForm(initial={
#             "title": article.title,
#             "author": article.author,
#             "content": article.content,
#             "genres": article.genres.all()
#         })
#         return render(request, "articles/update_article.html", {"form": form})
#     else:
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             genres = form.cleaned_data.pop("genres")
#             article.title = form.cleaned_data.get("title")
#             article.content = form.cleaned_data.get("content")
#             article.author = form.cleaned_data.get("author")
#             article.save()
#             article.genres.set(genres)
#             return redirect("article_view", pk=article.pk)
#         else:
#             return render(request, "articles/update_article.html", {"form": form})


# def article_view(request, *args, pk, **kwrags):
#     # article = get_object_or_404(Article, id=pk)
#     try:
#         article = Article.objects.get(id=pk)
#     except Article.DoesNotExist:
#         return HttpResponseNotFound("Not found ")
#     return render(request, "articles/article.html", {"article": article})

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete_article.html"
    success_url = reverse_lazy("index")


# def article_delete_view(request, pk):
#     article = get_object_or_404(Article, id=pk)
#     if request.method == "GET":
#         return render(request, "articles/delete_article.html", {"article": article})
#     else:
#         article.delete()
#         return redirect("index")


class ArticleDView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = get_object_or_404(Article, id=kwargs['pk'])
        return context

    def get_template_names(self):
        return "articles/article.html"
