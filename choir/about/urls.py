from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('register', views.registers, name='registers'),
    path('register/<campus>', views.campus, name='campus'),
    path('register/<campus_print>/print', views.print_, name='print'),
    path('history', views.history, name='history'),

]