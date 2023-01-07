import django.db.models as models
from django.dispatch import receiver
from .models import About


@receiver(models.signals.post_delete, sender=About)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    instance.constitution.delete(save=False)

@receiver(models.signals.pre_save, sender=About)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    old_constitution = instance.__class__.objects.get(id=instance.id).constitution.path
    try:
        new_constitution = instance.constitution.path
    except:
        new_constitution = None
    if new_constitution != old_constitution:
        import os
        if os.path.exists(old_constitution):
            os.remove(old_constitution)
