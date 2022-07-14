from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.base_view import FormView as CustomFormView
from webapp.forms import ArticleForm
from webapp.models import Article
from django.views.generic import View, TemplateView, RedirectView, FormView



class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by("-created_at")
        context = {"articles": articles}
        return render(request, "index.html", context)


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


class MyRedirectView(RedirectView):
    url = "https://www.google.com/"

class CreateArticle(CustomFormView):
    form_class = ArticleForm
    template_name = "create.html"
    article = None

    def form_valid(self, form):
        # tags = form.cleaned_data.pop("tags")
        # self.article = Article.objects.create(**form.cleaned_data)
        # self.article.tags.set(tags)
        self.article = form.save()
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect("article_view", pk=self.article.pk)


# def create_article(request):
#     if request.method == "GET":
#         return render(request, "create.html", {'statuses': STATUS_CHOICES})
#     else:
#         project = request.POST.get("project")
#         content = request.POST.get("content")
#         author = request.POST.get("author")
#         status = request.POST.get("status")
#         new_article = Article(project=project, content=content, author=author, status=status)
#         errors = article_validate(project, content, author)
#         if errors:
#             return render(request, "create.html", {"errors": errors, "article": new_article})
#         new_article.save()
#         #new_article = Article.objects.create(project=project, author=author, content=content, status=status)
#
#         return redirect("article_view", pk=new_article.pk)


class UpdateArticle(FormView):
    form_class = ArticleForm
    template_name = "update.html"
    article = None


    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)


    def get_success_url(self):
        return reverse("article_view", kwargs={"pk": self.article.pk})


    # def get_inition(self):
    #     initial = {}
    #     for key in "project", "content", "author", "status":
    #         initial[key] = getattr(self.article, key)
    #     initial["tags"] = self.article.tags.all()
    #     return initial

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["instance"] = self.article
        return form_kwargs


    def form_valid(self, form):
        # tags = form.cleaned_data.pop("tags")
        # self.article.objects.update(**form.cleaned_data)
        # for key, value in form.cleaned_data.items():
        #     # if value is not None:
        #     setattr(self.article, key, value)
        # self.article.save()
        # self.article.tags.set(tags)
        self.article = form.save()
        return super().form_valid(form)


    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs.get("pk"))


# def update_article(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == "GET":
#         return render(request, "update.html", {"article": article})
#     else:
#         article.project = request.POST.get("project")
#         article.content = request.POST.get("content")
#         article.author = request.POST.get("author")
#         errors = article_validate(article.project, article.content, article.author)
#         if errors:
#             return render(request, "update.html", {"article": article, "errors": errors})
#         article.save()
#
#         return redirect("article_view", pk=article.pk)


def delete_article(request, **kwargs):
    pk = kwargs["pk"]
    article = get_object_or_404(Article, pk=pk)
    if request.method == "GET":
        pass
        #return render(request, "delete.html", {"article": article})
    else:
        article.delete()
        return redirect("index")