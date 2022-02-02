from django import forms
from django.forms import ModelForm
from .models import Subscription
from django_countries.fields import CountryField

#
class SubscriptionForm(ModelForm):

    # !Validation!
    # Server-side: error_messages include Validation against model // tags are the one from the Model:
    # 'max_length', 'unique'
    # Client-side: Default Django field validation

    # id="validationCustom01" for bootstrap validation style
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name*',
            'value': False,
            'id': 'validationCustom01',
        }
    ), error_messages={'max_length': 'First Name: Please enter a maximum of 50 letters.'})

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name*',
            'value': False,
            'id': 'validationCustom02',
        }
    ), error_messages={'max_length': 'Last Name: Please enter a maximum of 50 letters.'})

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email*',
            'value': False,
            'id': 'validationCustom03',
        }
    ), error_messages={'unique': 'Email: A Subscription with this email already exists.'})

    # See docs https://pypi.org/project/django-countries/
    # Add Northern Part of Cyprus to List
    country = CountryField(blank_label='Select country*').formfield(widget=forms.Select(
        attrs={
            'class': 'form-select',
            'value': False,
            'id': 'validationCustom04',
            'style': '.custom-select',
        }
    ))

    phone = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
            'value': False,
            'id': 'validationCustom05',
        }
    ), help_text='Example: +90 141 4992834', required=False)

    terms_accepted = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'value': False,
            'id': 'validationCustom06',
        }
    ), label='Terms & Conditions*')

    class Meta:
        model = Subscription
        fields = ['first_name', 'last_name', 'email', 'country', 'phone', 'terms_accepted']



