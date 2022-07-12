
from django.urls import path
from django.views.generic import TemplateView

from webapp.models import Article
from webapp.views import IndexView, create_article, update_article, delete_article, ArticleView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("articles/add/", create_article, name="create_article"),
    path('article/<int:pk>/', ArticleView.as_view(extra_context={"test": 5}), name="article_view"),
    path('article/<int:pk>/update/', update_article, name="update_article"),
    path('article/<int:pk>/delete/', delete_article, name="delete_article"),

]