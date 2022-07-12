from django import forms
from django.forms import widgets

from webapp.models import Tag


class ArticleForm(forms.Form):
    project = forms.CharField(max_length=50, required=True, label="Project")
    content = forms.CharField(max_length=3000, required=True, label="Content")
    author = forms.CharField(max_length=50, required=True, label="Author", widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, label="Teg")
