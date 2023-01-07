from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name='home'),
    path('library/<media>/uploadmedia_', views.upload, name='upload'),
    path('library', views.library, name='library'),
    path('library/audio', views.audio, name='audio'),
    path('library/audio/<audioname>', views.viewaudio, name='viewaudio'),
    path('library/sheet', views.sheet, name='sheet'),
    path('library/sheet/<sheettype>', views.sheet_type, name='sheet_type'),
    path('library/sheet/<sheettype>/<sheetname>', views.viewsheet, name='viewsheet'),
    path('library/mcc_documents', views.document, name='document'),
    path('library/mcc_documents/<title>', views.viewdoc, name='viewdoc'),
    path('library/<docname>/Upload_', views.uploaddoc, name='uploaddoc'),
    path('library/video', views.video, name='video'),


]