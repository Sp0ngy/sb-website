from django import forms
from django.forms import ModelForm
from .models import Subscription
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class SubscriptionForm(ModelForm):

    # !Validation!
    # Server-side: error_messages include Validation against model // tags are the one from the Model:
    # 'max_length', 'unique'
    # Client-side: Default Django field validation

    # id="validationCustom01" for bootstrap validation style
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('First Name*'),
            'value': False,
            'id': 'first_name',
        }
    ), error_messages={'max_length': _('First Name: Please enter a maximum of 50 letters.')})

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Last Name*'),
            'value': False,
            'id': 'last_name',
        }
    ), error_messages={'max_length': _('Last Name: Please enter a maximum of 50 letters.')})

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Email'),
            'value': False,
            'id': 'email',
        }
    ), required=False)

    # See docs https://pypi.org/project/django-countries/
    # Add Northern Part of Cyprus to List
    country = CountryField(blank_label='Select country*').formfield(widget=forms.Select(
        attrs={
            'class': 'form-select',
            'value': False,
            'id': 'country',
            'style': '.custom-select',
        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Phone*'),
            'value': False,
            'id': 'phone',
        }
    ), help_text=_('Example: +90 141 4992834'))

    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': _('Date of Birth*'),
            'value': False,
            'id': 'datepicker',
        }
    ),)

    terms_accepted = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'value': False,
            'id': 'terms_accepted',
        }
    ),)

    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email', 'country', 'phone', 'date_of_birth', 'terms_accepted']



