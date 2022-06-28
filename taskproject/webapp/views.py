from django.shortcuts import render

# Create your views here.
from webapp.models import Article


def index_view(request):
    articles = Article.objects.order_by(("-created_at"))
    context = {"articles": articles}
    return render(request, "index.html", context)


def article_view(request):
    pk = request.GET.get("pk")
    article = Article.objects.get(pk=pk)
    return render(request, "article_view.html", {"article": article})


def create_article(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:

        project = request.POST.get("project")
        content = request.POST.get("content")
        author = request.POST.get("author")
        new_article = Article.objects.create(project=project, author=author, content=content)
        context = {"article": new_article}

        return render(request, "article_view.html", context)
