from django.db import models
from django_countries.fields import CountryField

# Create your models here.

#Export via MySQL Shell or Workbench in csv and import in Google MyMaps "DjangoMap"
class Partner(models.Model):
    name = models.CharField(max_length=50, null=False)
    #not in user: title = models.CharField(max_length=50, blank=True)
    type = models.ForeignKey('PartnerType', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=False)
    country = CountryField(blank_label='Select country')
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=False) #Längengrad
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=False) #Breitengrad

    #change default, implement resizing on upload if necessary
    image = models.ImageField(upload_to='home/media/uploads/', default='home/media/uploads/placeholder.png')

    #Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in admin list
    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Partner'

# types of partners, e.g. research, institution, applied medicine, ...
class PartnerType(models.Model):
    name = models.CharField(max_length=50, null=False)

    # Shows up in admin list
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Partner Type'


class Subscription(models.Model):
    first_name = models.CharField(max_length=50, null=False, verbose_name='First Name')
    last_name = models.CharField(max_length=50, null=False, verbose_name='Last Name')
    country = CountryField('Select country Test')
    email = models.EmailField(null=False, verbose_name='Email')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Phone')
    terms_accepted = models.BooleanField()

    # Standard
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

