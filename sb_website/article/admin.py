from django.contrib import admin
from .models import Article, ArticleTemplate, ArticleCategory, Paragraph


#TODO: create admin docs, see https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/
class ArticleAdmin(admin.ModelAdmin):
    model = Article

    list_display = ['title', 'template', 'category', 'created_at']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Paragraph)
admin.site.register(ArticleTemplate)
admin.site.register(ArticleCategory)


# Register your models here.
