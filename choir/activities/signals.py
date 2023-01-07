from django.db import models
from django.dispatch import receiver
from .models import Gallery, Act_video


####===============gallery==================
@receiver(models.signals.post_delete, sender=Gallery)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Gallery)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_file = instance.__class__.objects.get(id=instance.id).file.path
        try:
            new_file = instance.file.path
        except:
            new_file = None
        if new_file != old_file:
            import os
            if os.path.exists(old_file):
                os.remove(old_file)
    except:
        pass


####=================ACt_video======
@receiver(models.signals.post_delete, sender=Act_video)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Act_video)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_file = instance.__class__.objects.get(id=instance.id).file.path
        try:
            new_file = instance.file.path
        except:
            new_file = None
        if new_file != old_file:
            import os
            if os.path.exists(old_file):
                os.remove(old_file)
    except:
        pass
