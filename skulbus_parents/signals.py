from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Parent

@receiver(post_save, sender=User)
def create_or_update_parent(sender, instance, created, **kwargs):
    if created:
        Parent.objects.create(
            user=instance,
            firstname=instance.first_name,
            lastname=instance.last_name,
            username=instance.username,
            email=instance.email
        )