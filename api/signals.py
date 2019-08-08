from django.contrib.auth.models import User
from api.models.Option import Option
from django.db.models.signals import post_save
from django.dispatch import receiver

# When a new User is saved create an options object for him
@receiver(post_save, sender=User)
def save_option(sender, instance, created, **kwargs):
    if created:
        option = Option(user=instance)
        option.save()