from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(sender)
    print(instance)
    print(created)

    if created:
        Profile.objects.create(user=instance)