from django.contrib import admin
from webapp.models import Article, Tag


class TagInline(admin.TabularInline):
    model = Article.tags.through

# class PersonAdmin(admin.ModelAdmin):
#     inlines = [
#         TagInline,
#     ]
#
# class GroupAdmin(admin.ModelAdmin):
#     inlines = [
#         MembershipInline,
#     ]
#     exclude = ('members', )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'project', 'author', 'status']
    list_display_links = ['project']
    list_filter = ['author']
    search_fields = ['project', 'content', 'status']
    fields = ['project', 'author', 'content', 'created_at', 'updated_at']
    readonly_fields = ['status', 'created_at', 'updated_at']
    # filter_horizontal = ['tags']
    inlines = [TagInline]


class TagsAdmin(admin.ModelAdmin):
    inlines = [TagInline]


admin.site.register(Tag, TagsAdmin)
admin.site.register(Article, ArticleAdmin)

