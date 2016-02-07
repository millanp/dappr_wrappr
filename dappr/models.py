from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string

# Create your models here.
class RegistrationProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    identity_confirmed = models.BooleanField(default=False)
    confirmation_key = models.CharField(max_length=20)

@receiver(post_save, sender=RegistrationProfile)
def set_confirmation_key(sender, instance, created, **kwargs):
    if created:
        instance.confirmation_key = get_random_string(length=20)
        instance.save()