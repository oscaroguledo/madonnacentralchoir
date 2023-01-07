from django.contrib import admin
from .models import Gallery, Act_video


# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Gallery, GalleryAdmin)


class Act_videoAdmin(admin.ModelAdmin):
    list_per_page = 20


admin.site.register(Act_video, Act_videoAdmin)
