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
    types = models.ManyToManyField('webapp.Type', related_name='articles', through='webapp.ArticleType',
                                   through_fields=('article', 'type'), blank=True)

    def __str__(self):
        return f"{self.pk} {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Type(AbstractModel):
    name = models.CharField(max_length=31, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Type"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"


class ArticleType(AbstractModel):
    article = models.ForeignKey('webapp.Article', related_name='article_types', on_delete=models.CASCADE,
                                verbose_name='Статья')
    type = models.ForeignKey('webapp.Type', related_name='type_articles', on_delete=models.CASCADE, verbose_name='Тип')

    def __str__(self):
        return "{} | {}".format(self.article, self.type)
