from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')
    list_display_links = ('id', 'title', 'text')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'article', 'parent_id')
    list_display_links = ('id', 'author', 'comment', 'article', 'parent_id')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)


