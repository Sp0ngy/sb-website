
# TODO: translations see https://www.youtube.com/watch?v=AlJ8cGbk8ps

# Internationalization:
# - Specify all translation (via e.g. gettext(), reference  https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#internationalization-in-template-code)
# - Once: Create directory local in app
# - Add 'django.middleware.locale.LocaleMiddleware' in correct order: https://docs.djangoproject.com/en/1.11/topics/i18n/translation/#how-django-discovers-language-preference'
# - "django-admin makemessages" flag -l for LOCALE - specifies the country code:
# e.g. "django-admin makemessages -l tr" for Turkey country code...creates .mo file
# -  "django-admin compilemessages" compiles .mo file: e.g. "django-admin compilemessages -l tr"
# - Add {% load i18n %} to all templates
# - Check the .po file for #fuzzy tags, those have to be accepted manually by removing #fuzzy tag
# See checklist here https://stackoverflow.com/questions/2328185/django-i18n-common-causes-for-translations-not-appearing

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Partner, InfoBox
from .forms import SubscriptionForm
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
import json



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
        ctx = {'info_list': info_list, 'page_name': self.page_name}
        return render(request, self.template_name, ctx)

class PrivateServiceView(CustomTemplateView):
    template_name = 'home/private_service.html'
    page_name = 'Private Service'

def MembershipView(request):

    # TODO: Add email backend to subscription
    #   Check invalid-feedback w bootstrap v5 and if working remove else statement

    page_name = 'Membership Program'

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SubscriptionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.success(request, f'You successfully subscribed for news about Health Membership Program')
            return redirect('home:membership')
        else:
            # Errors displayed as message because bootstrap is-invalid is not working
            # Loop through each key and get error message
            for key in form.errors:
                # gives JSON dictionary with key "message"
                error_json = form.errors.get(key).as_json()
                # Converts JSON to Python dictionary
                error_python = json.loads(error_json)
                # Gets value of key 'message'
                error_message = [value['message'] for value in error_python]
                messages.warning(request, error_message[0])

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




