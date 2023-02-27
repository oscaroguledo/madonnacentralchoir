from django.urls import path
from . import views
urlpatterns = [
    path('', views.activities, name='activities'),
    path('gallery', views.gallery, name='gallery'),
    path('videos', views.video, name='act_videos'),
    path('<type>/<media>/upload_', views.upload, name='upload'),
]

