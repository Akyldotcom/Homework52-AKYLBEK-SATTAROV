from django import forms
from django.forms import widgets

from webapp.models import Type


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    author = forms.CharField(max_length=50, required=True, label="Автор")
    content = forms.CharField(max_length=2000, required=True, label="Контент",
                              widget=widgets.Textarea(
                                  attrs={"cols": 30, "rows": 5, "class": "test"})),
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label="Типы")
