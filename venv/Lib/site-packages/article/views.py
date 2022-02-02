
from django.views.generic.list import ListView

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy

from .models import Default


class KnowledgeListView(ListView):

    model = Default
    template_name = 'article/index.html'
    page_name = _('Cancer Knowledge')
