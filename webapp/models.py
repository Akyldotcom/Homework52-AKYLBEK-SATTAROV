from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="TITLE", choices=status_choices)
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="CREATOR", default="EMPTY")
    content = models.TextField(max_length=2000, verbose_name="CONTENT")


    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    def __str__(self):
        return f"{self.pk} {self.title}: {self.author}"

    class Meta:
        db_table = "articles"
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
