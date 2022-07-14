
from django.urls import path
from django.views.generic import TemplateView

from webapp.models import Article
from webapp.views import IndexView, CreateArticle, UpdateArticle, delete_article, ArticleView, RedirectView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    # path("articles/", RedirectView.as_view(pattern_name="index")),
    path("articles/add/", CreateArticle.as_view(), name="create_article"),
    path('article/<int:pk>/', ArticleView.as_view(), name="article_view"),
    path('article/<int:pk>/update/', UpdateArticle.as_view(), name="update_article"),
    path('article/<int:pk>/delete/', delete_article, name="delete_article"),

]