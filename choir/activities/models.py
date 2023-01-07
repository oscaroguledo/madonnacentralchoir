from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import CustomUser

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100000, )
    description = models.TextField(verbose_name='description', max_length=10000, blank=True)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='gallery')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-uploaded_at',)
        verbose_name_plural = "Galleries"


class Act_video(models.Model):
    title = models.CharField(verbose_name='Title', max_length=10000, )
    description = models.TextField(verbose_name='description', max_length=100000, blank=True)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True,)
    file = models.FileField(upload_to='Activity_videos/%Y/%m/%d/',
                            validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'flv','avi'])])

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-uploaded_at',)

