from django.contrib import admin

# Register your models here.
from webapp.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'author', 'status']
    list_display_links = ['project']
    list_filter = ['author']
    search_fields = ['project', 'content', 'status']
    fields = ['project', 'author', 'content', 'created_at', 'updated_at']
    readonly_fields = ['status', 'created_at', 'updated_at']


admin.site.register(Article, ArticleAdmin)

