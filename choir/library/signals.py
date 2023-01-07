from django.db import models
from django.dispatch import receiver
from .models import Sheet, Document, Video, Audio


####=============sheet===================
@receiver(models.signals.post_delete, sender=Sheet)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
        instance.cover.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Sheet)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_file = instance.__class__.objects.get(id=instance.id).file.path
        old_cover = instance.__class__.objects.get(id=instance.id).cover.path
        try:
            new_cover = instance.cover.path
            new_file = instance.file.path
        except:
            new_cover = None
            new_file = None
        if new_file != old_file:
            import os
            if os.path.exists(old_file):
                os.remove(old_file)
        if new_cover != old_cover:
            import os
            if os.path.exists(old_cover):
                os.remove(old_cover)
    except:
        pass


##========Audio====================
@receiver(models.signals.post_delete, sender=Audio)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Audio)
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


# =============video==================
@receiver(models.signals.post_delete, sender=Video)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Video)
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


##===============document===========

@receiver(models.signals.post_delete, sender=Document)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.file.delete(save=False)
    except:
        pass


@receiver(models.signals.pre_save, sender=Document)
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
