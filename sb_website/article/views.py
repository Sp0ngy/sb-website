
from django.views.generic import ListView, DetailView

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from .models import Article


class ArticleList(ListView):

    model = Article
    template_name = 'article/article_list.html'
    page_name = _('Cancer Knowledge')

class ArticleDetail(DetailView):

    model = Article
    template_name = 'article/article_detail.html'

