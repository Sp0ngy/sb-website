from django.contrib import admin
from .models import Partner, PartnerType, Subscription
from import_export.admin import ImportExportMixin

# Register your models here.
class PartnerAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Partner
    #display all fields: list_display = [field.name for field in Partner._meta.get_fields()]
    list_display = ['name', 'type', 'city', 'country', 'created_at']

class SubscriptionAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Subscription
    list_display = ['first_name', 'last_name', 'country', 'email', 'phone', 'created_at']

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerType)
