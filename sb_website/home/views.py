

# Create your views here.

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Partner
from .forms import SubscriptionForm
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render


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

def MembershipView(request):
    page_name = 'Membership Program'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, f'You successfully subscribed for news about Health Membership Program')
            return redirect('membership')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SubscriptionForm()

    ctx = {
        's_form': form,
        'page_name': page_name,
    }

    return render(request, 'home/membership.html', ctx)




class PartnerListView(ListView):

    model = Partner
    template_name = 'home/partner.html'
    page_name = 'Worldwide Partner'

    def get(self, request):
        partner_list = Partner.objects.all()
        ctx = {'partner_list': partner_list, 'page_name': self.page_name}
        return render(request, self.template_name, ctx)




