from django.contrib import admin
from .models import Partner, PartnerType, Subscription, InfoBox
from import_export.admin import ImportExportMixin

# Register your models here.
class PartnerAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Partner
    #display all fields: list_display = [field.name for field in Partner._meta.get_fields()]
    list_display = ['name', 'type', 'city', 'country', 'created_at']

class SubscriptionAdmin(ImportExportMixin, admin.ModelAdmin):
    model = Subscription
    list_display = ['first_name', 'last_name', 'country', 'internal_note']

class InfoBoxAdmin(ImportExportMixin, admin.ModelAdmin):
    model = InfoBox
    list_display = ['info_name', 'is_active']

class PartnerTypeAdmin(ImportExportMixin, admin.ModelAdmin):
    model = PartnerType

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerType, PartnerTypeAdmin)
admin.site.register(InfoBox, InfoBoxAdmin)

