from django import forms

class ArticleForm(forms.Form):
    project = forms.CharField(max_length=50, required=True, label="Project")
    content = forms.CharField(max_length=3000, required=True, label="Content")
    author = forms.CharField(max_length=50, required=True, label="Author")
