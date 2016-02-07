from django.contrib import admin
from dappr.models import RegistrationProfile

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'identity_confirmed', 'confirmation_key')
admin.site.register(RegistrationProfile, RegistrationAdmin)