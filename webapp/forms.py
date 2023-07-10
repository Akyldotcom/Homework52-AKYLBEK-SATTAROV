from django import forms
from django.forms import widgets

from webapp.models import Genre


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    author = forms.CharField(max_length=50, required=True, label="Автор")
    content = forms.CharField(max_length=2000, required=True, label="Контент")
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label="Типы")
