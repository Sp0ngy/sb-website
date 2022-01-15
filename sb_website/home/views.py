

# Create your views here.

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Partner
from django.shortcuts import render

class CustomTemplateView(TemplateView):

    """
    Sub-class of the TemplateView to pass the page_name automatically in.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = self.page_name
        return context


class HomeView(CustomTemplateView):
    template_name = 'home/home.html'
    page_name = 'Home'

class PrivateServicesView(CustomTemplateView):
    template_name = 'home/private_services.html'
    page_name = 'Private Services'

class MembershipView(CustomTemplateView):
    template_name = 'home/membership.html'
    page_name = 'Membership Program'

class PartnerListView(ListView):

    model = Partner
    template_name = 'home/partner.html'
    page_name = 'Worldwide Partner'

    def get(self, request):
        partner_list = Partner.objects.all()
        ctx = {'partner_list': partner_list, 'page_name': self.page_name}
        return render(request, self.template_name, ctx)




