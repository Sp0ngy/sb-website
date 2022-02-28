
from django.views.generic.list import ListView

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from .models import Article


class KnowledgeListView(ListView):

    model = Article
    template_name = 'article/index.html'
    page_name = _('Cancer Knowledge')
