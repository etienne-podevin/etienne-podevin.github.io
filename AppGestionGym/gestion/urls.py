from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groupe', views.groupe, name='groupe'),
    path('adherent', views.adherent, name='adherent'),
    path('encadrant', views.encadrant, name='encadrant'),
]