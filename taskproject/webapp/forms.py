import re

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Tag, Article
from webapp.validate import validate_title


# class ArticleForm(forms.Form):
#     project = forms.CharField(max_length=50, required=True, label="Project")
#     content = forms.CharField(max_length=3000, required=True, label="Content")
#     author = forms.CharField(max_length=50, required=True, label="Author", widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
#     tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, label="Teg")


class ArticleForm(forms.ModelForm):
    project = forms.CharField(max_length=50, required=True, label="Project", validators=[validate_title, ])

    class Meta:
        model = Article
        # fields = "__all__"
        fields = ["project", "author", "content", "tags"]

        widgets = {
            "tags": widgets.CheckboxSelectMultiple,
            "content": widgets.Textarea(attrs={"rows": 5, "placeholder": "enter content"})
        }

    # def clean_project(self):
    #     project = self.cleaned_data.get("project")
    #     if len(project) > 15:
    #         raise ValidationError("Nazvanie ne mojet byt bolshe 7 simvolov")
    #     return project


    def clean(self):
        author = self.cleaned_data.get("author")
        if not re.match("^[a-zA-Z]+$", author):
            self.add_error("author", ValidationError("Enter letters"))
        if self.cleaned_data.get("project") == self.cleaned_data.get("content"):
            raise ValidationError("Nazvanie i opisanie ne moget sovpodat")
        return super().clean()
