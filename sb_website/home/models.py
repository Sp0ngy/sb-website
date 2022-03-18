from django.db import models
from django_countries.fields import CountryField

#Export via MySQL Shell or Workbench in csv and import in Google MyMaps "DjangoMap"
class Partner(models.Model):
    name = models.CharField(max_length=50, null=False)
    type = models.ForeignKey('PartnerType', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=False)
    country = CountryField(blank_label='Select country')
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=False) #Längengrad
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=False) #Breitengrad

    #change default, implement resizing on upload if necessary
    image = models.ImageField(upload_to='home/', default='home/placeholder.png')

    #Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Object Name
    def __str__(self):
        return self.name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Partner'

# types of partners, e.g. research, institution, applied medicine, ...
class PartnerType(models.Model):
    name = models.CharField(max_length=50, null=False)

    # Object Name
    def __str__(self):
        return self.name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Partner Type'


class Subscription(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=50, null=False, verbose_name='Last Name')
    country = CountryField('Country')
    # TODO: defaul=null
    email = models.EmailField(null=False, unique=True, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    internal_note = models.TextField(blank=True)
    terms_accepted = models.BooleanField()

    # Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Object Name
    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Subscriber'

class InfoBox(models.Model):
    is_active = models.BooleanField(blank=True)
    info_name = models.CharField(max_length=100, verbose_name='Info Name')
    info_text = models.TextField(verbose_name='Info Text', help_text='Infoboxes will only be shown in English on the website.')

    # Object Name
    def __str__(self):
        return self.info_name

    # String shown in Admin-Interface
    class Meta:
        verbose_name = 'Infoboxe'

