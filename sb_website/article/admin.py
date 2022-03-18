from django.contrib import admin
from .models import Article, ArticleTemplate, ArticleCategory, Paragraph
from import_export.admin import ImportExportMixin

#TODO: create admin docs, see https://docs.djangoproject.com/en/4.0/ref/contrib/admin/admindocs/
class ArticleAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Article

    list_display = ['title', 'template', 'category', 'created_at']

class ParagraphAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Paragraph

class ArticleTemplateAdmin(ImportExportMixin, admin.ModelAdmin):
    model = ArticleTemplate

class ArticleCategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    model = ArticleCategory

admin.site.register(Article, ArticleAdmin)
admin.site.register(Paragraph, ParagraphAdmin)
admin.site.register(ArticleTemplate, ArticleTemplateAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)


# Register your models here.
