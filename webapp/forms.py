from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Genre, Article


def validator_for_Author(value):
    if len(value) < 2:
        raise ValidationError('This value is too short')
    else:
        if len(value) > 50:
            raise ValidationError('This value is to long')


def validator_for_content(value):
    if len(value) < 10:
        raise ValidationError('this field should be longer')


class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, label="Название", validators=[validator_for_Author])
    content = forms.CharField(max_length=2000, required=True, label="Контент", validators=[validator_for_content])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Article
        fields = ["title", "author", "content", "genres"]
        widgets = {
            "content": widgets.Textarea(attrs={"cols": 30, "rows": 5, "class": "test"}),
            "genres": widgets.CheckboxSelectMultiple
        }

    # title = forms.CharField(max_length=50, required=True, label="Название", validators=[validator_for_Author])
    # author = forms.CharField(max_length=50, required=True, label="Автор")
    # content = forms.CharField(max_length=2000, required=True, label="Контент")
    # genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), label="Типы")

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('title') and cleaned_data.get('author') and \
                cleaned_data['author'] == cleaned_data['title']:
            raise ValidationError("title cant be the Author ")
        return cleaned_data

    # def clean_title(self):
    #     if len(value) < 2:
    #         raise ValidationError('This value is too short')
    #     else:
    #         if len(value) > 50:
    #             raise ValidationError('This value is to long')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label="Поиск")

