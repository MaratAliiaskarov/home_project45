from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from django.views import View

from webapp.models import Article, STATUS_CHOICES
from webapp.validate import article_validate
from  django.views.generic import TemplateView, RedirectView


class IndexView(View):
    def get(self, request):
        articles = Article.objects.order_by(("-updated_at"))
        context = {"articles": articles}
        return render(request, "index.html", context)

class MyRedirectView(RedirectView):
    url = "https://www.google.com/"


class ArticleView(TemplateView):
    template_name = "article_view.html"
    # extra_context = {"test": "test"}
    # def get_template_names(self):
    #     return "article_view.html"

    def get_context_data(self, **kwargs):
        pk = kwargs.get("pk")
        article = get_object_or_404(Article, pk=pk)
        kwargs["article"] = article
        return super().get_context_data(**kwargs)



def create_article(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CHOICES})
    else:
        project = request.POST.get("project")
        content = request.POST.get("content")
        author = request.POST.get("author")
        status = request.POST.get("status")
        new_article = Article(project=project, content=content, author=author, status=status)
        errors = article_validate(project, content, author)
        if errors:
            return render(request, "create.html", {"errors": errors, "article": new_article})
        new_article.save()
        #new_article = Article.objects.create(project=project, author=author, content=content, status=status)

        return redirect("article_view", pk=new_article.pk)



def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, "update.html", {"article": article})
    else:
        article.project = request.POST.get("project")
        article.content = request.POST.get("content")
        article.author = request.POST.get("author")
        errors = article_validate(article.project, article.content, article.author)
        if errors:
            return render(request, "update.html", {"article": article, "errors": errors})
        article.save()

        return redirect("article_view", pk=article.pk)


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        pass
        #return render(request, "delete.html", {"article": article})
    else:
        article.delete()

        return redirect("index")