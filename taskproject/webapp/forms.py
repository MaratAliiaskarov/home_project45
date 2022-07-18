import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import widgets

from webapp.models import Tag, Article
from webapp.validate import validate_title


class ArticleForm(forms.ModelForm):
    project = forms.CharField(max_length=50, required=True, label="Project", validators=[RegexValidator(
        regex="^[a-zA-Z\s]+$",
        message="Enter letters",
    )])



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

        error_messages = {
            "content":{
                "required": "Pole obyazatelnoe"
            }
        }

    def clean_project(self):
        project = self.cleaned_data.get("project")
        if len(project) > 15:
            raise ValidationError("Nazvanie ne mojet byt bolshe 7 simvolov")
        return project


    def clean(self):
        author = self.cleaned_data.get("author")
        if not re.match("^[a-zA-Z\s]+$", author):
            self.add_error("author", ValidationError("Enter letters"))
        if self.cleaned_data.get("project") == self.cleaned_data.get("content"):
            raise ValidationError("Nazvanie i opisanie ne moget sovpodat")
        return super().clean()
