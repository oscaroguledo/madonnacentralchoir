from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='authentication/logout.html'),
         name='logout'),
    path('editprofile/<username>', views.editprofile, name='editprofile'),
    path('profile/<username>', views.profile, name='profile'),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name='authentication/reset_password.html'),
         name='reset_password'),
    path('reset_password_sent',
         auth_views.PasswordResetDoneView.as_view(template_name='authentication/reset_password_sent.html'),
         name='password_reset_done'),
    path('reset<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'),
         name='password_reset_complete'),

]
