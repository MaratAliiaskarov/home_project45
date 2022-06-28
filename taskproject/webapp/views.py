from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from webapp.models import Article, STATUS_CHOICES


def index_view(request):
    articles = Article.objects.order_by(("-created_at"))
    context = {"articles": articles}
    return render(request, "index.html", context)


def article_view(request, pk):
    #pk = request.GET.get("pk")
    article = Article.objects.get(pk=pk)
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
