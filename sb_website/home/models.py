from django.db import models

# Create your models here.

#Export via MySQL Shell or Workbench in csv and import in Google MyMaps "DjangoMap"
class Partner(models.Model):
    name = models.CharField(max_length=50, null=False)
    #not in user: title = models.CharField(max_length=50, blank=True)
    type = models.ForeignKey('PartnerType', on_delete=models.CASCADE)
    city = models.CharField(max_length=50, null=False)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=False) #Längengrad
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=False) #Breitengrad

    #change default, implement resizing on upload if necessary
    image = models.ImageField(upload_to='home/media/partneruploads/', default='home/placeholder.png')

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