from django.contrib import admin
from .models import Article, ArticleImages, ArticleTemplate, ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = ['title', 'type', 'category']

admin.site.register(Article)
admin.site.register(ArticleImages)
admin.site.register(ArticleTemplate)
admin.site.register(ArticleCategory)


# Register your models here.
