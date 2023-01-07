from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile_Akpugo, CustomUser, Profile_National, Profile_Okija, Profile_Elele


@receiver(models.signals.post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.campus == 'Akpugo':
            Profile_Akpugo.objects.create(user=instance, firstname=instance.first_name, lastname=instance.last_name)
        if instance.campus == 'Elele':
            Profile_Elele.objects.create(user=instance, firstname=instance.first_name, lastname=instance.last_name)
        if instance.campus == 'Okija':
            Profile_Okija.objects.create(user=instance, firstname=instance.first_name, lastname=instance.last_name)
        if instance.campus == 'National':
            Profile_National.objects.create(user=instance, firstname=instance.first_name, lastname=instance.last_name)


@receiver(models.signals.post_save, sender=CustomUser)
def save_profile(sender, instance, created, **kwargs):
    if instance.campus == 'Akpugo':
        try:
            instance.profile_akpugo.save()
        except Exception:
            pass
    if instance.campus == 'Elele':
        try:
            instance.profile_elele.save()
        except Exception:
            pass
    if instance.campus == 'Okija':
        try:
            instance.profile_okija.save()
        except Exception:
            pass
    if instance.campus == 'National':
        try:
            instance.profile_national.save()
        except Exception:
            pass


@receiver(models.signals.post_delete, sender=Profile_Akpugo)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image.url != 'default.jpg':
        instance.image.delete(save=False)


@receiver(models.signals.pre_save, sender=Profile_Akpugo)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_image = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_image = instance.image.path
        except Exception:
            new_image = None
        if new_image != old_image:
            import os
            if os.path.exists(old_image):
                if 'default.jpg' not in os.path.exists(old_image):
                    os.remove(old_image)
    except Exception:
        pass
@receiver(models.signals.post_delete, sender=Profile_Elele)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image.url != 'default.jpg':
        instance.image.delete(save=False)


@receiver(models.signals.pre_save, sender=Profile_Elele)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_image = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_image = instance.image.path
        except Exception:
            new_image = None
        if new_image != old_image:
            import os
            if os.path.exists(old_image):
                if 'default.jpg' not in os.path.exists(old_image):
                    os.remove(old_image)
    except Exception:
        pass
@receiver(models.signals.post_delete, sender=Profile_Okija)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image.url != 'default.jpg':
        instance.image.delete(save=False)


@receiver(models.signals.pre_save, sender=Profile_Okija)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_image = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_image = instance.image.path
        except Exception:
            new_image = None
        if new_image != old_image:
            import os
            if os.path.exists(old_image):
                if 'default.jpg' not in os.path.exists(old_image):
                    os.remove(old_image)
    except Exception:
        pass
@receiver(models.signals.post_delete, sender=Profile_National)
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    if instance.image.url != 'default.jpg':
        instance.image.delete(save=False)


@receiver(models.signals.pre_save, sender=Profile_National)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_image = instance.__class__.objects.get(id=instance.id).image.path
        try:
            new_image = instance.image.path
        except Exception:
            new_image = None
        if new_image != old_image:
            import os
            if os.path.exists(old_image):
                if 'default.jpg' not in os.path.exists(old_image):
                    os.remove(old_image)
    except Exception:
        pass
