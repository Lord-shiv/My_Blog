from django.db.models.signals import post_save
form django.contrib.auth.models import User
form django.dispatch import receiver
from .models import Userprofile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Userprofile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.Userprofile.save()
