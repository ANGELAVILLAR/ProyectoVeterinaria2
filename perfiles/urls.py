from django.urls import path
from core import views
from django import urls

from perfiles.views import SignOutView, SignUpView, BienvenidaView, SignInView


urlpatterns = [
    path(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    path(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    path(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    path(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
]








