from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# Create your models here.


class About(models.Model):
    title = models.CharField(verbose_name='About Madonna Central Choir', help_text='About Madonna Central Choir', max_length=100000)
    history = models.TextField(verbose_name='History of Madonna Central Choir',max_length=255, blank=True)
    logo = models.ImageField(upload_to='logo', blank=True)
    Anthem = models.TextField(max_length=1000000, blank=True)
    contact = models.CharField(verbose_name='contact', max_length=100000, blank=True)
    commandments = models.TextField(verbose_name='commandments', max_length=100000, blank=True)
    slogan = models.CharField(verbose_name='slogan', max_length=100000, blank=True)
    motto = models.CharField(verbose_name='Motto', max_length=100000, blank=True)
    email = models.EmailField(verbose_name='Email', blank=True)
    constitution = models.FileField(upload_to='Constitution/%Y/%m/%d/',
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])], blank=True)
    date_created = models.DateField(verbose_name='The Date MCC was Created', null=True, blank=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = "Abouts"
