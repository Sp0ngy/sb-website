from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Partner, InfoBox

from .forms import SubscriptionForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
import json
from django.core.mail import send_mail

from article import models



class CustomTemplateView(TemplateView):

    """
    Sub-class of the TemplateView to pass the page_name automatically in.
    """

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = self.page_name
        return context


class HomeInfoListView(ListView):

    model = InfoBox
    template_name = 'home/home.html'
    page_name = pgettext_lazy('override default', 'Home')

    def get(self, request):
        info_list = InfoBox.objects.all()
        ctx = {
            'info_list': info_list,
            'page_name': self.page_name,
            'article_category': models.ArticleCategory.objects.order_by('-created_at'),
            'article_list': models.Article.objects.order_by('-created_at'),
        }
        return render(request, self.template_name, ctx)


class PrivateServiceView(CustomTemplateView):
    template_name = 'home/private_service.html'
    page_name = 'Private Service'

class ProfessionalServiceView(CustomTemplateView):
    template_name = 'home/professional_service.html'
    page_name = 'Professional Service'

class MaintenanceView(TemplateView):
    template_name = 'home/maintenance.html'

# Errors displayed as message because bootstrap is-invalid is not working
# Loop through each key and get error message
def get_form_messages_as_str(form, request, messagetype='warning'):

    # available messagetype arguments: info, warning, success
    # default: warning

    for key in form.errors:
                # gives JSON dictionary with key "message"
                error_json = form.errors.get(key).as_json()
                # Converts JSON to Python dictionary
                error_python = json.loads(error_json)
                # Gets value of key 'message'
                error_message = [value['message'] for value in error_python]

                # select method to call
                method_to_call = getattr(messages, messagetype)
                # pass arguments into method
                result = method_to_call(request, error_message[0])

def MembershipView(request):

    # TODO: Add email backend to subscription -> when Subcribe POST, send Mail, add view to cancel subscription for phone or mail

    page_name = 'Health Program'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, f'You successfully subscribed for news about our upcoming Health Program')

            return redirect('home:membership')
        else:
            get_form_messages_as_str(form, request, 'info')

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




