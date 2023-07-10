from django.db import models


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Article(AbstractModel):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="TITLE")
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="CREATOR", default="EMPTY")
    content = models.TextField(max_length=2000, verbose_name="CONTENT")
    genres = models.ManyToManyField('webapp.Genre', related_name='articles', through='webapp.ArticleGenre',
                                   through_fields=('article', 'genre'), blank=True)

    # status = models.ManyToManyField('webapp.Status', related_name='articles', through='webapp.ArticleStatus',
    #                                 through_fields=('article', 'status'), blank=True)

    def __str__(self):
        return f"{self.pk} {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Genre(AbstractModel):
    name = models.CharField(max_length=31, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Genre"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class ArticleGenre(AbstractModel):
    article = models.ForeignKey('webapp.Article', related_name='article_genres', on_delete=models.CASCADE,
                                verbose_name='Статья')
    genre = models.ForeignKey('webapp.Genre', related_name='genre_articles', on_delete=models.CASCADE, verbose_name='Тип')

    def __str__(self):
        return "{} | {}".format(self.article, self.genre)

# class Status(AbstractModel):
#     name = models.CharField(max_length=10, verbose_name='Статус')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "Status"
#         verbose_name = "Статус"
#         verbose_name_plural = "Статусы"
#
#
# class ArticleStatus(AbstractModel):
#     article = models.ForeignKey('webapp.Article', related_name='article_statuses', on_delete=models.CASCADE,
#                                 verbose_name='Статья')
#     status = models.ForeignKey('webapp.Status', related_name='status_articles', on_delete=models.CASCADE,
#                                verbose_name='Статус')
#
#     def __str__(self):
#         return "{} | {}".format(self.article, self.status)
