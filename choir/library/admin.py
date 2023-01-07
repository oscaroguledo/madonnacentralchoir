from django.contrib import admin
from .models import *
# Register your models here.

class SheetAdmin(admin.ModelAdmin):
    list_per_page = 20
admin.site.register(Sheet, SheetAdmin)
class AudioAdmin(admin.ModelAdmin):
    list_per_page = 20
admin.site.register(Audio, AudioAdmin)
class VideoAdmin(admin.ModelAdmin):
    list_per_page = 20
admin.site.register(Video, VideoAdmin)
class DocumentAdmin(admin.ModelAdmin):
    list_per_page = 20
admin.site.register(Document, DocumentAdmin)

admin.site.site_title  =  "MCCAdmin"