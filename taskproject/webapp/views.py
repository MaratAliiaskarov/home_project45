from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    articles = Article.objects.order_by(("-updated_at"))
    context = {"articles": articles}
    return render(request, "index.html", context)


def article_view(request, **kwargs):
    pk = kwargs.get("pk")
    article = get_object_or_404(Article, pk=pk)
    return render(request, "article_view.html", {"article": article})


def create_article(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS_CHOICES})
    else:

        project = request.POST.get("project")
        content = request.POST.get("content")
        author = request.POST.get("author")
        status = request.POST.get("status")
        new_article = Article.objects.create(project=project, author=author, content=content, status=status)

        return redirect("article_view", pk=new_article.pk)

        #context = {"article": new_article}
        #return HttpResponseRedirect(reverse("article_view", kwargs={"pk": new_article.pk}))
        #return HttpResponseRedirect(f"/article/{new_article.pk}")
        #return render(request, "article_view.html", context)

def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        return render(request, "update.html", {"article": article})
    else:
        article.project = request.POST.get("project")
        article.content = request.POST.get("content")
        article.author = request.POST.get("author")
        article.save()

        return redirect("article_view", pk=article.pk)
