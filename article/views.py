
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from .models import Article, ArticleCategory, Publication


class ArticleList(ListView):

    model = Article
    template_name = 'article/article_list.html'
    page_name = _('Cancer Knowledge')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleList, self).get_context_data()

        category_pk_list = list(ArticleCategory.objects.values_list('pk', flat=True).order_by('-created_at')[:5])

        context.update(
            {
                'article_category': ArticleCategory.objects.order_by('-created_at'),
                'article_category_pk_list': category_pk_list,
                'article_list': Article.objects.order_by('-created_at'),
                'page_name': self.page_name,
            }
        )
        return context

class ArticleDetail(DetailView):

    model = Article
    template_name = 'article/article_detail.html'

class PublicationList(ListView):

    model = Article
    template_name = 'article/publication.html'
    page_name = 'Publications'

    def get(self, request):
        publications = Publication.objects.all().order_by('-created_at')
        ctx = {'publication_list': publications, 'page_name': self.page_name}
        return render(request, self.template_name, ctx)


