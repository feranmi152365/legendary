from .models import Refferal
from Users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=CustomUser)
def post_save_create_refferal(sender, instance, created, *args, **kwargs):
    if created:
        Refferal.objects.create(user=instance)