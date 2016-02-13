from django.contrib import admin
from dappr.models import RegistrationProfile

# Register your models here.
def approve_requests(modeladmin, request, queryset):
    pass
def reject_requests(modeladmin, request, queryset):
    pass
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'identity_confirmed', 'confirmation_key')
admin.site.register(RegistrationProfile, RegistrationAdmin)